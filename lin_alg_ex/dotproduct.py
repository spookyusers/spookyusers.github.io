#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 16:08:33 2024

@author: kymd
"""

import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([2,5,4,7])
v2 = np.array([4,1,0,2])
dp = np.dot(v1,v2)

plt.plot([0,dp[0]], [0, dp[1]])
