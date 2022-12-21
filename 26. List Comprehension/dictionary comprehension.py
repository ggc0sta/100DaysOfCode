"""
DICTIONARY COMPREHENSION

new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key, value) in dict.items()}
new_dict = {new_key:new_value for (key, value) in dict.items() if condition}
"""

# Create a dictionary with name of students and random score
import random

student_names = ["Alex", "Beth", "Caroline", "Dave", "Lola", "Freddie", "Elanor"]
student_score = {
    student: random.randint(5, 10) for student in student_names
}
print(student_score)

# Only for students with short names
# student_score = {
#     student: random.randint(5, 10) for student in student_names if len(student) < 5
# }
# print(student_score)

# Passed students (grade > 6)
passed_students = {
    name: score for (name, score) in student_score.items() if score > 6
}
print(passed_students)


# Exercises
# Print the number of characters for each word in the string

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split(" ")}  # split sentence in words

print(result)


# dictionary with farenhite temperatures
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {
    day: temp*9/5 + 32 for (day, temp) in weather_c.items()
}
print(weather_f)
