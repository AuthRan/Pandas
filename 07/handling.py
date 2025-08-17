# Now after finding the khrab data we have two options
# 1. Remove that data
# 2. Handle that data

# 1.
import pandas as pd

data = {
    "Name": ["Aarav", None, "Kabir", "Zoya", "Rohan", "Anika", "Vivaan", "Ishita", "Arjun", "Diya"],
    "Age": [25, None, 28, 22, 35, 29, 41, 26, 33, 24],
    "City": ["Bangalore", None, "Delhi", "Kolkata", "Pune", "Hyderabad", "Chennai", "Jaipur", "Lucknow", "Ahmedabad"],
    "Profession": ["Software Engineer", None, "Doctor", "Architect", "Entrepreneur", "Designer", "Professor", "Journalist", "Lawyer", "Musician"],
    "Hobby": ["Chess", None, "Cycling", "Cooking", "Photography", "Dancing", "Reading", "Traveling", "Gaming", "Singing"],
    "Favorite_Tech": ["Python", "TensorFlow", "Flutter", "AutoCAD", "Excel", "Figma", "LaTeX", "WordPress", "PowerBI", "Ableton"],
    "Monthly_Income_USD": [1500, 2500, 3000, 2200, 5000, 1800, 2700, 2100, 4000, 1200],
    "Pet": ["Dog", "Cat", "None", "Parrot", "Dog", "None", "Fish", "Dog", "None", "Rabbit"]
}

df = pd.DataFrame(data)

# Uda dena that data
# df.dropna(axis = 1/0, inplace = True)

print(df)
df.dropna(axis=0, inplace=True)

print(df)



# 2. Handle that data using fillna()
# fillna(0, inplace=True)  -> fill 0 wherever you find 0
# But in real life you might want to fill the None with something meaningful like avg/mean
# df['Age'].fillna(df["Age"].mean(), inplace=True)
# print(df)

# Let's try interpolation
df['Age'] = df["Age"].interpolate(method = "Linear")