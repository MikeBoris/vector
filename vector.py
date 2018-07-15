#!/usr/bin/env python3
#
#	07-14-18
#	multidimensional vector class
#
# 	example usage
#
# 	v = Vector(5)	# construct 5-dimensional <0, 0, 0, 0, 0>
#	v[1] = 23
#	v[-1] = 45
#	print(v[4])
#	u = v + v
#	print(u)
#	total = 0
#	for entry in v:
#		total += entry	# implicit iteration via __len__ and __getitem__
#
#
class Vector:
	""" Represent a vector in an multidimensional space."""

	def __init__(self, d):
		""" Create d-dimensional vector of 0s."""
		self._coords = [0] * d

	def __len__(self):
		""" Return the dimension of the vector."""

