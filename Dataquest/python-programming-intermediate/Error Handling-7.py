## 2. Sets ##

gender = []
for i in legislators:
    gender.append(i[3])
    
print(set(gender))

## 3. Exploring the Dataset ##

party = []
for i in legislators:
    party.append(i[6])
    
print(set(party))
print(legislators)

## 4. Missing Values ##

gender = []
for row in legislators:
    if row[3] == "":
        row[3] = "M"
    gender.append(row[3])
    
    
print(set(gender))

## 5. Parsing Birth Years ##

birth_years = []
for i in legislators:
    parts = i[2].split("-")
    birth_years.append(parts[0])

## 6. Try/except Blocks ##

try:
    float("Hello")
    
except:
    print("Error converting to float..")

## 7. Exception Instances ##

try:
    int(' ')
    
except Exception as ex:
    print(type(ex))
    print(str(ex))

## 8. The Pass Keyword ##

converted_years = []
for year in birth_years:
    try:
        year = int(year)
    except Exception:
        pass
    converted_years.append(year)

## 9. Convert Birth Years to Integers ##



for i in legislators:
    
    try:
       birth_year= int(i[2].split("-")[0])
    except Exception:
        birth_year= 0
    i.append(birth_year)

## 10. Fill in Years Without a Value ##

last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]