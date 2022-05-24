
class Recipe:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    # Need to hanlde type checking
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            if name:
                self._name = name
            else:
                raise ValueError('"name" cannot be empty')
        else:
            raise TypeError('"name" must be a string')

    @property
    def cooking_lvl(self):
        return self._cooking_lvl

    @cooking_lvl.setter
    def cooking_lvl(self, cooking_lvl):
        if isinstance(cooking_lvl, int):
            if cooking_lvl >= 1 and cooking_lvl <= 5:
                self._cooking_lvl = cooking_lvl
            else:
                raise ValueError('"cooking_lvl" should be between 1 and 5')
        else:
            raise TypeError('"cooking_lvl" must be an int')
    
    @property
    def cooking_time(self):
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, cooking_time):
        if isinstance(cooking_time, int):
            if cooking_time > 0:
                self._cooking_time = cooking_time
            else:
                raise ValueError('"cooking_time" should be positive')
        else:
            raise TypeError('"cooking_time" must be an int')
    
    
    @property
    def ingredients(self):
        return self._ingredients


    @ingredients.setter
    def ingredients(self, ingredients):
        if isinstance(ingredients, list):
            if not ingredients:
                raise ValueError('"ingredients" cannot be empty')
            if not all(i for i in ingredients):
                raise ValueError('"ingredients" cannot contain empty values')
            if not all(isinstance(i, str) for i in ingredients):
                raise TypeError('"ingredients" should contain strings')
            self._ingredients = ingredients
        else:
            raise TypeError('"ingredients" must be a list')

    @property
    def description(self):
        return self._description


    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self._description = description
        else:
            raise TypeError('"description" must be a string')

    @property
    def recipe_type(self):
        return self._recipe_type


    @recipe_type.setter
    def recipe_type(self, recipe_type):
        if isinstance(recipe_type, str):
            if not recipe_type:
                raise ValueError('"recipe_type" cannot be empty')
            if recipe_type in ["starter", "lunch", "dessert"]:
                self._recipe_type = recipe_type
            else:
                raise ValueError('"recipe_type" must be "starter", "lunch" or "dessert"')
        else:
            raise TypeError('"recipe_type" must be a string')

    
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"{self.name} is a level {self.cooking_lvl} recipe.\n"
        txt += f"You will need {self.cooking_time} mins "
        txt += f"and these ingredients {self.ingredients} to complete it.\n"
        txt += f"This dish is usually served as {self.recipe_type}.\n"
        if self.description:
            txt += f"Additional details:\n{self.description}\n"
        return txt
