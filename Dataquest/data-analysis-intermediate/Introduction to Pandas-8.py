## 3. Read a CSV File into a DataFrame ##


import pandas
food_info = pandas.read_csv("food_info.csv")
print(type(food_info))

## 4. Exploring the DataFrame ##

print(food_info.head(3))
dimensions = food_info.shape
print(dimensions)
num_rows = dimensions[0]
print(num_rows)
num_cols = dimensions[1]
print(num_cols)
first_twenty = food_info.head(20)

## 6. Selecting a Row in a DataFrame ##


hundredth_row = food_info.loc[99]
print(hundredth_row)

## 7. Data Types in Pandas ##

print(food_info.dtypes)


## 8. Selecting Multiple Rows in a DataFrame ##

print("Rows 3, 4, 5 and 6")
print(food_info.loc[3:6])

print("Rows 2, 5, and 10")
two_five_ten = [2,5,10]
print(food_info.loc[two_five_ten])
num_rows = food_info.shape[0]
last_rows = food_info.loc[num_rows-5:num_rows]

## 9. Selecting Individual Columns in a DataFrame ##

# Series object.
ndb_col = food_info["NDB_No"]
print(ndb_col)

# Display the type of the column to confirm it's a Series object.
print(type(ndb_col))
saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]

## 10. Selecting Multiple Columns in a DataFrame by Name ##

zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]
selenium_thiamin = food_info[['Selenium_(mcg)', 'Thiamin_(mg)']]

## 11. Practice ##

print(food_info.columns)
print(food_info.head(2))
col_names = food_info.columns.tolist()
gram_columns = []

for c in col_names:
    if c.endswith("(g)"):
        gram_columns.append(c)
gram_df = food_info[gram_columns]
print(gram_df.head(3))

## 12. Next Steps ##

print(food_info.columns)
print(food_info.head(2))

c = food_info.columns.tolist()
gram_columns = []

for i in c:
    if i.endswith("(g)"):
        gram_columns.append(i)
        
gram_df = food_info[gram_columns]
gram_df.head(3)