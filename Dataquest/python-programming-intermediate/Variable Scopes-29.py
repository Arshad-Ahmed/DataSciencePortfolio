## 2. Built-In Functions ##

total = sum([6,11])

## 4. Scopes ##

def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

total = sum(borrower_default_count_240)

average = find_average(principal_outstanding_240)


## 5. Scope Isolation ##

def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

def find_length(column):
    length = len(column)
    return length

length = len(borrower_default_count_240)
average = find_average(principal_outstanding_240)
principal_length = find_length(principal_outstanding_240)
print(length)
print(find_average)
print(find_length)

## 6. Scope Inheritance ##

def find_average(column):
    total = sum(column)
    # In this function, we are going to pretend that we forgot to calculate the length
    return total / length

length = 10

average = find_average(principal_outstanding_240)
print(length)

## 9. Global Variables ##

def fun():
    global b 
    b = 20
    
fun()
print(b)