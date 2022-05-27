import unittest
from vector import Vector
import numpy as np # for testing purpose


class TestVectorOutput(unittest.TestCase):

    def test_init_vector_as_row(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        expected = list(np.array([[0.0], [1.0], [2.0], [3.0]]))
        self.assertEqual(v1.values, expected)

    def test_init_vector_as_column(self):
        v1 = Vector([0.0, 1.0, 2.0, 3.0])
        expected = list(np.array([0.0, 1.0, 2.0, 3.0]))
        self.assertEqual(v1.values, expected)

    def test_init_vector_with_size(self):
        v1 = Vector(3)
        expected = list(np.arange(stop=3, dtype=float))
        self.assertEqual(v1.values, expected)

    def test_init_vector_as_tuple(self):
        v1 = Vector((10, 15))
        expected = list(np.arange(start=10, stop=15, step=1, dtype=float))
        self.assertEqual(v1.values, expected)

    def test_add_builtin(self):
        v1 = Vector((0, 5))
        v2 = Vector((5, 10))
        # expected = [[6.0], [8.0], [10.0], [13.0]]
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr2 = np.arange(start=5, stop=10, step=1, dtype=float)
        expected = np.add(arr1, arr2)
        self.assertEqual(list(v1.__add__(v2)), list(expected))

    def test_rev_add_builtin(self):
        v1 = Vector((0, 5))
        v2 = Vector((5, 10))
        # expected = [[6.0], [8.0], [10.0], [13.0], [15.0]]
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr2 = np.arange(start=5, stop=10, step=1, dtype=float)
        expected = arr1.__radd__(arr2)
        self.assertEqual(list(v1.__radd__(v2)), list(expected))

class TestVectorExcept(unittest.TestCase):
    def test_type_error_float(self):
        with self.assertRaises(TypeError) as e:
            i = 3.0
            expected = f"{type(i)} is not a supported initializer type"
            Vector(i)
        self.assertEqual(str(e.exception), expected)

    def test_type_error_range(self):
        with self.assertRaises(TypeError) as e:
            i = range(1, 5)
            expected = f"{type(i)} is not a supported initializer type"
            Vector(i)
        self.assertEqual(str(e.exception), expected)
# Cmd entrypoint for unittest
if __name__ == '__main__':
    unittest.main()

arr1 = [[0.0], [1.0], [2.0], [3.0]]
arr2 = [[-3.0], [-2.0], [-1.0], [0.0]]
a1 = [0.0, 1.0, 2.0, 3.0]
a2 = [0.0, 1.0, 2.0, 3.0]
v1 = Vector(a1)
v2 = Vector(a2)
print(list(v1.__radd__(v2)))
print(list(Vector(arr1).__radd__(Vector(a2))))