## 1. Spark DataFrame ##

with open('census_2010.json') as f:
    for i in range(0,4):
        print(f.readlines())
    

## 3. Schema ##

sqlCtx = SQLContext(sc)
df = sqlCtx.read.json("census_2010.json")
print(df.printSchema())

## 4. Pandas vs Spark DataFrames ##

df.show()

## 5. Row object ##

first_five = df.head(5)
for i in first_five:
    print(i.age)

## 6. Selecting columns ##

df.select('age','males','females').show()

## 7. Filtering rows ##

fifty_plus = df[df.age > 5]
fifty_plus.show()

## 8. Comparing columns ##

df[df.females < df.males].show()

## 9. Spark to Pandas ##

pandas_df = df.toPandas()
pandas_df.total.plot.hist()