## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

mean_group_a = np.mean(weight_lost_a)
print(mean_group_a)

mean_group_b = np.mean(weight_lost_b)
print(mean_group_b)

plt.hist(weight_lost_a)
plt.show()

plt.hist(weight_lost_b)
plt.show()

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation test ##

import numpy as np
mean_difference = 2.52
print(all_values)

mean_differences = []

for i in range(1000):
    group_a = []
    group_b = []
    
    for j in all_values:
        rand = np.random.rand()
        if rand >= 0.5:
            group_a.append(j)
        else:
            group_b.append(j)
    iteration_mean_difference = np.mean(group_b) - np.mean(group_a)
    mean_differences.append(iteration_mean_difference)

plt.hist(mean_differences)
plt.show()

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}

for i in mean_differences:
    if sampling_distribution.get(i,False):
        val = sampling_distribution.get(i)
        inc = val + 1
        sampling_distribution[i] = inc
    else:
        sampling_distribution[i] = 1
        
        
        

## 8. P value ##

frequencies = []

for i in sampling_distribution.keys():
    if i >= 2.52:
        frequencies.append(i)
    
    
p_value = np.sum(frequencies)/1000