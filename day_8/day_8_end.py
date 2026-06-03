def greet(name,location):#name, location are parameters
    print(f"Hello, {name}!")
    print(f"Welcome to {location}")
greet("Soumajit", "Jaipur")#Soumajit, Jaipur are arguments
greet("Jaipur", "Soumajit")#positional arguments means name=jaipur, location=Soumajit
greet(location="Jaipur", name="Soumajit")#keyword argument, order doesn't matter
