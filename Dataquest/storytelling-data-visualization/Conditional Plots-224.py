## 2. Introduction to the Data Set ##

import pandas as pd

titanic = pd.read_csv("train.csv")
titanic.drop(["PassengerId","Name","Ticket","Cabin"],axis=1,inplace=True)
titanic.dropna(inplace=True)

## 3. Creating Histograms In Seaborn ##

import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(titanic["Age"])
plt.show()

## 4. Generating A Kernel Density Plot ##

sns.kdeplot(titanic["Age"], shade=True)
plt.xlabel("Age")
plt.show()

## 5. Modifying The Appearance Of The Plots ##

sns.kdeplot(titanic['Age'], shade=True)
sns.despine(left=True, bottom=True)
plt.xlabel('Age')

## 6. Conditional Distributions Using A Single Condition ##

g = sns.FacetGrid(titanic, col="Pclass", size=6)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 7. Creating Conditional Plots Using Two Conditions ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass",size=3)
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 8. Creating Conditional Plots Using Three Conditions ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass",hue="Sex")
g.map(sns.kdeplot, "Age", shade=True)
sns.despine(left=True, bottom=True)
plt.show()

## 9. Adding A Legend ##

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue="Sex", size=3)
g.map(sns.kdeplot, "Age", shade=True)
g.add_legend()
sns.despine(left=True, bottom=True)
plt.show()