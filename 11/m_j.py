import pandas as pd

students = {
    "StudentID": [1, 2, 3, 4, 5],
    "Name": ["Arun", "Simran", "Karun", "Anjhisht", "Riya"],
    "Age": [20, 22, 21, 19, 23]
}

courses = {
    "StudentID": [1, 2, 3, 6],
    "Course": ["Python", "Java", "C++", "Data Science"],
    "Marks": [85, 90, 75, 95]
}

students_df = pd.DataFrame(students)
courses_df = pd.DataFrame(courses)

merged_df = pd.merge(students_df, courses_df, on="StudentID", how="inner")

print(merged_df)