## 3. Reading in to Pandas ##

import pandas as pd

loans_2007 = pd.read_csv("loans_2007.csv")

print(loans_2007.loc[0],loans_2007.shape[0])

## 4. First group of columns ##


todrp = ['id','member_id','funded_amnt','funded_amnt_inv','grade','sub_grade','emp_title','issue_d']

loans_2007.drop(todrp,axis=1,inplace=True)

## 5. Second group of features ##

drop = ['zip_code','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv','total_rec_prncp']
loans_2007.drop(drop,axis=1,inplace=True)


## 6. Third group of features ##



drop =['total_rec_int','total_rec_late_fee','recoveries','collection_recovery_fee','last_pymnt_d', 'last_pymnt_amnt']

loans_2007.drop(drop,axis=1,inplace=True)
print(loans_2007.shape[0])
print(loans_2007.head(3))


## 7. Target column ##

print(loans_2007["loan_status"].value_counts)

## 8. Binary classification ##

loans_2007 = loans_2007[(loans_2007['loan_status'] == "Fully Paid") | (loans_2007['loan_status'] == "Charged Off")]

status_replace = {
    "loan_status" : {
        "Fully Paid": 1,
        "Charged Off": 0,
    }
}

loans_2007 = loans_2007.replace(status_replace)

## 9. Removing single value columns ##

orig_columns = loans_2007.columns
drop_columns = []
for col in orig_columns:
    col_series = loans_2007[col].dropna().unique()
    if len(col_series) == 1:
        drop_columns.append(col)
loans_2007 = loans_2007.drop(drop_columns, axis=1)
print(drop_columns)