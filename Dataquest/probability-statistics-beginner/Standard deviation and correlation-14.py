## 2. The mean as the center ##

# Make a list of values
values = [2, 4, 5, -1, 0, 10, 8, 9]
# Compute the mean of the values
values_mean = sum(values) / len(values)
# Find the difference between each of the values and the mean by subtracting the mean from each value.
differences = [i - values_mean for i in values]
# This equals 0.  Try changing the values around and verifying that it equals 0 if you want.
print(sum(differences))

# We can use the median function from numpy to find the median
# The median is the "middle" value in a set of values -- if you sort the values in order, it's the one in the center (or the average of the two in the center if there are an even number of items in the set)
# You'll see that the differences from the median don't always add to 0.  You might want to play around with this and think about why that is.
from numpy import median

values_median = median(values)
median_difference_sum = sum(numpy.asarray(values) - values_median)

## 3. Finding variance ##

import matplotlib.pyplot as plt
import pandas as pd
# The nba data is loaded into the nba_stats variable.
# Find the mean value of the column
pf_mean = nba_stats["pf"].mean()
# Initialize variance at zero
variance = 0
# Loop through each item in the "pf" column
for p in nba_stats["pf"]:
    # Calculate the difference between the mean and the value
    difference = p - pf_mean
    # Square the difference -- this ensures that the result isn't negative
    # If we didn't square the difference, the total variance would be zero
    # ** in python means "raise whatever comes before this to the power of whatever number is after this"
    square_difference = difference ** 2
    # Add the difference to the total
    variance += square_difference
# Average the total to find the final variance.
variance = variance / len(nba_stats["pf"])

point_variance = nba_stats["pts"].var()

variance = 0
# Loop through each item in the "pf" column
for p in nba_stats["pf"]:
    # Calculate the difference between the mean and the value
    difference = p - pf_mean
    # Square the difference -- this ensures that the result isn't negative
    # If we didn't square the difference, the total variance would be zero
    # ** in python means "raise whatever comes before this to the power of whatever number is after this"
    square_difference = difference ** 2
    # Add the difference to the total
    variance += square_difference
# Average the total to find the final variance.
variance = variance / len(nba_stats["pf"])
point_mean = nba_stats["pts"].mean()
point_variance = 0
for p in nba_stats["pts"]:
    difference = p - point_mean
    square_difference = difference ** 2
    point_variance += square_difference
point_variance = point_variance / len(nba_stats["pts"])

## 4. Order of operations ##

# You might be wondering why multiplication and division are on the same level.
# It doesn't matter whether we do the multiplication first, or the division first -- the answer here will always be the same.
# In this case, we need to think of division as multiplication by a fraction -- otherwise, we'll be dividing more than we want to.
# Create a formula
a = 5 * 5 / 2
# Multiply by 1/2 instead of dividing by 2 -- the result is the same (2/2 == 2 * 1/2)
a_subbed = 5 * 5 * 1/2
a_mul_first = 25 * 1/2
a_div_first = 5 * 2.5
print(a_mul_first == a_div_first)

# The same thing is true for subtraction and addition
# In this case, we need to convert subtraction into adding a negative number -- if we don't we'll end up subtracting more than we expect
b = 10 - 8 + 5
# Add -8 instead of subtracting 8
b_subbed = 10 + -8 + 5
b_sub_first = 2 + 5
b_add_first = 10 + -3
print(b_sub_first == b_add_first)

c = 10 * 2 + 5
d = 1/2

## 5. Using parentheses ##

a = 50 * 50 - 10 / 5
a_paren = 50 * (50 - 10) / 5
# If we put multiple operations inside parentheses, the order of operations is used inside to determine the order.
a_paren = 50 * (50 - 10 / 5)

b = (10 * 100) + 100
c = (8 - 6) * 100

## 6. Fractional powers ##

a = 5 ** 2
# Raise to the fourth power
b = 10 ** 4

# Take the square root ( 3 * 3 == 9, so the answer is 3)
c = 9 ** (1/2)

# Take the cube root (4 * 4 * 4 == 64, so 4 is the cube root)
d = 64 ** (1/3)

e = 11 ** 5
f= 10000 ** (1/4)

## 7. Calculating standard deviation ##

# The nba stats are loaded into the nba_stats variable.

def calc_column_deviation(column):
    mean = column.mean()
    variance = 0
    for p in column:
        difference = p - mean
        square_difference = difference ** 2
        variance += square_difference
    variance = variance / len(column)
    return variance ** (1/2)

mp_dev = calc_column_deviation(nba_stats["mp"])
ast_dev = calc_column_deviation(nba_stats["ast"])

## 8. Find standard deviation distance ##

import matplotlib.pyplot as plt

plt.hist(nba_stats["pf"])
mean = nba_stats["pf"].mean()
plt.axvline(mean, color="r")
# We can calculate standard deviation by using the std() method on a pandas series.
std_dev = nba_stats["pf"].std()
# Plot a line one standard deviation below the mean
plt.axvline(mean - std_dev, color="g")
# Plot a line one standard deviation above the mean
plt.axvline(mean + std_dev, color="g")

# We can see how much of the data points fall within 1 standard deviation of the mean
# The more that falls into this range, the less spread out the data is
plt.show()

