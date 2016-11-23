## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, x in enumerate(ships):
    print(x)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i,x in enumerate(things):
    x.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]

apple_prices_doubled  = [x * 2 for x in apple_prices]
apple_prices_lowered = [x - 100 for x in apple_prices]

## 5. Counting Female Names ##

name_counts = {}
for row in legislators:
    gender = row[3]
    year = row[7]
    if gender == "F" and year > 1940:
        name = row[1]
        if name in name_counts:
            name_counts[name] = name_counts[name] + 1
        else:
            name_counts[name] = 1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []

for i in values:
    b = i is not None and i > 30
    checks.append(b)

## 8. Highest Female Name Count ##


max_value = None
for i in name_counts:
    count = name_counts[i]
    if  max_value is None or count > max_value:
        max_value = count
        

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for i,x in plant_types.items():
    print(i)
    print(x)

## 10. Finding the Most Common Female Names ##

top_female_names = []

for i,x in name_counts.items():
    if x >= 2:
        top_female_names.append(i)

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts = {}
for row in legislators:
    if row[3] == "M" and row[7] > 1940:
        name = row[1]
        if name in male_name_counts:
            male_name_counts[name] = male_name_counts[name] + 1
        else:
            male_name_counts[name] = 1

highest_value = None
for name,count in male_name_counts.items():
    if highest_value is None or count > highest_value:
        highest_value = count

for name,count in male_name_counts.items():
    if count == highest_value:
        top_male_names.append(name)