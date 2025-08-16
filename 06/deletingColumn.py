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

df = pd.DataFrame(data)

# To delete a column df.drop(columns = ["ColumnName"], inplace=True/False)
df.drop(columns= ["Pet"], inplace=True)

print(df)