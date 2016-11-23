## 2. Condensing class size ##

class_size = data["class_size"]
class_size = class_size[(class_size["GRADE "] == "09-12") & (class_size["PROGRAM TYPE"] == "GEN ED")]

class_size.head()

## 3. Computing average class sizes ##

import numpy
class_size = class_size.groupby("DBN").agg(numpy.mean)
class_size.reset_index(inplace=True)
data["class_size"] = class_size
print(data["class_size"].head())

## 4. Condensing demographics ##

data["demographics"] = data["demographics"][data["demographics"]["schoolyear"] == 20112012]



## 5. Condensing graduation ##

data["graduation"] = data["graduation"][data["graduation"]["Cohort"] =="2006"]
data["graduation"] = data["graduation"][data["graduation"]["Demographic"] == "Total Cohort"]

                                      
                                        
data["graduation"].head()

## 6. Converting AP test scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
data["ap_2010"] = data["ap_2010"][cols]

for i in cols:
    data["ap_2010"][i] = pd.to_numeric(data["ap_2010"][i],errors="coerce")


## 8. Performing the left joins ##

combined = data["sat_results"].merge(data["ap_2010"],how='left')
combined = combined.merge(data["graduation"],how='left')
combined.head()
combined.shape

## 9. Performing the inner joins ##

combined =  combined.merge(data["class_size"], how='inner').merge(data["demographics"], how='inner').merge(data["survey"], how='inner').merge(data["hs_directory"], how='inner')
print(combined.head())
combined.shape

## 10. Filling in missing values ##

means = combined.mean()
combined = combined.fillna(means).fillna(0)
combined.head()

## 11. Adding a school district column ##

def xt(s):
    tmp =  str(s)
    return tmp[0:2]

combined["school_dist"] = combined["DBN"].apply(xt)
combined["school_dist"].head()