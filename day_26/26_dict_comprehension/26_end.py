import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
stu_score = {k:random.randint(1,100) for k in names}
print(stu_score)
pass_stu = {k:v for (k,v) in stu_score.items() if v>=60}
print(pass_stu)

sentence = "What is the airspeed velocity of an unladen swallow ?"
words = {word:len(word) for word in sentence.split() if word.isalpha()}
print(words)

cel ={"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday":24}
far = {day:((temp*9)/5+32) for (day,temp) in cel.items()}
print(far)