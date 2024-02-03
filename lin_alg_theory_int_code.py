#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 08:56:39 2024

@author: kymd
"""

"""
Linear Algebra: Theory, Intuition, Code
Exercises
"""

"""
Linear combinations
"""

import numpy as np

l1 = -1
l2 = 2
l3 = -3

v1 = np.array([4,5,1])
v2 = np.array([-4,0,-4])
v3 = np.array([1,3,2])

combo = l1*v1 + l2*v2 + l3*v3

# test what happens when vectors are lists instead of numpy arrays

vec1 = [4,5,1]
vec2 = [-4,0,-4]
vec3 = [1,3,2]

lin_combo = l1*vec1 + l2*vec2 + l3*vec3

# interesting, it looks like the integers multiplied by the lists just 
# multiply the list as a whole item, like -1 times the list deletes the items


"""
Outer Product
"""

v1 = np.array([2,5,4,7])
v2 = np.array([4,1,0,2])

op = np.outer(v1,v2)

#print(op)

# practice problems

#a
v1 = np.array([-1,1])
v2 = np.array([2,3])
op = np.outer(v1,v2)


#b
v1 = np.array([4,6])
v2 = np.array([2,3])
op = np.outer(v1,v2)


#c
v1 = np.array([-1,0,1])
v2 = np.array([1,2,3])
op = np.outer(v1,v2)

""" Element-wise or Hadamard Multiplicaiton"""

# two sets of variables individually multiplied

v1 = np.array([2,5,4,7])
v2 = np.array([4,1,0,2])

u = np.array([-6,5])
v = np.array([-2,6])

print(op)