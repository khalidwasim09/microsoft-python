import pandas as pd 

df = pd.read_csv("fitness_tracker.csv")
print(df.head())

print(df.info())

print(df.describe())

missing_values = df.isnull().sum()
print(missing_values) 



df_clean = df.dropna(subset=["Steps", "SleepHours"])
print(df_clean)

sleep_deprived_users = df_clean[df_clean["SleepHours"]< 6] 

print(sleep_deprived_users)

walkers = df_clean[df_clean["Steps"] > 10000]
print (walkers)

tired_users = df_clean[df_clean["Mood"] == "Tired"]
print(tired_users)

average_steps = df_clean["Steps"].mean()
average_sleep = df_clean["SleepHours"].mean()
average_calories = df_clean["Calories"].mean()

print(average_steps)
print(average_sleep)
print(average_calories)

