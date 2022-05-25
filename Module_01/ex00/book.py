import datetime
from recipe import Recipe


class Book:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    # Need to hanlde type checking
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError(f'"name" must be a string')
        if not name:
            raise ValueError(f'"name" cannot be empty')
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name {name} and returns the instance"""
        for recipes in self.recipes_list.values():
            for recipe in recipes:
                if recipe.name == name:
                    print(f"Recipe {name} found !")
                    return recipe
        print(f"Recipe {name} not found !")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        return self.recipes_list.get(recipe_type)

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError(f'"recipe" must be of type recipe')
        self.last_update = datetime.datetime.now()
        if recipe.recipe_type in self.recipes_list.keys():
            self.recipes_list[recipe.recipe_type].append(recipe)
            print("Added successfuly")
        else:
            print("ERROR: recipe type not found!")
