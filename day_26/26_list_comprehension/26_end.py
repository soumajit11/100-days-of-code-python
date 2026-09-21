# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

numbers = [1, 2, 3]
new_list =[n+1 for n in numbers]
print(new_list)

range_list = [n*2 for n in range(1,5)]
print(range_list)

#Conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name)<5]
print(short_names)
long_names = [name.upper() for name in names if len(name)>4]
print(long_names)