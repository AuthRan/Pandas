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

print(df.isnull())  # Tells about wherever there is NaN or none

print(df.isnull().sum()) # Tells about each column kitna khrab data hai

