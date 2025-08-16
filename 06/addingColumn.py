import pandas as pd

data = {
    "Name": ["Aarav", "Meera", "Kabir", "Zoya", "Rohan", "Anika", "Vivaan", "Ishita", "Arjun", "Diya"],
    "Age": [25, 31, 28, 22, 35, 29, 41, 26, 33, 24],
    "City": ["Bangalore", "Mumbai", "Delhi", "Kolkata", "Pune", "Hyderabad", "Chennai", "Jaipur", "Lucknow", "Ahmedabad"],
    "Profession": ["Software Engineer", "Data Scientist", "Doctor", "Architect", "Entrepreneur", "Designer", "Professor", "Journalist", "Lawyer", "Musician"],
    "Hobby": ["Chess", "Painting", "Cycling", "Cooking", "Photography", "Dancing", "Reading", "Traveling", "Gaming", "Singing"],
    "Favorite_Tech": ["Python", "TensorFlow", "Flutter", "AutoCAD", "Excel", "Figma", "LaTeX", "WordPress", "PowerBI", "Ableton"],
    "Monthly_Income_USD": [1500, 2500, 3000, 2200, 5000, 1800, 2700, 2100, 4000, 1200],
    "Pet": ["Dog", "Cat", "None", "Parrot", "Dog", "None", "Fish", "Dog", "None", "Rabbit"]
}

# Inserting at the end of Table

df = pd.DataFrame(data)

print(df)

print("New data after----------")

df["Bonus"] = df["Monthly_Income_USD"] * 0.1

print(df)

# Inserting at a particular position insert()
# df.insert(location, "Column_Name", some_data)

df.insert(0, "Employee_ID", [f"B230{i}" for i in range(len(df))])

print(df)