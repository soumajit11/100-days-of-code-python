#randomisation
import random
random_int = random.randint(1,10)#1 to 10
random_float = random.random()#0.0000 to 0.9999999
#list
states_of_america = ["Delaware  ", "Pennsylvania", "New Jersey", "Georgia"]
states_of_america.append("Connecticut")
states_of_america.extend(["Massachusetts","Maryland"])
print(states_of_america)
#nested list
fruits = ["Strawberries", "Apples"]
vegetables = ["Spinach", "Kale", "Tomato"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)