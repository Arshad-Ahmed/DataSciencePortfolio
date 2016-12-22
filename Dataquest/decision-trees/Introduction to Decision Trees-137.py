## 3. Converting categorical variables ##

# Convert a single column from text categories into numbers.
col = pandas.Categorical.from_array(income["workclass"])
income["workclass"] = col.codes
print(income["workclass"].head(5))
for name in ["education", "marital_status", "occupation", "relationship", "race", "sex", "native_country", "high_income"]:
    col = pandas.Categorical.from_array(income[name])
    income[name] = col.codes

## 5. Performing a split ##

# Enter your code here.

private_incomes = income[income["workclass"] == 4]
public_incomes = income[income["workclass"] != 4]

print(private_incomes.shape)
print(public_incomes.shape)

## 8. Entropy ##

math.log(3/5, 2)
print(entropy)
prob_0 = income[income["high_income"] == 0].shape[0] / income.shape[0]
prob_1 = income[income["high_income"] == 1].shape[0] / income.shape[0]
income_entropy = -(prob_0 * math.log(prob_0, 2) + prob_1 * math.log(prob_1, 2))

## 9. Information gain ##

import numpy

def calc_entropy(column):
    """
    Calculate entropy given a pandas Series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column.
    counts = numpy.bincount(column)
    # Divide by the total column length to get a probability.
    probabilities = counts / len(column)
    
    # Initialize the entropy to 0.
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy.
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)
    
    return -entropy

# Verify our function matches our answer from earlier.
# Verify our function matches our answer from earlier.
entropy = calc_entropy([1,1,0,0,1])
print(entropy)

information_gain = entropy - ((.8 * calc_entropy([1,1,0,0])) + (.2 * calc_entropy([1])))
print(information_gain)
income_entropy = calc_entropy(income["high_income"])

median_age = income["age"].median()

left_split = income[income["age"] <= median_age]
right_split = income[income["age"] > median_age]

age_information_gain = income_entropy - ((left_split.shape[0] / income.shape[0]) * calc_entropy(left_split["high_income"]) + ((right_split.shape[0] / income.shape[0]) * calc_entropy(right_split["high_income"])))

## 10. Finding the best split ##

def calc_information_gain(data, split_name, target_name):
    """
    Calculate information gain given a dataset, column to split on, and target.
    """
    # Calculate original entropy.
    original_entropy = calc_entropy(data[target_name])
    
    # Find the median of the column we're splitting.
    column = data[split_name]
    median = column.median()
    
    # Make two subsets of the data based on the median.
    left_split = data[column <= median]
    right_split = data[column > median]
    
    # Loop through the splits, and calculate the subset entropy.
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = (subset.shape[0] / data.shape[0]) 
        to_subtract += prob * calc_entropy(subset[target_name])
    
    # Return information gain.
    return original_entropy - to_subtract

# Verify that our answer is the same as in the last screen.
print(calc_information_gain(income, "age", "high_income"))

print(calc_information_gain(income, "age", "high_income"))

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]
information_gains = []
# Loop through and compute information gains.
for col in columns:
    information_gain = calc_information_gain(income, col, "high_income")
    information_gains.append(information_gain)

# Find the name of the column with the highest gain.
highest_gain_index = information_gains.index(max(information_gains))
highest_gain = columns[highest_gain_index]