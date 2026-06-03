vertebrae_dict = {
    "Mammals":"Dog",
    "Reptiles":"Snake",
    "Amphibians":"Frog",
    "Fish":"Shark",
}
print(vertebrae_dict["Mammals"])
vertebrae_dict["Fish"] = "Salmon"#chaning value
vertebrae_dict["Birds"] = "Sparrow"#adding new key into dictionary
#Nested Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visted" : ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visted": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}
#Nested Dictionary in a List
travel_log = [
    {
        "country":"France",
        "cities_visted" : ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country":"Germany",
        "cities_visted": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    },    
]