## 1. Recap ##

import pandas as pd
loans = pd.read_csv('filtered_loans_2007.csv')
null_counts = loans.isnull().sum()
print(null_counts)

## 2. Handling missing values ##

loans.drop(["pub_rec_bankruptcies"],axis=1,inplace=True)
loans.dropna(inplace=True)
loans.dtypes.value_counts()

## 3. Text columns ##

object_columns_df = loans.select_dtypes(include=['object'])
object_columns_df.head()

## 5. First 5 categorical columns ##

cols = ['home_ownership', 'verification_status', 'emp_length', 'term', 'addr_state']

for c in cols:
    print(loans[c].value_counts())

## 6. The reason for the loan ##

col = ["purpose","title"]

for c in col:
    print(loans[c].value_counts())

## 7. Categorical columns ##

mapping_dict = {
    "emp_length": {
        "10+ years": 10,
        "9 years": 9,
        "8 years": 8,
        "7 years": 7,
        "6 years": 6,
        "5 years": 5,
        "4 years": 4,
        "3 years": 3,
        "2 years": 2,
        "1 year": 1,
        "< 1 year": 0,
        "n/a": 0
    }
}

dc = ["last_credit_pull_d", "addr_state", "title", "earliest_cr_line"]
loans.drop(dc,axis=1,inplace=True)
loans["int_rate"] = loans["int_rate"].str.rstrip("%").map(float)
loans["revol_util"] = loans["revol_util"].str.rstrip("%").map(float)
loans = loans.replace(mapping_dict)

## 8. Dummy variables ##

cat_columns = ["home_ownership", "verification_status", "emp_length", "purpose", "term"]
dummy_df = pd.get_dummies(loans[cat_columns])
loans = pd.concat([loans, dummy_df], axis=1)
loans = loans.drop(cat_columns, axis=1)
                  
                  