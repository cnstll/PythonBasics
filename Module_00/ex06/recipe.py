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


def print_keys():
  print('\n{:-^29}\n'.format("KEYS FROM DICTIONNARY"))
  for recipe in cookbook.items():
    print("key: '" + recipe[0] + "'")
    for details in recipe[1].keys():
      print("sub-key: '" + details + "'")
    print()


def print_values():
  print('\n{:-^29}\n'.format("VALUES FROM DICTIONNARY"))
  for recipe in cookbook.items():
    for details in recipe[1].values():
      print("value: '" + str(details) + "'")
    print()


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
  if recipe_name in cookbook:
    print(f"Recipe for {recipe_name}:")
    recipe = cookbook[recipe_name]
    print(f"Ingredients list: {recipe['ingredients']}.")
    print(f"To be eaten for {recipe['meal']}.")
    print(f"Takes {recipe['prep_time']} minutes to cook.")
    print()
  else:
    print(f"Recipe '{recipe_name}' not found :(\n")


def del_from_cookbook(recipe_name):
  if recipe_name in cookbook:
    print(f"Deleting '{recipe_name}' recipe...")
    cookbook.pop(recipe_name)
    print("Done.")
    print()
  else:
    print(f"Recipe '{recipe_name}' not found :(\n")


def add_to_cookbook(recipe_name, ingredients, meal, prep_time):
  if recipe_name in cookbook:
    print(f"Recipe '{recipe_name}' already saved in cookbook\n")
    print()
  else:
    print(f"Adding '{recipe_name}' to cookbook...\n")
    recipe_details = {}
    recipe_details.setdefault('ingredients', ingredients)
    recipe_details.setdefault('meal', meal)
    recipe_details.setdefault('prep_time', prep_time)
    cookbook.setdefault(recipe_name, recipe_details)
    print("Done.")



print()
print_keys()
print()
print_values()
print()
print_dictionnary_details()
print()
print_recipe("salad")
print_recipe("burgers")
del_from_cookbook("salad")
print_dictionnary_details()
add_to_cookbook("pasta", ["pasta", "oil"], "lunch", 10)
print_dictionnary_details()
print_dictionnary()