# We can calculate how many standard deviations a data point is from the mean by doing some subtraction and division
# First, we find the total distance by subtracting the mean
total_distance = nba_stats["pf"][0] - mean
# Then we divide by standard deviation to find how many standard deviations away the point is.
standard_deviation_distance = total_distance / std_dev

point_10 = nba_stats["pf"][9]
point_100 = nba_stats["pf"][99]

point_10_std = (point_10 -mean)/ std_dev
point_100_std = (point_100 -mean)/ std_dev

## 9. Working with the normal distribution ##

import numpy as np
import matplotlib.pyplot as plt
# The norm module has a pdf function (pdf stands for probability density function)
from scipy.stats import norm

# The arange function generates a numpy vector
# The vector below will start at -1, and go up to, but not including 1
# It will proceed in "steps" of .01.  So the first element will be -1, the second -.99, the third -.98, all the way up to .99.
points = np.arange(-10, 10, 0.1)

# The norm.pdf function will take points vector and turn it into a probability vector
# Each element in the vector will correspond to the normal distribution (earlier elements and later element smaller, peak in the center)
# The distribution will be centered on 0, and will have a standard devation of .3
probabilities = norm.pdf(points, 0, 2)

# Plot the points values on the x axis and the corresponding probabilities on the y axis
# See the bell curve?
plt.plot(points, probabilities)
plt.show()

## 10. Normal distribution deviation ##

# Housefly wing lengths in millimeters
wing_lengths = [36, 37, 38, 38, 39, 39, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 50, 51, 51, 51, 51, 52, 52, 53, 53, 54, 55]

mean = sum(wing_lengths) / len(wing_lengths)
variances = [(i - mean) ** 2 for i in wing_lengths]
variance = sum(variances)/ len(variances)
standard_deviation = variance ** (1/2)

standard_deviations = [(i - mean) / standard_deviation for i in wing_lengths]
def within_percentage(deviations, count):
    within = [i for i in deviations if i <= count and i >= -count]
    count = len(within)
    return count / len(deviations)

within_one_percentage = within_percentage(standard_deviations, 1)
within_two_percentage = within_percentage(standard_deviations, 2)
within_three_percentage = within_percentage(standard_deviations, 3)

## 11. Plotting correlations ##

import matplotlib.pyplot as plt

# This is plotting field goals attempted (number of shots someone takes in a season) vs point scored in a season
# Field goals attempted is on the x-axis, and points is on the y-axis
# As you can tell, they are very strongly correlated -- the plot is close to a straight line.
# The plot also slopes upward, which means that as field goal attempts go up, so do points.
# That means that the plot is positively correlated.
plt.scatter(nba_stats["fga"], nba_stats["pts"])
plt.show()

# If we make points negative (so the people who scored the most points now score the least, because 3000 becomes -3000), we can change the direction of the correlation
# Field goals are negatively correlated with our new "negative" points column -- the more free throws you attempt, the less negative points you score.
# We can see this because the correlation line slopes downward.
plt.scatter(nba_stats["fga"], -nba_stats["pts"])
plt.show()

# Now, we can plot total rebounds (number of times someone got the ball back for their team after someone shot) vs total assists (number of times someone helped another person score)
# These are uncorrelated, so you don't see the same nice line as you see with the plot above.
plt.scatter(nba_stats["trb"], nba_stats["ast"])
plt.show()

plt.scatter(nba_stats["fta"], nba_stats["pts"])
plt.show()

plt.scatter(nba_stats["stl"], nba_stats["pf"])
plt.show()

## 12. Measuring correlation ##

from scipy.stats.stats import pearsonr

# The pearsonr function will find the correlation between two columns of data.
# It returns the r value and the p value.  We'll learn more about p values later on.
r, p_value = pearsonr(nba_stats["fga"], nba_stats["pts"])
# As we can see, this is a very high positive r value -- close to 1
print(r)

# These two columns are much less correlated
r, p_value = pearsonr(nba_stats["trb"], nba_stats["ast"])
# We get a much lower, but still positive, r value
print(r)


r_fta_pts, p_value = pearsonr(nba_stats["fta"], nba_stats["pts"])
# We get a much lower, but still positive, r value
print(r)

r_stl_pf, p_value = pearsonr(nba_stats["stl"], nba_stats["pf"])
# We get a much lower, but still positive, r value
print(r)

## 13. Calculate covariance ##

# The nba_stats variable has been loaded.


def cov(x,y):
    import numpy as np
    meanx = np.mean(x)
    meany = np.mean(y)
    x -= meanx
    y -= meany
    return (np.sum(np.dot(x,y))/len(x))

cov_stl_pf = cov(nba_stats["stl"],nba_stats["pf"])
cov_fta_pts = cov(nba_stats["fta"],nba_stats["pts"])

## 14. Calculate correlation ##

from numpy import cov
# The nba_stats variable has already been loaded.

r_fta_blk = cov(nba_stats["fta"],nba_stats["blk"])[0,1]/(nba_stats["fta"].std()*nba_stats["blk"].std())
r_ast_stl = cov(nba_stats["ast"],nba_stats["stl"])[0,1]/(nba_stats["ast"].std()*nba_stats["stl"].std())