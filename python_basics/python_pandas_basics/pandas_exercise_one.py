## Coding Exercise 1

# import numpy as np, pandas as pd
import numpy as np
import pandas as pd

# read csv file as df named sal
print("Reading Salaries file")
sal = pd.read_csv('2_pandas_Salaries.csv')

# 1: check head of df
print("\nChecking DataFrame head")
print(sal.head())

# 2: use .info()
print("\nUsing .info()")
sal.info()

# 3: find average of first 10000 items in BasePay
print("\nFinding average of first 10000 BasePay")
print(sal["BasePay"].head(10000).mean())

# 4: find highest amount of TotalPayBenefits
print("\nFinding highest TotalPayBenefits")
print(sal["TotalPayBenefits"].max())

# 5: find job title of JOSEPH DRISCOLL
print("\nFinding job title of JOSEPH DRISCOLL")
print(sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"])

# 6: find JOSEPH DRISCOLL total earnings
print("\nFinding total earnings of JOSEPH DRISCOLL")
print(sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits"])

# 7: find highest paid person
print("\nFinding highest paid person")
print(sal[sal["TotalPayBenefits"].max() == sal["TotalPayBenefits"]]["EmployeeName"])

# 8: find lowest paid person
print("\nFinding lowest paid person")
print(sal[sal["TotalPayBenefits"].min() == sal["TotalPayBenefits"]]["EmployeeName"])
print("This person appears to have been paid a negative salary")

# 9: find average TotalPay per year
print("\nFinding average TotalPay per year")
print(sal.groupby("Year")["TotalPay"].mean())

# 10: find number of unique job titles
print("\nFinding unique number of job titles")
print(sal["JobTitle"].nunique())

# 11: find top 7 most common jobs
print("\nFinding 7 most comming jobs")
print(sal["JobTitle"].value_counts().head(7))

# 12: how many job titles were represented by only one person in 2013?
print("\nFinding number of job titles represented by only one person in 2013")
one_person_count = 0
for job in sal[sal["Year"] == 2013]["JobTitle"].value_counts() == 1:
    if job:
        one_person_count += 1
print(one_person_count)

# 13: how many people have the word 'Chief' in their job title?
print("\nFinding number of people with 'Chief' in their job title")
chief_count = 0
for title in sal["JobTitle"]:
    if "Chief" in title:
        chief_count += 1
print(chief_count)

# 14: is there a correlation between salary and job title string length?
print("\nChecking for correlation between salary and job title string length")
new_sal = pd.DataFrame(sal["TotalPayBenefits"])
new_sal["str_len"] = sal["JobTitle"].str.len()
print(new_sal.corr())
print("There does not appear to be a correlation between salary and job title string length")