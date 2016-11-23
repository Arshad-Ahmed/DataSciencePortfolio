## 1. Introduction ##

import matplotlib.pyplot as plt
%matplotlib inline
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")

movie_reviews.plot.hist(subplots=True)


## 2. Mean ##

user_reviews = movie_reviews[["RT_user_norm",'Metacritic_user_nom','Fandango_Ratingvalue','IMDB_norm']]

rt_mean = user_reviews.mean()[0]
mc_mean = user_reviews.mean()[1]
fg_mean = user_reviews.mean()[2]
id_mean = user_reviews.mean()[3]

print(user_reviews.mean())

## 3. Variance and standard deviation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations
columns = ["RT_user_norm", "Metacritic_user_nom", "Fandango_Ratingvalue", "IMDB_norm"]
user_reviews = movie_reviews[columns]
user_reviews_variances = user_reviews.apply(calc_variance)

rt_var = user_reviews_variances["RT_user_norm"]
mc_var = user_reviews_variances["Metacritic_user_nom"]
fg_var = user_reviews_variances["Fandango_Ratingvalue"]
id_var = user_reviews_variances["IMDB_norm"]

rt_stdev = rt_var ** (1/2)
mc_stdev = mc_var ** (1/2)
fg_stdev = fg_var ** (1/2)
id_stdev = id_var ** (1/2)

print("Rotten Tomatoes (variance):", rt_var)
print("Metacritic (variance):", mc_var)
print("Fandango (variance):", fg_var)
print("IMDB (variance):", id_var)

print("Rotten Tomatoes (standard deviation):", rt_stdev)
print("Metacritic (standard deviation):", mc_stdev)
print("Fandango (standard deviation):", fg_stdev)
print("IMDB (standard deviation):", id_stdev)

## 4. Scatter plots ##

fig = plt.figure(figsize=(4,8))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)

ax1.scatter(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
ax2.scatter(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
ax3.scatter(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

## 5. Covariance ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

print("Covariance between Rotten Tomatoes and Fandango:", rt_fg_covar)
print("Covariance between Metacritic and Fandango", mc_fg_covar)
print("Covariance between IMDB and Fandango", id_fg_covar)

## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])
def calc_correlation(series_one, series_two):
    numerator = calc_covariance(series_one, series_two)
    series_one_std = calc_variance(series_one) ** (1/2)
    series_two_std = calc_variance(series_two) ** (1/2)
    denominator = series_one_std * series_two_std
    correlation = numerator / denominator
    return correlation

rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

print("Correlation between Rotten Tomatoes and Fandango", rt_fg_corr)
print("Correlation between Metacritic and Fandango", mc_fg_corr)
print("Correlation between IMDB and Fandango", id_fg_corr)