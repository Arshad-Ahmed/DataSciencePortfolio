## 2. Introduction to the data ##


cnames = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]
cars = pd.read_table("auto-mpg.data", delim_whitespace=True, names=cnames)

print(cars.head())

## 3. Exploratory data analysis ##

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

cars.plot.scatter("weight","mpg",ax=ax1)
cars.plot.scatter("acceleration","mpg", ax=ax2)
plt.show()

## 5. Scikit-learn ##

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

inputs = cars[["weight"]].values
output = cars["mpg"].values

lr.fit(inputs,output)

## 6. Making predictions ##

import sklearn
from sklearn.linear_model import LinearRegression
lr = LinearRegression(fit_intercept=True)
lr.fit(cars[["weight"]], cars["mpg"])

predictions = lr.predict(cars[["weight"]])
predictions[0:5]
print(cars["mpg"].head())

## 7. Plotting the model ##

plt.scatter(cars["weight"],cars["mpg"], c='r')
plt.scatter(cars["weight"],predictions, c='b')
plt.show()

## 8. Error metrics ##

lr = LinearRegression()
lr.fit(cars[["weight"]], cars["mpg"])
predictions = lr.predict(cars[["weight"]])

from sklearn.metrics import mean_squared_error 
mse = mean_squared_error(cars["mpg"].values,predictions)
print(mse)

## 9. Root mean squared error ##

mse = mean_squared_error(cars["mpg"], predictions)
rmse= mse ** 0.5