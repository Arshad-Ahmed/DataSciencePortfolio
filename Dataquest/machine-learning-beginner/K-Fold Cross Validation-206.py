## 2. Partititioning the data ##

import pandas as pd

admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)

shuffled_index = np.random.permutation(admissions.index)
shuffled_admissions = admissions.loc[shuffled_index]
admissions = shuffled_admissions.reset_index()

fold = np.arange(644)
fold[0:129] = 1
fold[129:258] = 2
fold[258:387] = 3
fold[387:515] = 4
fold[515:644] = 5

admissions["fold"] = fold
admissions.head()

## 3. First iteration ##

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
train_iteration_one = admissions[admissions["fold"] != 1]
test_iteration_one = admissions[admissions["fold"] == 1]
model.fit(train_iteration_one[["gpa"]], train_iteration_one["actual_label"])

# Predicting
labels = model.predict(test_iteration_one[["gpa"]])
test_iteration_one["predicted_label"] = labels

matches = test_iteration_one["predicted_label"] == test_iteration_one["actual_label"]
correct_predictions = test_iteration_one[matches]
iteration_one_accuracy = len(correct_predictions) / len(test_iteration_one)
print(iteration_one_accuracy)



## 4. Function for training models ##

# Use np.mean to calculate the mean.
import numpy as np
fold_ids = [1,2,3,4,5]

def train_and_test(df,vlist):
    accuracy = []
    for i in vlist:
        model = LogisticRegression()
        train = df[df["fold"] != i]
        test = df[df["fold"] == i]
        model.fit(train[["gpa"]], train["actual_label"])
        
        labels = model.predict(test[["gpa"]])
        test["predicted_label"] = labels
        
        matches = test["predicted_label"] == test["actual_label"]
        correct_predictions = test[matches]
        acc = len(correct_predictions) / len(test)
        accuracy.append(acc)
        
    return accuracy
        
accuracies = train_and_test(admissions, [1,2,3,4,5])
average_accuracy = np.mean(accuracies)
print(average_accuracy)

## 5. Sklearn ##

from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score

admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)

kf = KFold(n=admissions.shape[0],n_folds=5,shuffle=True,random_state=8)
lr = LogisticRegression()
accuracies = cross_val_score(lr,admissions[["gpa"]],admissions[["actual_label"]],cv=kf)
average_accuracy = np.mean(accuracies)
print(average_accuracy)