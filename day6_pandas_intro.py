import pandas as pd 

df = pd.read_csv("sample_data.csv")

print("\n🔹 First 5 rows of the data:") 
print(df.head()) 

# Step 4: Show info about the columns — names, types, if anything is missing
print("\n Dataframe info (columns, types, nulls):")
print(df.info()) 

# Step 5: Show summary statistics — min, max, average, count, etc. 

print("\n🔹 Summary statistics for numeric columns:")
print(df.describe())

# Step 6: Optional — print just the Mood column
print("\n🔹 Mood column:")
print(df["Mood"])
