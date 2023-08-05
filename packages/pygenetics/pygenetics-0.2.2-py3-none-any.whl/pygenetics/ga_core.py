#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#	ga_core.py
#  
#	Developed in 2018 by Travis Kessler <travis.j.kessler@gmail.com>
#  
#	ga_core.py contains classes/functions for optimizing arbritrary
#	cost functions (given as an argument, *cost_fn*, to the Population
# 	object). The given cost function takes a 'feed_dict' argument, a 
# 	dictionary, containing keys and values (parameters) that the cost
# 	function will use to calculate and return a fitness score (a metric 
# 	to determine the performance of the cost function using the given 
# 	paramters).
#
#	Optionally, the Population object can take an arbitrary selection 
# 	function *select_fn* argument, a function used to rank Population 
# 	Members based on their fitness score. Arguments to this function 
# 	should include a list of Members and an integer to determine how 
# 	many Members are selected. This function should return a ranked/
# 	ordered list of Members. The probability of a ranked Member being
#	chosen is determined using a reverse exponential function (see
# 	'next_generation' method). By default, the selection function is
#	configured to rank the Members by lowest fitness score.
#

# Third party packages (open src.)
import random
import numpy as np
import types
from operator import add, sub

# PyGenetics source files
from pygenetics import selection_functions

class Population:
	'''
	Population object: contains parameters to tune, members of each generation
	'''

	def __init__(self, size, cost_fn, select_fn = selection_functions.minimize_best_n):
		'''
		Initialize the population with a population size *size*, a *cost_fn* to
		run for each member, and a *select_fn* to select/order member performance
		'''

		if size <= 0:
			raise ValueError('ERROR: population size cannot be <= 0!')
		self.pop_size = size
		if not callable(cost_fn):
			raise ValueError('ERROR: supplied cost function must be callable!')
		self.cost_fn = cost_fn
		if not callable(select_fn):
			raise ValueError('ERROR: supplied selection function must be callable!')
		self.select_fn = select_fn
		self.parameters = []
		self.members = []

	def __len__(self):
		'''
		len(Population) = number of members
		'''

		return len(self.members)

	class Parameter:
		'''
		Parameter object: created by "add_parameter"; stores relevant parameter
		attributes
		'''

		def __init__(self, name, min_val, max_val):

			self.name = name
			self.min_val = min_val
			self.max_val = max_val
			self.dtype = type(min_val + max_val)
			if self.dtype is not int and self.dtype is not float:
				raise ValueError('ERROR: unsupported paramter data type (must be int or float)!')

	class Member:
		'''
		Member object: holds a *feed_dict* with unique values for each population
		Parameter and a *fitness_score* calculated using the population's *cost_fn*
		'''

		def __init__(self, feed_dict, fitness_score):

			self.feed_dict = feed_dict
			self.fitness_score = fitness_score

	def add_parameter(self, name, min_val, max_val):
		'''
		Adds a parameter to the list of parameters with name *name*, a minimum 
		possible value *min_val*, and a maximum possible value *max_val*
		'''

		self.parameters.append(self.Parameter(name, min_val, max_val))

	def generate_population(self):
		'''
		Generates initial pop_size members (generation 0) for the population using
		randomly calculated parameter values within parameter value range
		'''

		# For each new member of the new population:
		for _ in range(self.pop_size):

			# Construct a parameter feed_dict for the member
			feed_dict = {}

			# For each population parameter:
			for param in self.parameters:

				# Add a random parameter value (within range) to feed_dict
				feed_dict[param.name] = self.__random_param_val(param.min_val, param.max_val, param.dtype)\

			# Compute the fitness score of the member using parameter feed_dict
			fitness_score = self.cost_fn(feed_dict)

			# Append the new member to population's list of members
			self.members.append(self.Member(feed_dict, fitness_score))

	def next_generation(self, num_survivors, mut_rate = 0.1, max_mut_amt = 0.1):
		'''
		Produces a new population generation using *num_survivors* members
		obtained through the population's select_fn (select_fn returns an
		ordered list of members, e.g. top performers). Optional arguments
		for mutation rate *mut_rate*, and maximum mutation amount *max_mut_amt*
		'''

		# Obtain sorted list of *num_survivors* members using population's select_fn
		selected_members = self.select_fn(self.members, num_survivors)

		# Compute inverse exponential probability distribution for parent choices
		#	(first elements of the list have a higher chance to be chosen)
		member_chosen_probs = list(reversed(np.logspace(0.0, 1.0, num = num_survivors, base = 10)))
		# Sum probabilities = 1
		member_chosen_probs = member_chosen_probs / sum(member_chosen_probs)

		# Reset population member list
		self.members = []

		# For each new population member (pop_size total members)
		for _ in range(self.pop_size):

			# Select each parent using calculated probabilities
			parent_1 = np.random.choice(selected_members, p = member_chosen_probs)
			parent_2 = np.random.choice(selected_members, p = member_chosen_probs)

			# Construct feed_dict for new member
			feed_dict = {}

			# For each population parameter:
			for param in self.parameters:

				# Choose which parent passes on its parameter value
				which_parent = random.uniform(0, 1)
				if which_parent < 0.5:
					feed_dict[param.name] = parent_1.feed_dict[param.name]
				else:
					feed_dict[param.name] = parent_2.feed_dict[param.name]

				# Apply mutation to the parameter (depends on mutation rate, mutation amount)
				feed_dict[param.name] = self.__mutate_parameter(feed_dict[param.name], param, mut_rate, max_mut_amt)

			# Compute the fitness score for the new member
			fitness_score = self.cost_fn(feed_dict)

			# Append new member to population's member list
			self.members.append(self.Member(feed_dict, fitness_score))

	@staticmethod
	def __random_param_val(min_val, max_val, dtype):
		'''
		Private, static method: returns a random parameter value in
		range [min_val, max_val] of type *dtype*
		'''
		if dtype is int:
			return random.randint(min_val, max_val)
		elif dtype is float:
			return random.uniform(min_val, max_val)
		else:
			return 0

	@staticmethod
	def __mutate_parameter(value, param, mut_rate, max_mut_amt):
		'''
		Private, static method: mutates a parameter *param*; chance
		of mutation dependent on *mut_rate*, maximum range of change
		dependent on *max_mut_amt*
		'''

		# Determine if mutation occurs:
		if random.uniform(0, 1) < mut_rate:

			# Determine mutation amount
			mut_amt = random.uniform(0, max_mut_amt)

			# Randomly add or subtract mutation amount
			op = random.choice((add, sub))

			# Apply mutation
			if param.dtype is int:
				new_val = op(value, int((param.max_val - param.min_val) * mut_amt))
			elif param.dtype is float:
				new_val = op(value, (param.max_val - param.min_val) * mut_amt)
			else:
				new_val = value

		# No mutation
		else:
			new_val = value

		# Ensure parameter is within specified range
		if new_val > param.max_val:
			new_val = param.max_val
		elif new_val < param.min_val:
			new_val = param.min_val

		# Return new parameter value
		return new_val