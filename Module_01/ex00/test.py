import unittest
import recipe

class TestRecipeException(unittest.TestCase):
    def test_empty_name(self):
        with self.assertRaises(ValueError) as e:
            recipe.Recipe("", 1, 5, ["salad", "cucumber"], "", "lunch")
        self.assertEqual(str(e.exception), '"name" cannot be empty')
    
    def test_empty_recipe_type(self):
        with self.assertRaises(ValueError) as e:
            recipe.Recipe("salad", 1, 5, ["salad", "cucumber"], "", "")
        self.assertEqual(str(e.exception), '"recipe_type" cannot be empty')
    
    def test_empty_ingredients(self):
        with self.assertRaises(ValueError) as e:
            recipe.Recipe("salad", 1, 5, [], "", "lunch")
        self.assertEqual(str(e.exception), '"ingredients" cannot be empty')

    def test_empty_ingredients_elements(self):
        with self.assertRaises(ValueError) as e:
            recipe.Recipe("salad", 1, 5, ["salad", ""], "", "lunch")
        self.assertEqual(str(e.exception), '"ingredients" cannot contain empty values')

    def test_type_name(self):
        with self.assertRaises(TypeError) as e:
            recipe.Recipe(42, 1, 5, ["salad", "cucumber"], "", "lunch")
        self.assertEqual(str(e.exception), '"name" must be a string')

    def test_type_cooking_lvl(self):
        with self.assertRaises(TypeError) as e:
            recipe.Recipe("salad", "foo", 5, ["salad", "cucumber"], "", "lunch")
        self.assertEqual(str(e.exception), '"cooking_lvl" must be an int')

    def test_type_cooking_time(self):
        with self.assertRaises(TypeError) as e:
            recipe.Recipe("salad", 1, "foo", ["salad", "cucumber"], "", "lunch")
        self.assertEqual(str(e.exception), '"cooking_time" must be an int')

    def test_type_ingredients(self):
        with self.assertRaises(TypeError) as e:
            recipe.Recipe("salad", 1, 5, 42, "", "lunch")
        self.assertEqual(str(e.exception), '"ingredients" must be a list')

    def test_type_ingredients_elements(self):
        with self.assertRaises(TypeError) as e:
            recipe.Recipe("salad", 1, 5, ["salad", 42], "", "lunch")
        self.assertEqual(str(e.exception), '"ingredients" should contain strings')

    def test_type_description(self):
        with self.assertRaises(TypeError) as e:
            recipe.Recipe("salad", 1, 5, ["salad", "cucumber"], 42, "lunch")
        self.assertEqual(str(e.exception), '"description" must be a string')

    def test_type_recipe_type(self):
        with self.assertRaises(TypeError) as e:
            recipe.Recipe("salad", 1, 5, ["salad", "cucumber"], "", 42)
        self.assertEqual(str(e.exception), '"recipe_type" must be a string')

    def test_bound_cooking_lvl(self):
        with self.assertRaises(ValueError) as e:
            recipe.Recipe("salad", 42, 5, ["salad", "cucumber"], "", "lunch")
        self.assertEqual(str(e.exception), '"cooking_lvl" should be between 1 and 5')

    def test_negative_cooking_time(self):
        with self.assertRaises(ValueError) as e:
            recipe.Recipe("salad", 1, -42, ["salad", "cucumber"], "", "lunch")
        self.assertEqual(str(e.exception), '"cooking_time" should be positive')

    def test_incorrect_value_recipe_type(self):
        with self.assertRaises(ValueError) as e:
            recipe.Recipe("salad", 1, 5, ["salad", "cucumber"], "", "tea time")
        self.assertEqual(str(e.exception), '"recipe_type" must be "starter", "lunch" or "dessert"')
       
class TestRecipeOutput(unittest.TestCase):
    def test_str_builtin(self):
        salad = recipe.Recipe("salad", 1, 10, ["cucumber", "tomatoes", "feta", "olives"], "", "lunch")
        str_out = salad.__str__()
        expected = "salad is a level 1 recipe.\nYou will need 10 mins and these ingredients"
        expected += " ['cucumber', 'tomatoes', 'feta', 'olives'] to complete it.\n"
        expected += "This dish is usually served as lunch.\n"
        self.assertEqual(str_out, expected)
    
    def test_str_builtin_other_type_of_call(self):
        salad = recipe.Recipe("salad", 1, 10, ["cucumber", "tomatoes", "feta", "olives"], "", "lunch")
        str_out = str(salad)
        expected = "salad is a level 1 recipe.\nYou will need 10 mins and these ingredients"
        expected += " ['cucumber', 'tomatoes', 'feta', 'olives'] to complete it.\n"
        expected += "This dish is usually served as lunch.\n"
        self.assertEqual(str_out, expected)

# Cmd entrypoint for unittest
if __name__ == '__main__':
    unittest.main()