student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
for (key, value) in student_dict.items():
    print(value)

import pandas as pd
student_df = pd.DataFrame(student_dict)
# print(student_df)

# Loop through rows of a data frame
# for (index, row) in student_df.iterrows():
#     if row.student == "Angela":
#         print(row)  # prints entire row

for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)
