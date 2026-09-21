numbers = [1,1,2,3,5,8,13,21,34,55]
sq_num = [n**2 for n in numbers]
print(sq_num)

str = "1,1,2,3,5,8,13,21,34,55"
lst = str.split(",")
str_int = [int(n) for n in lst]
even_int = [n for n in str_int if n%2 == 0]
print(even_int)