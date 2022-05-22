cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}


# def print_keys():
#   print('\n{:-^29}\n'.format("KEYS FROM DICTIONNARY"))
#   for recipe in cookbook.items():
#     print("key: '" + recipe[0] + "'")
#     for details in recipe[1].keys():
#       print("sub-key: '" + details + "'")
#     print()


# def print_values():
#   print('\n{:-^29}\n'.format("VALUES FROM DICTIONNARY"))
#   for recipe in cookbook.items():
#     for details in recipe[1].values():
#       print("value: '" + str(details) + "'")
#     print()


def print_dictionnary():
    print('\n{:~^29}\n'.format("Your Cookbook"))
    for recipe in cookbook.items():
        print('{:^29}'.format(recipe[0]))
    print()
    print('\n{:~^29}\n'.format(""))


def print_dictionnary_details():
    print('\n{:-^29}\n'.format("ITEMS FROM DICTIONNARY"))
    for recipe in cookbook.items():
        print("key: '" + recipe[0] + "'")
        for details in recipe[1].items():
            print("pair: " + str(details))
            print()


def print_recipe(recipe_name):
    print(f"\nRecipe for {recipe_name}:")
    recipe = cookbook[recipe_name]
    print(f"Ingredients list: {recipe['ingredients']}.")
    print(f"To be eaten for {recipe['meal']}.")
    print(f"Takes {recipe['prep_time']} minutes to cook.")


def print_from_cookbook():
    print("\nEnter the name of the recipe you want to look up:")
    recipe_name = input("\n>> ")
    if recipe_name in cookbook:
        print_recipe(recipe_name)
    elif not recipe_name:
        print("No recipe name entered...")
    else:
        print(f"Recipe '{recipe_name}' not found :(\n")


def del_recipe(recipe_name):
    cookbook.pop(recipe_name)


def del_from_cookbook():
    print("\nEnter the name of the recipe you want to delete:")
    recipe_name = input("\n>> ")
    if recipe_name in cookbook:
        del_recipe(recipe_name)
        print("Recipe succesfully deleted.")
    elif not recipe_name:
        print("No recipe name entered...")
    else:
        print(f"Recipe '{recipe_name}' not found :(\n")


def add_recipe(recipe_name, ingredients, meal, prep_time):
    recipe_details = {}
    recipe_details.setdefault('ingredients', ingredients)
    recipe_details.setdefault('meal', meal)
    recipe_details.setdefault('prep_time', prep_time)
    cookbook.setdefault(recipe_name, recipe_details)


def add_to_cookbook():
    print("\nEnter the name of the recipe you want to add: ")
    recipe_name = input("\n>>  ")
    if recipe_name in cookbook:
        print(f"Recipe '{recipe_name}' already saved in cookbook\n")
    elif not recipe_name:
        print("No recipe name entered...")
    else:
        print(f"\nFill in the details for '{recipe_name}' recipe")
        ingredients = input("Ingredients (list): ")
        meal = input("Meal: ")
        prep_time = input("Preparation time: ")
        add_recipe(recipe_name, ingredients, meal, prep_time)
        print("Recipe succesfully added.")


def print_functionalities():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


def check_input(input):
    valid_inputs = [str(x) for x in range(1, 6)]  # comprehension list
    if input in valid_inputs:
        return True
    else:
        return False


def print_input_error():
    print("\nThis option does not exist, ", end="")
    print("please type the corresponding number.")
    print("To exit, enter 5.")


def quit():
    print('\nCookbook closing...\nBye.\n')
    exit(0)


def execute_functionality(selection):
    functionalities[selection]()


functionalities = {
    '1': add_to_cookbook,
    '2': del_from_cookbook,
    '3': print_from_cookbook,
    '4': print_dictionnary,
    '5': quit
}

while (1):
    print_functionalities()
    selection = input(">> ")
    if check_input(selection):
        execute_functionality(selection)
    elif not selection:
        print("\nEmpty entry. Please enter a number between 1 and 5.")
    else:
        print_input_error()
    print()
