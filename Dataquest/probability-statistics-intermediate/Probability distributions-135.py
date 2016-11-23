## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

prob_over_5000 = bikes["cnt"][bikes.cnt > 5000].shape[0]/bikes.shape[0]

## 4. Computing the distribution ##

import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))

def calc_binomp(p,n,k):
    comb = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    q = 1-p
    return (p ** k)*(q**(n-k))*comb



outcome_probs = [calc_binomp(0.39,30,i) for i in outcome_counts]

## 6. Simplifying the computation ##

import scipy
from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)
plt.bar(outcome_counts,binom.pmf(outcome_counts,30,0.39))
plt.show()

## 8. Computing the mean of a probability distribution ##

dist_mean = None
dist_mean = 30*0.39


## 9. Computing the standard deviation ##

dist_stdev = None

dist_stdev = (30 * 0.39 * (1-0.39))**0.5

## 10. A different plot ##

# Enter your answer here.

outcome_counts = linspace(0,10,11)
plt.bar(outcome_counts,binom.pmf(outcome_counts,10,0.39))
plt.show()

outcome_counts = linspace(0,100,101)
plt.bar(outcome_counts,binom.pmf(outcome_counts,100,0.39))
plt.show()

## 12. Cumulative density function ##

outcome_counts = linspace(0,30,31)
dist = binom.cdf(outcome_counts,30,0.39)
plt.plot(dist)


## 14. Faster way to calculate likelihood ##

left_16 = None
right_16 = None

left_16 = binom.cdf(linspace(0,16,17),30,0.39)
right_16 = 1 - left_16