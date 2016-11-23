## 2. Drawing lines ##

import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3, 4, 5]
# Going by our formula, every y value at a position is the same as the x-value in the same position.
# We could write y = x, but let's write them all out to make this more clear.
y = [0, 1, 2, 3, 4, 5]

# As you can see, this is a straight line that passes through the points (0,0), (1,1), (2,2), and so on.
plt.plot(x, y)
plt.show()

# Let's try a slightly more ambitious line.
# What if we did y = x + 1?
# We'll make x an array now, so we can add 1 to every element more easily.
x = np.asarray([0, 1, 2, 3, 4, 5])
y = x + 1

# y is the same as x, but every element has 1 added to it.
print(y)

# This plot passes through (0,1), (1,2), and so on.
# It's the same line as before, but shifted up 1 on the y-axis.
plt.plot(x, x+10)
plt.show()

# By adding 1 to the line, we moved what's called the y-intercept -- where the line intersects with the y-axis.
# Moving the intercept can shift the whole line up (or down when we subtract).

## 3. Working with slope ##

import matplotlib.pyplot as plt
import numpy as np

x = np.asarray([0, 1, 2, 3, 4, 5])
# Let's set the slope of the line to 2.
y = 2 * x

# See how this line is "steeper" than before?  The larger the slope is, the steeper the line becomes.
# On the flipside, fractional slopes will create a "shallower" line.
# Negative slopes will create a line where y values decrease as x values increase.
plt.plot(x, y)
plt.show()


plt.plot(x, 4*x)
plt.show()
plt.plot(x, 0.5*x)
plt.show()
plt.plot(x, -2*x)
plt.show()

## 4. Starting out with linear regression ##

# The wine quality data is loaded into wine_quality
from numpy import cov

slope_density = cov(wine_quality.quality,wine_quality.density)[0,1]/wine_quality.density.var()

## 5. Finishing linear regression ##

from numpy import cov

# This function will take in two columns of data, and return the slope of the linear regression line.
def calc_slope(x, y):
  return cov(x, y)[0, 1] / x.var()


def cal_int(x,y):
    m = calc_slope(x,y)
    c = y.mean() - m*x.mean()
    return c

intercept_density = cal_int(wine_quality.density,wine_quality.quality)

## 6. Making predictions ##

from numpy import cov

def calc_slope(x, y):
  return cov(x, y)[0, 1] / x.var()

# Calculate the intercept given the x column, y column, and the slope
def calc_intercept(x, y, slope):
  return y.mean() - (slope * x.mean())

m = calc_slope(wine_quality.density,wine_quality.quality)
c = calc_intercept(wine_quality.density,wine_quality.quality,m)
predicted_quality = wine_quality.density.apply(lambda x: (m*x)+c)

## 7. Finding error ##

from scipy.stats import linregress

# We've seen the r_value before -- we'll get to what p_value and stderr_slope are soon -- for now, don't worry about them.
slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])

# As you can see, these are the same values we calculated (except for slight rounding differences)
print(slope)
print(intercept)

pred_y = (slope * wine_quality["density"]) + intercept
rss = sum((wine_quality["quality"] - pred_y)**2)

## 8. Standard error ##

from scipy.stats import linregress
import numpy as np

# We can do our linear regression
# Sadly, the stderr_slope isn't the standard error, but it is the standard error of the slope fitting only
# We'll need to calculate the standard error of the equation ourselves

slope, intercept, r_value, p_value, stderr_slope = linregress(wine_quality["density"], wine_quality["quality"])

predicted_y = np.asarray([slope * x + intercept for x in wine_quality["density"]])
residuals = (wine_quality["quality"] - predicted_y) ** 2
rss = sum(residuals)
stderr = (rss / (len(wine_quality["quality"]) - 2)) ** .5

def within_percentage(y, predicted_y, stderr, error_count):
  within = stderr * error_count

  differences = abs(predicted_y - y)
  lower_differences = [d for d in differences if d <= within]

  within_count = len(lower_differences)
  return within_count / len(y)

within_one = within_percentage(wine_quality["quality"], predicted_y, stderr, 1)
within_two = within_percentage(wine_quality["quality"], predicted_y, stderr, 2)
within_three = within_percentage(wine_quality["quality"], predicted_y, stderr, 3)