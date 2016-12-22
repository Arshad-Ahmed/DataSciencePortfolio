## 3. Euclidean distance ##

selected_player = nba[nba["player"] == "LeBron James"].iloc[0]
distance_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']

import math
def euclidean_distance(row):
    inner_value = 0
    for k in distance_columns:
        inner_value += (row[k] - selected_player[k]) ** 2
    return math.sqrt(inner_value)

lebron_distance = nba.apply(euclidean_distance, axis=1)


## 4. Normalizing columns ##

nba_numeric = nba[distance_columns]


nba_normalized = (nba_numeric -nba_numeric.mean())/nba_numeric.std()

## 5. Finding the nearest neighbor ##

from scipy.spatial import distance

# Fill in NA values in nba_normalized
nba_normalized.fillna(0, inplace=True)

# Find the normalized vector for lebron james.
lebron_normalized = nba_normalized[nba["player"] == "LeBron James"]

# Find the distance between lebron james and everyone else.
euclidean_distances = nba_normalized.apply(lambda row: distance.euclidean(row, lebron_normalized), axis=1)

most_similar_to_lebron = 'Carmelo Anthony'

## 8. Computing error ##

actual = test[y_column]
import numpy as np

mse = np.sum((predictions-actual)**2)/len(actual)
              
        