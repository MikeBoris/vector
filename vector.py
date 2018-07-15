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
		return len(self._coords)

	def __getitem__(self, j):
		""" Return jth coordinate of vector."""
		return self._coords[j]

	def __setitem__(self, j, val):
		""" Set jth coordinate of vector to given value."""
		self._coords[j] = val

	def __add__(self, other):
		""" Return sum of the two vectors."""
		if len(self) != len(other):		# relies on __len__
			raise ValueError('dimensions must agree')
		# start w/ vector of 0s
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result

	def __eq__(self, other):
		""" Return True if vector has same coordinates as other."""
		return self._coords == other._coords

	def __ne__(self, other):
		""" Return True if vector differs from other."""
		return not self == other 	# relies on __eq__

	def __str__(self):
		""" Return string representation of vector."""
		return '<' + str(self._coords)[1:-1] + '>'	# adapt list representation

	


