## 1. Shared index ##

import pandas as pd


fandango = pd.read_csv("fandango_score_comparison.csv")
fandango.head(2)
print(fandango.index)

## 2. Selecting using integer index ##

fandango = pd.read_csv('fandango_score_comparison.csv')
first_last = fandango.iloc[[0,len(fandango)-1]]

## 3. Custom Index ##

fandango = pd.read_csv('fandango_score_comparison.csv')

fandango_films = fandango.set_index("FILM", drop=False)

print(fandango_films.index)

## 4. Selection using custom index ##

m = ["The Lazarus Effect (2015)","Gett: The Trial of Viviane Amsalem (2015)","Mr. Holmes (2015)"]
best_movies_ever = fandango_films.loc[m]

## 6. Apply() over columns, practice ##

double_df = float_df.apply(lambda x: x*2)
print(double_df.head(1))

halved_df = float_df.apply(lambda x: x/2)

## 7. Apply() over rows ##

rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
print(rt_mt_deviations[0:5])

rt_mt_means = rt_mt_user.apply(lambda x: np.mean(x), axis=1)
rt_mt_means.head()