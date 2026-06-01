#Scope

#local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()
# print(drink_potion)  #throws error as the variable defined inside the function

#global scope
player_health = 10 # global variable
def drink_portion_2():
    potion_strength = player_health + 1 #global can be used locally
    print(potion_strength)
drink_portion_2()
print(player_health)

# there is no block scope means variables can accessed even though defined inside a if-else/ for/while loop

# modifying global scope
enemies = 1
def increase_enemies():
    global enemies # helps in modify global variable locally
    enemies += 1
    print(f"enemies inside function: {enemies}") 
increase_enemies()
print(f"enemies outside function: {enemies}")
# not advised ^

# we can update global scope using return like
x=2
def x1():
    return x+1
x = x1()
print(x)

# global constants
PI = 3.14159
URL_GOOGLE = "https://www.google.com"
# use caps as it helps you to remind that these are global variable and not to change its value locally
