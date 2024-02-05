import pandas as pd

data = {
 'Name': ['John', 'Emma', 'Sam', 'Lisa', 'Tom'],
 'Age': [25, 30, 28, 32, 27],
 'Country': ['USA', 'Canada', 'Australia', 'UK', 'Germany'],
 'Salary': [50000, 60000, 55000, 70000, 52000]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

name_age = df[['Name', 'Age']]
print("\nName and Age columns:")
print(name_age)

filtered_df = df[df['Country'] == 'USA']
print("\nFiltered DataFrame (Country = 'USA'):")
print(filtered_df)

sorted_df = df.sort_values('Salary', ascending=False)

print("\nSorted DataFrame (by Salary in descending order):")
print(sorted_df)

average_salary = df['Salary'].mean()
print("\nAverage Salary:", average_salary)

df['Experience'] = [3, 6, 4, 8, 5]
print("\nDataFrame with added Experience column:")
print(df)

df.loc[df['Name'] == 'Emma', 'Salary'] = 65000
print("\nDataFrame after updating Emma's Salary:")
print(df)

df = df.drop('Experience', axis=1)
print("\nDataFrame after deleting Experience column:")
print(df)


#output:
Original DataFrame:
   Name  Age    Country  Salary
0  John   25        USA   50000
1  Emma   30     Canada   60000
2   Sam   28  Australia   55000
3  Lisa   32         UK   70000
4   Tom   27    Germany   52000

Name and Age columns:
   Name  Age
0  John   25
1  Emma   30
2   Sam   28
3  Lisa   32
4   Tom   27

Filtered DataFrame (Country = 'USA'):
   Name  Age Country  Salary
0  John   25     USA   50000

Sorted DataFrame (by Salary in descending order):
   Name  Age    Country  Salary
3  Lisa   32         UK   70000
1  Emma   30     Canada   60000
2   Sam   28  Australia   55000
4   Tom   27    Germany   52000
0  John   25        USA   50000

Average Salary: 57400.0

DataFrame with added Experience column:
   Name  Age    Country  Salary  Experience
0  John   25        USA   50000           3
1  Emma   30     Canada   60000           6
2   Sam   28  Australia   55000           4
3  Lisa   32         UK   70000           8
4   Tom   27    Germany   52000           5

DataFrame after updating Emma's Salary:
   Name  Age    Country  Salary  Experience
0  John   25        USA   50000           3
1  Emma   30     Canada   65000           6
2   Sam   28  Australia   55000           4
3  Lisa   32         UK   70000           8
4   Tom   27    Germany   52000           5

DataFrame after deleting Experience column:
   Name  Age    Country  Salary
0  John   25        USA   50000
1  Emma   30     Canada   65000
2   Sam   28  Australia   55000
3  Lisa   32         UK   70000
4   Tom   27    Germany   52000
#

