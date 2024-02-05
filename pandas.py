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
