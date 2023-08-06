#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random
import sys
import datetime
from operator import le, ge
from bisect import bisect_left
from math import exp


class Chromosome:
    __slots__ = ['genes', 'fitness', 'age', 'strategy']
    def __init__(self, genes, fitness, age=None, strategy=None):
        """
        The `Chromosome` class is a container object to store the variables
        used in genetic evolution process. Think of it like an organism.

        :param genes: The genome of this organism
        :type genes: list
        :param fitness: The fitness object from mitochondria.fitness
        :type fitness: Fitness
        :param age: The age from which the organism has descended.
        :type age: int
        :param strategy: Specify how is the organism created.
        :type strategy: str
        """
        self.genes = genes
        self.fitness = fitness
        self.strategy = strategy
        self.age = age


class Evolution:
    def __init__(self, gene_set, fitness_func, mutation, *args, **kwargs):
        """
        The `Evolution` class is the main object that controls the evolution
        process.

        :param gene_set: The no. of unique genes of the organism's genome.
        :type gene_set: list
        :param fitness_func: The fitness function to optimize evolution.
        :type fitness_func: module
        :param mutation: The mutation object from helix.mutation
        :type mutation: Mutation
        """
        self.gene_set = gene_set
        self.fitness_func = fitness_func
        # Select the mutation strategy.
        self.mutation = mutation
        # Currently *gene_indices* are only used for swap mutation


    def generate_parent(self, num_genes, age=None, *args, **kwargs):
        """
        The function to emulate the genesis of the ancestor's gene.

        :param num_genes: The length of the genes for the Chromosome object.
        :param num_genes: int
        :param age: The age from which the organism has descended.
        :type age: int
        """
        genes = []
        while len(genes) < num_genes:
            sample_size = min(num_genes-len(genes), len(self.gene_set))
            genes.extend(random.sample(self.gene_set, sample_size))
        return Chromosome(genes, self.fitness_func(genes, *args, **kwargs),
                          age, strategy='create')

    def child_becomes_parent(self, child_fitness, fitness_history):
        """
        The stimulated annealing condition function.

        :param child_fitness: The child's fitness object.
        :type child_fitness: Fitness
        :param fitness_history: The history of fitness objects through the evolution.
        :type fitness_history: list(Fitness)
        """
        # Determine how far away is the child_fitness from best_fitness.
        # Find the  position of the child's fitness.
        index = bisect_left(fitness_history, child_fitness, 0, len(fitness_history))
        # Find the proxmity to the best fitness (last on the *fitness_history*)
        difference = len(fitness_history) - index
        # Convert it to a proportion.
        similar_proportion = difference / len(fitness_history)
        # Pick a random number, check if random number is smaller than
        # `exp(-similar_proportion)`, then child becomes parent.
        return random.random() < exp(-similar_proportion)

    def evolve(self, parent, max_age=None, keep_history=False, *args, **kwargs):
        """
        The evolve functions that:
         1. Mutate the child from the parent

         2. Check if the parent's fitness is > child's fitness.
           2a.  Continue the evolution if no max_age is required
           2b.1.  If yes, let the parent die out if max_age is reached
           2b.2.  Check the condition for stimulated annealing
           2b.2.1.  If condition, parent genes passed on to child fully
           2b.2.2   Else, reset the parent's age and make it the best_parent

         3. Check if the childn's fitness == parent's fitness.
           3a.  If yes, update the child's age to be parent's age + 1
               and the child becomes the new parent, process on the branch.

         4. Set the child's age to 0 and the child becomes the new parent to
            start a new branch.

         5. Check if the child's fitness is better than the best_parent's fitness
           5a.  if yes, the child becomes the best_parent and append its fitness
                to the fitness_history.

        :param parent: The parent chromosome.
        :type parent: Chromosome
        :param max_age: The hyperparameter that affects the rate of stimulated annealing.
        :type max_age: int
        :rtype: Chromosome
        """
        fitness_history = [parent.fitness]
        best_parent = parent
        this_generation = []

        while True:
            child = self.mutation.mutate(parent, self.gene_set, self.fitness_func,
                                         *args, **kwargs)
            # Keep logging each generation.
            this_generation.append(child)
            # To break the generations, we check that:
            # parent's fitness > child's fitness
            if parent.fitness >  child.fitness:
                if max_age is None:
                    continue
                # Let the parent die out if max_age is reached.
                parent.age += 1
                if max_age > parent.age:
                    continue
                # Simulated annealing.
                # If child is to become the new parent.
                if self.child_becomes_parent(child.fitness, fitness_history):
                    parent = child
                else: # Otherwise reset parent's age.
                    best_parent.age = 0
                    parent = best_parent
                continue

            # parent's fitness == child's fitness
            if child.fitness == parent.fitness:
                child.age = parent.age + 1
                parent = child
                continue

            # parent's fitness < child's fitness:
            child.age = 0
            parent = child

            # if best_parent's fitness < child's fitness:
            if child.fitness > best_parent.fitness:
                best_parent = child
                yield best_parent if keep_history == False else this_generation
                fitness_history.append(child.fitness)
                this_generation = []

    def generate(self, num_genes, optimal_fitness, random_seed=0, max_age=None,
                 keep_history=False, degree=1.0, epitome=None, *args, **kwargs):
        """
        The main function to start the evolution process.

        First the generation 0 parent will be generated and then the evolution
        starts with self.evolve().

        This function will print the best child in each evolution process and
        return the final child that matches the target based on the fitness.

        :param num_genes: The length of the genes for the Chromosome object.
        :param num_genes: int
        :param optimal_fitness: The optimal fitness that evolution should head towards.
        :type optimal_fitness: Fitness
        :param random_seed: The random seed.
        :type random_seed: int
        :param max_age: The hyperparameter that affects the rate of stimulated annealing.
        :type max_age: int
        :param degree: The hyperparameter how far evolution shoud go, 1.0 goes to perfection.
        :type degree: float
        :param epitome: The argument to kickstart devolution instead of evolution.
        :type epitome: list
        :rtype: Chromosome
        """
        random.seed(random_seed)
        generations_best = []

        if not epitome:
            # When evolving, fire genesis: Create generation 0 parent.
            gen0 = self.generate_parent(num_genes, age=0, *args, **kwargs)
        else: # When devolving, the *epitome* variable is used.
            gen0 = Chromosome(epitome, self.fitness_func(epitome, age=0, *args, **kwargs),
                              age=0, strategy='create')
        generations_best.append(gen0)

        # When evolving, if somehow, we met the criteria after gen0, banzai!
        if optimal_fitness < gen0.fitness and not epitome:
            return generations_best if keep_history == False else [[generations_best]]

        start_time = datetime.datetime.now()
        for child in self.evolve(gen0, max_age, keep_history=keep_history, *args, **kwargs):
            # Log time taken to reach better fitness.
            time_taken = datetime.datetime.now() - start_time
            best_child = child[-1] if keep_history else child
            print("{}\t{}\t{}".format(best_child.genes, best_child.fitness, time_taken), file=sys.stderr)
            generations_best.append(child)
            # Return child if fitness reached optimal.
            if optimal_fitness <= best_child.fitness:
                break
        return generations_best
