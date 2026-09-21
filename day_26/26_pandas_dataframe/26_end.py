student_dict = {"student": ["Angela", "James", "Lily"],"score": [56, 76, 98]}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

import pandas as pd
stu_df = pd.DataFrame(student_dict)
print(stu_df)

# Loop through a dataframe
# for (key,value) in stu_df.items:
#   print(value)

#Loop through rows of a dataframe
for (index, row) in stu_df.iterrows():
    if row.student == "Angela":
        print(row.score)