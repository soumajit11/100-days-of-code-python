def format_name(f_name, l_name):
    #Docstring - info shows up on hovering over user defined function calling
    """Take first and last name and return name in title case"""
    if f_name == "" or l_name == "":
        return "Not a valid input!"
    name = f_name + " " + l_name
    name = name.title()
    return name
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
print(f"{format_name(f_name, l_name)}")
