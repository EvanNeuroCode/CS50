calories_per_fruit={
    'apple' : 130,
    'avocado' : 50,
    'banana' : 110,
    'cantaloupe' : 50,
    'grapefruit' : 60,
    'grapes' : 90,
    'honeydew melon' : 50,
    'kiwifruit' : 90,
    'lemon' : 15,
    'lime' : 20,
    'nectarine' : 60,
    'orange' : 80,
    'peach' : 60,
    'pear' : 100,
    'pineapple' : 50,
    'plums' : 70,
    'strawberries' : 50,
    'sweet cherries' : 100,
    'tangerine' : 50,
    'watermelon' : 80
}

def calculate_calories(fruit_name):

    if fruit_name in calories_per_fruit:
        print( calories_per_fruit[fruit_name])
    else:
        return ""



fruit=input("What fruit do you want to know their calories? ").lower()

calculate_calories(fruit)
