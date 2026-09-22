def add(*arg):
    total = 0
    for i in arg:
        total += i
    print(total)

add(1,2,3,4,5,6,7,8,9,10)

def calc(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multi"]
    n -= kwargs["sub"]
    # n /= kwargs["div"]
    return n 

print(calc(2, add=4, sub=2, multi=2))

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.make, my_car.model)

