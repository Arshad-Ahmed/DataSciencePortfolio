## 2. Array Comparisons ##

countries_canada =  (world_alcohol[:,2] == 'Canada')
years_1984 = (world_alcohol[:,0] == '1984')


## 3. Selecting Elements ##

country_is_algeria = world_alcohol[:,2] == "Algeria"
country_algeria = world_alcohol[country_is_algeria,:]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Algeria")
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

## 5. Replacing Values ##

world_alcohol[:,0][world_alcohol[:,0] == "1986"] = "2014"
world_alcohol[:,3][world_alcohol[:,3] == "Wine"] = "Grog"

## 6. Replacing Empty Strings ##

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty, 4] = '0'

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

canada_1986  = world_alcohol[(world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Canada")]
canada_alcohol = canada_1986[:,4]
canada_alcohol[canada_alcohol == ''] = '0'

total_canadian_drinking = canada_alcohol.astype(float).sum()

## 10. Calculating Consumption for Each Country ##

totals = {}
is_year = world_alcohol[:,0] == "1989"
year = world_alcohol[is_year,:]

for country in countries:
    is_country = year[:,2] == country
    country_consumption = year[is_country,:]
    alcohol_column = country_consumption[:,4]
    is_empty = alcohol_column == ''
    alcohol_column[is_empty] = "0"
    alcohol_column = alcohol_column.astype(float)
    totals[country] = alcohol_column.sum()
    
        

## 11. Finding the Country That Drinks the Most ##

highest_value = 0
highest_key = None

for i in totals.items():
    if i[1] > highest_value:
        highest_key= i[0]
        highest_value = i[1]