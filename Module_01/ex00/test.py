import unittest
from book import Book
from recipe import Recipe


class TestRecipeException(unittest.TestCase):
    def test_empty_name(self):
        with self.assertRaises(ValueError) as e:
            Recipe("", 1, 5, ["salad", "cucumber"], "", "lunch")
        self.assertEqual(str(e.exception), '"name" cannot be empty')

    def test_empty_recipe_type(self):
        with self.assertRaises(ValueError) as e:
            Recipe("salad", 1, 5, ["salad", "cucumber"], "", "")
        self.assertEqual(str(e.exception), '"recipe_type" cannot be empty')

    def test_empty_ingredients(self):
        with self.assertRaises(ValueError) as e:
            Recipe("salad", 1, 5, [], "", "lunch")
        self.assertEqual(str(e.exception), '"ingredients" cannot be empty')

    def test_empty_ingredients_elements(self):
        with self.assertRaises(ValueError) as e:
            Recipe("salad", 1, 5, ["salad", ""], "", "lunch")
        self.assertEqual(str(e.exception),
                         '"ingredients" cannot contain empty values')

    def test_type_name(self):
        with self.assertRaises(TypeError) as e:
            Recipe(42, 1, 5, ["salad", "cucumber"], "", "lunch")
        self.assertEqual(str(e.exception), '"name" must be a string')

    def test_type_cooking_lvl(self):
        with self.assertRaises(TypeError) as e:
            Recipe("salad", "foo", 5, ["salad", "cucumber"], "", "lunch")
        self.assertEqual(str(e.exception), '"cooking_lvl" must be an int')

    def test_type_cooking_time(self):
        with self.assertRaises(TypeError) as e:
            Recipe("salad", 1, "foo", ["salad", "cucumber"], "", "lunch")
        self.assertEqual(str(e.exception), '"cooking_time" must be an int')

    def test_type_ingredients(self):
        with self.assertRaises(TypeError) as e:
            Recipe("salad", 1, 5, 42, "", "lunch")
        self.assertEqual(str(e.exception), '"ingredients" must be a list')

    def test_type_ingredients_elements(self):
        with self.assertRaises(TypeError) as e:
            Recipe("salad", 1, 5, ["salad", 42], "", "lunch")
        self.assertEqual(str(e.exception),
                         '"ingredients" should contain strings')

    def test_type_description(self):
        with self.assertRaises(TypeError) as e:
            Recipe("salad", 1, 5, ["salad", "cucumber"], 42, "lunch")
        self.assertEqual(str(e.exception), '"description" must be a string')

    def test_type_recipe_type(self):
        with self.assertRaises(TypeError) as e:
            Recipe("salad", 1, 5, ["salad", "cucumber"], "", 42)
        self.assertEqual(str(e.exception), '"recipe_type" must be a string')

    def test_bound_cooking_lvl(self):
        with self.assertRaises(ValueError) as e:
            Recipe("salad", 42, 5, ["salad", "cucumber"], "", "lunch")
        self.assertEqual(str(e.exception),
                         '"cooking_lvl" should be between 1 and 5')

    def test_negative_cooking_time(self):
        with self.assertRaises(ValueError) as e:
            Recipe("salad", 1, -42, ["salad", "cucumber"], "", "lunch")
        self.assertEqual(str(e.exception), '"cooking_time" should be positive')

    def test_incorrect_value_recipe_type(self):
        with self.assertRaises(ValueError) as e:
            Recipe("salad", 1, 5, ["salad", "cucumber"], "", "tea time")
        self.assertEqual(str(e.exception),
                         '"type" must be in ["starter", "lunch", "dessert"]')


