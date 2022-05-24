import datetime
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
        self.last_update = datetime.datetime.now()
        self.creation_date = datetime.datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}


    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        pass


    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        pass

#You will have to handle the error if the argument passed in add_recipe is not a Recipe.
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass