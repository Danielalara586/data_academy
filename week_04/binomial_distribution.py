# -*- coding: utf-8 -*-
"""Binomial_Distribution.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fZJLiIONXR4GGJBEoYO4hg8wPjYxPFC5
"""

# Libraries
import numpy as np
from numpy.random import binomial
from scipy.stats import binom
from math import factorial
import matplotlib.pyplot as plt

"""## Bernoulli's Event Sequences
$$
P(k, n; p) = {n \choose k} p^k (1-p)^{n-k} = \frac{n!}{k!(n-k)!}p^k (1-p)^{n-k}
$$
"""

# Binomial Distribution Definition 
def my_binomial(k,n,p):
  return factorial(n)/(factorial(k)*(factorial(n-k))) * pow(p,k)*pow(1-p, n-k)

print(f'My binomial {my_binomial(2,3,0.5)}')
dist = binom(3,0.5)
dist.pmf(2)

"""
## Sequence Simulations With Random Generators"""

# Simulation with 100 balanced coin tosses
# Run this cell multiple times to observe the results variation.
p = 0.5
n = 3
binomial(n,p)

# We are going to do an experiment generating a sample of sets of flips of 3 coins
arr = []
for _ in range(100):
  arr.append(binomial(n,p))

def plot_histogram(num_trials):
  values = [0,1,2,3]
  arr = []
  for _ in range(num_trials):
    arr.append(binomial(3,0.5))
  
  simulated_distrib = np.unique(arr, return_counts=True)[1]/len(arr)
  theorical_distrib = [binom(3,0.5).pmf(k) for k in values]
  plt.bar(values, theorical_distrib, label = 'Theory', color = 'red')
  plt.bar(values, simulated_distrib, label = 'Simulation', alpha = 0.5, color = 'blue')
  plt.title(f'Simulation with {num_trials} experiments')

plot_histogram(20)