class TestRecipeOutput(unittest.TestCase):
    def test_str_builtin(self):
        salad = Recipe("salad", 1, 10,
                       ["cucumber", "tomatoes", "feta", "olives"], "", "lunch")
        str_out = salad.__str__()
        expected = "salad is a level 1 recipe."
        expected += "\nYou will need 10 mins and these ingredients"
        expected += " ['cucumber', 'tomatoes', 'feta', 'olives'] "
        expected += "to complete it.\n"
        expected += "This dish is usually served as lunch.\n"
        self.assertEqual(str_out, expected)

    def test_str_builtin_other_type_of_call(self):
        salad = Recipe("salad", 1, 10,
                       ["cucumber", "tomatoes", "feta", "olives"], "", "lunch")
        str_out = str(salad)
        expected = "salad is a level 1 recipe."
        expected += "\nYou will need 10 mins and these ingredients"
        expected += " ['cucumber', 'tomatoes', 'feta', 'olives'] "
        expected += "to complete it.\n"
        expected += "This dish is usually served as lunch.\n"
        self.assertEqual(str_out, expected)

    class TestBookException(unittest.TestCase):
        def test_empty_name(self):
            with self.assertRaises(ValueError) as e:
                Book("")
            self.assertEqual(str(e.exception), '"name" cannot be empty')

        def test_empty_name(self):
            with self.assertRaises(ValueError) as e:
                Book(42)
            self.assertEqual(str(e.exception), '"name" cannot be empty')

        def test_type_name(self):
            with self.assertRaises(TypeError) as e:
                Book(42)
            self.assertEqual(str(e.exception), '"name" must be a string')

        def test_type_add_recipe(self):
            with self.assertRaises(TypeError) as e:
                test = Book("test")
                test.add_recipe(42)
            self.assertEqual(str(e.exception),
                             '"recipe" must be of type recipe')


class TestBookOutput(unittest.TestCase):

    def test_get_recipe_by_name_invalid(self):
        test_book = Book("test")
        salad_dup = test_book.get_recipe_by_name("salad")
        str_out = salad_dup
        expected = None
        self.assertEqual(str_out, expected)

    def test_get_recipe_by_name_valid(self):
        salad = Recipe("salad", 1, 10,
                       ["cucumber", "tomatoes", "feta", "olives"], "", "lunch")
        test_book = Book("test")
        test_book.add_recipe(salad)
        salad_dup = test_book.get_recipe_by_name("salad")
        str_out = str(salad_dup)
        expected = "salad is a level 1 recipe."
        expected += "\nYou will need 10 mins and these ingredients"
        expected += " ['cucumber', 'tomatoes', 'feta', 'olives'] "
        expected += "to complete it.\n"
        expected += "This dish is usually served as lunch.\n"
        self.assertEqual(str_out, expected)

    def test_get_recipe_by_type_invalid(self):
        salad = Recipe("salad", 1, 10,
                       ["cucumber", "tomatoes", "feta", "olives"], "", "lunch")
        test_book = Book("test")
        test_book.add_recipe(salad)
        lunch_list = test_book.get_recipes_by_types("brunch")
        self.assertEqual(lunch_list, None)

    def test_get_recipe_by_type_valid(self):
        salad = Recipe("salad", 1, 10,
                       ["cucumber", "tomatoes", "feta", "olives"], "", "lunch")
        test_book = Book("test")
        test_book.add_recipe(salad)
        lunch_list = test_book.get_recipes_by_types("lunch")
        self.assertIsInstance(lunch_list, list)
        self.assertIsInstance(lunch_list[0], Recipe)


# Cmd entrypoint for unittest
if __name__ == '__main__':
    unittest.main()

# my_book = Book("cookbook 2.0")
# print(str(my_book.name))
# print(str(my_book.last_update))
# print(str(my_book.creation_date))
# print(str(my_book.recipes_list))
# my_book.get_recipe_by_name("salad")
# my_book.get_recipes_by_types("doesnotexit")
# salad = recipe.Recipe("salad", 1, 10,
#                       "cucumber", "tomatoes", "feta", "olives"], "", "lunch")
# # my_book.add_recipe("Should raise an exception")
# my_book.add_recipe(salad)
# salad_dup = my_book.get_recipe_by_name("salad")
# print(str(salad_dup))
# salad_dup.description = "I love it"
# my_book.get_recipes_by_types(salad.recipe_type)
# print(str(salad_dup))
