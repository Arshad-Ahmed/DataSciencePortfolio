## 2. Calculating differences ##

female_diff = (10771 -16280.5)/16280.5
male_diff = (21790-16280.5)/16280.5

## 3. Updating the formula ##

female_diff = ((10771 -16280.5)**2)/16280.5
male_diff = ((21790-16280.5)**2)/16280.5
gender_chisq = female_diff + male_diff

## 4. Generating a distribution ##

chi_squared_values = []
from numpy.random import random
import matplotlib.pyplot as plt

for i in range(1000):
    sequence = random((32561,))
    sequence[sequence < .5] = 0
    sequence[sequence >= .5] = 1
    male_count = len(sequence[sequence == 0])
    female_count = len(sequence[sequence == 1])
    male_diff = (male_count - 16280.5) ** 2 / 16280.5
    female_diff = (female_count - 16280.5) ** 2 / 16280.5
    chi_squared = male_diff + female_diff
    chi_squared_values.append(chi_squared)

plt.hist(chi_squared_values)

## 6. Smaller samples ##

female_diff = (107.71 - 162.805)**2 /162.805
male_diff = (217.90 - 162.805)**2/162.805
gender_chisq = male_diff + female_diff


## 7. Sampling distribution equality ##

chi_squared_values = []

from numpy.random import random

for i in range(1000):
    sequence = random((300,))
    sequence[sequence < .5] = 0
    sequence[sequence >= .5] = 1
    male_count = len(sequence[sequence == 0])
    female_count = len(sequence[sequence == 1])
    female_diff = (male_count - 150)**2 /150
    male_diff = (female_count - 150)**2/150
    gender_chisq = male_diff + female_diff
    chi_squared = male_diff + female_diff
    chi_squared_values.append(chi_squared)

plt.hist(chi_squared_values)

## 9. Increasing degrees of freedom ##

white = (27816-26146.5)**2/26146.5
black = (3124-3939.9)**2/3939.9
api = (1039-944.3)**2/944.3
aie = (311-260.5)**2/260.5
other = (271-1269.8)**2/1269.8

race_chisq = white + black + api + aie+other

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np

obs = [27816,3124,1039,311,271]
exp = [36146.5,3939.9,944.3,260.5,1269.8]

_,race_pvalue = chisquare(obs, exp)