## SF Salaries Exercise

# import pandas as pd
import pandas as pd

# read csv file as df named sal
sal = pd.read_csv('2_pandas_Salaries.csv')

# check head of df
print(sal.head())

# use .info()
sal.info()

# find average BasePay
print(sal["BasePay"].mean())

# find highest amount of OvertimePay
print(sal["OvertimePay"].max())

# find job title of JOSEPH DRISCOLL
print(sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["JobTitle"])

# find JOSEPH DRISCOLL total earnings
print(sal[sal["EmployeeName"] == "JOSEPH DRISCOLL"]["TotalPayBenefits"])

# find highest paid person
print(sal[sal["TotalPayBenefits"].max() == sal["TotalPayBenefits"]]["EmployeeName"])

# find lowest paid person
print(sal[sal["TotalPayBenefits"].min() == sal["TotalPayBenefits"]]["EmployeeName"])

# find average BasePay per year
print(sal.groupby("Year")["BasePay"].mean())

# find number of unique job titles
print(sal["JobTitle"].nunique())

# find top 5 most common jobs
print(sal["JobTitle"].value_counts().head(5))

# how many job titles were represented by only one person in 2013?
#print(sal[sal["Year"] == 2013]["JobTitle"].nunique())
#print(sal[sal["Year"] == 2013]["JobTitle"].value_counts() == 1)
#print(sal.groupby("Year")["JobTitle"].nunique())
#print(sal.groupby("Year")["JobTitle"].value_counts() == 1)
one_person_count = 0
for job in sal[sal["Year"] == 2013]["JobTitle"].value_counts() == 1:
    if job:
        one_person_count += 1
print(one_person_count)

# how many people have the word 'Chief' in their job title?
chief_count = 0
for title in sal["JobTitle"]:
    if "Chief" in title:
        chief_count += 1
print(chief_count)

# is there a correlation between job title string length and salary?
new_sal = pd.DataFrame(sal["TotalPayBenefits"])
new_sal["str_len"] = sal["JobTitle"].str.len()
print(new_sal.corr())