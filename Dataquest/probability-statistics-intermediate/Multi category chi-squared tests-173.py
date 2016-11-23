## 2. Calculating expected values ##

males_over50k = .669 * .241 * 32561
males_under50k = .669 * .759 * 32561
females_over50k = .331 * .241 * 32561
females_under50k = .331 * .759 * 32561

## 3. Calculating chi-squared ##

from scipy.stats import chisquare

obs = [6662,1179,15128,9592]
exp = [5249.8,2597.4,16533.5,8180.3]

chisq_gender_income,_ = chisquare(obs,exp)

## 4. Finding statistical significance ##

obs = [6662,1179,15128,9592]
exp = [5249.8,2597.4,16533.5,8180.3]

chisq_gender_income,pvalue_gender_income = chisquare(obs,exp)


## 5. Cross tables ##

table = pandas.crosstab(income["sex"], [income["race"]])
print(table)

## 6. Finding expected values ##

from scipy.stats import chi2_contingency
chisq_value,pvalue_gender_race, df, expected = chi2_contingency(table)