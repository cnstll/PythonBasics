import unittest
from vector import Vector
import numpy as np # for testing purpose


class TestVectorOutput(unittest.TestCase):

    # Testing vector initiation
    def test_init_vector_as_row(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        expected = np.array([[0.0], [1.0], [2.0], [3.0]])
        self.assertEqual(v1.shape, expected.shape)
        self.assertListEqual(v1.values, list(expected))

    def test_init_vector_as_column(self):
        v1 = Vector([0.0, 1.0, 2.0, 3.0])
        expected = list(np.array([0.0, 1.0, 2.0, 3.0]))
        self.assertListEqual(v1.values, list(expected))

    def test_init_vector_with_size(self):
        v1 = Vector(3)
        expected = np.arange(stop=3, dtype=float)
        self.assertListEqual(v1.values, list(expected))

    def test_init_vector_as_tuple(self):
        v1 = Vector((10, 15))
        expected = np.arange(start=10, stop=15, step=1, dtype=float)
        self.assertListEqual(v1.values, list(expected))

    # Testing vector addition
    def test_add_builtin_column_vector(self):
        v1 = Vector((0, 5))
        v2 = Vector((5, 10))
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr2 = np.arange(start=5, stop=10, step=1, dtype=float)
        arr1 = np.reshape(arr1, (5, 1))
        arr2 = np.reshape(arr2, (5, 1))
        expected = np.add(arr1, arr2)
        self.assertListEqual(list(v1.__add__(v2)), list(expected))

    def test_add_builtin_row_vector(self):
        v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
        v2 = Vector([5.0, 6.0, 7.0, 8.0, 9.0])
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr2 = np.arange(start=5, stop=10, step=1, dtype=float)
        expected = np.add(arr1, arr2)
        self.assertListEqual(list(v1.__add__(v2)), list(expected))

    def test_radd_builtin_column_vector(self):
        v1 = Vector((0, 5))
        v2 = Vector((5, 10))
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr2 = np.arange(start=5, stop=10, step=1, dtype=float)
        arr1 = np.reshape(arr1, (5, 1))
        arr2 = np.reshape(arr2, (5, 1))
        expected = np.add(arr2, arr1)
        self.assertListEqual(list(v1.__radd__(v2)), list(expected))

    def test_radd_builtin_row_vector(self):
        v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
        v2 = Vector([5.0, 6.0, 7.0, 8.0, 9.0])
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr2 = np.arange(start=5, stop=10, step=1, dtype=float)
        arr1 = np.reshape(arr1, (5, 1))
        arr2 = np.reshape(arr2, (5, 1))
        expected = np.add(arr2, arr1)
        self.assertListEqual(list(v1.__radd__(v2)), list(expected))

    # def test_add_builtin_column_with_scalar(self):
    #     v1 = Vector((0, 5))
    #     v2 = 5.0
    #     arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
    #     arr1 = np.reshape(arr1, (5, 1))
    #     arr2 = 5.0
    #     expected = np.add(arr1, arr2)
    #     self.assertListEqual(list(v1.__add__(v2)), list(expected))

    # def test_add_builtin_row_with_scalar(self):
    #     v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
    #     v2 = 5.0
    #     arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
    #     arr2 = 5.0
    #     expected = np.add(arr1, arr2)
    #     self.assertListEqual(list(v1.__add__(v2)), list(expected))
    
    # Testing vector subtraction    
    def test_sub_builtin_column_vectors(self):
        v1 = Vector((0, 5))
        v2 = Vector((5, 10))
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr2 = np.arange(start=5, stop=10, step=1, dtype=float)
        arr1 = np.reshape(arr1, (5, 1))
        arr2 = np.reshape(arr2, (5, 1))
        expected = np.subtract(arr1, arr2)
        self.assertEqual(list(v1.__sub__(v2)), list(expected))

    def test_sub_builtin_row_vectors(self):
        v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
        v2 = Vector([5.0, 6.0, 7.0, 8.0, 9.0])
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr2 = np.arange(start=5, stop=10, step=1, dtype=float)
        expected = np.subtract(arr1, arr2)
        self.assertListEqual(list(v1.__sub__(v2)), list(expected))

    def test_rsub_builtin_column_vectors(self):
        v1 = Vector((0, 5))
        v2 = Vector((5, 10))
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr2 = np.arange(start=5, stop=10, step=1, dtype=float)
        arr1 = np.reshape(arr1, (5, 1))
        arr2 = np.reshape(arr2, (5, 1))
        expected = np.subtract(arr2, arr1)
        self.assertListEqual(list(v1.__rsub__(v2)), list(expected))

    def test_rsub_builtin_row_vectors(self):
        v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
        v2 = Vector([5.0, 6.0, 7.0, 8.0, 9.0])
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr2 = np.arange(start=5, stop=10, step=1, dtype=float)
        expected = np.subtract(arr2, arr1)
        self.assertListEqual(list(v1.__rsub__(v2)), list(expected))

    # def test_sub_builtin_column_with_scalar(self):
    #     v1 = Vector((0, 5))
    #     v2 = 5.0
    #     arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
    #     arr1 = np.reshape(arr1, (5, 1))
    #     arr2 = 5.0
    #     expected = np.subtract(arr1, arr2)
    #     yours = v1.__sub__(v2)
    #     self.assertListEqual(list(yours), list(expected))

    # def test_sub_builtin_row_with_scalar(self):
    #     v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
    #     v2 = 5.0
    #     arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
    #     arr2 = 5.0
    #     expected = np.subtract(arr1, arr2)
    #     yours = v1.__sub__(v2)
    #     self.assertListEqual(list(yours), list(expected))

    def test_truediv_builtin_column_vectors(self):
        v1 = Vector((0, 5))
        s1 = 2       
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr1 = np.reshape(arr1, (5, 1))
        expected = np.true_divide(arr1, s1)
        self.assertEqual(list(v1.__truediv__(s1)), list(expected))

    def test_truediv_builtin_row_vectors(self):
        v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
        s1 = 2
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        expected = np.true_divide(arr1, s1)
        self.assertListEqual(list(v1.__truediv__(s1)), list(expected))

    def test_rtruediv_builtin_column_vectors(self):
        v1 = Vector((0, 5))
        s1 = 2       
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr1 = np.reshape(arr1, (5, 1))
        expected = np.true_divide(arr1, s1)
        self.assertEqual(list(v1.__rtruediv__(s1)), list(expected))

    def test_rtruediv_builtin_row_vectors(self):
        v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
        s1 = 2
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        expected = np.true_divide(arr1, s1)
        self.assertListEqual(list(v1.__rtruediv__(s1)), list(expected))

    def test_mul_builtin_column_vectors(self):
        v1 = Vector((0, 5))
        s1 = 2       
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr1 = np.reshape(arr1, (5, 1))
        expected = np.multiply(arr1, s1)
        self.assertEqual(list(v1.__mul__(s1)), list(expected))

    def test_mul_builtin_row_vectors(self):
        v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
        s1 = 2
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        expected = np.multiply(arr1, s1)
        self.assertListEqual(list(v1.__mul__(s1)), list(expected))

    def test_rmul_builtin_column_vectors(self):
        v1 = Vector((0, 5))
        s1 = 2       
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        arr1 = np.reshape(arr1, (5, 1))
        expected = np.multiply(s1, arr1)
        self.assertEqual(list(v1.__rmul__(s1)), list(expected))

    def test_rmul_builtin_row_vectors(self):
        v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
        s1 = 2
        arr1 = np.arange(start=0, stop=5, step=1, dtype=float)
        expected = np.multiply(s1, arr1)
        self.assertListEqual(list(v1.__rmul__(s1)), list(expected))

    def test_str_magic_method(self):
        v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
        values_expected = [0.0, 1.0, 2.0, 3.0, 4.0]
        shape_expected = (1,5)
        expected = f"Vector list: {values_expected} and shape: {shape_expected}"
        self.assertEqual(v1.__str__(), expected)

    def test_repr_magic_method(self):
        v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
        values_expected = [0.0, 1.0, 2.0, 3.0, 4.0]
        shape_expected = (1,5)
        expected = f"Vector({values_expected}, {shape_expected})"
        self.assertEqual(v1.__repr__(), expected)

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

    def test_type_error_add(self):
        with self.assertRaises(TypeError) as e:
            v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
            rhs = 42
            expected = f"Type {type(rhs)} not supported as an operand"
            v1.__add__(rhs)
        self.assertEqual(str(e.exception), expected)

    def test_type_error_sub(self):
        with self.assertRaises(TypeError) as e:
            v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
            rhs = 42
            expected = f"Type {type(rhs)} not supported as an operand"
            v1.__sub__(rhs)
        self.assertEqual(str(e.exception), expected)

    def test_type_error_truediv(self):
        with self.assertRaises(TypeError) as e:
            v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
            rhs = '42'
            expected = f"Type {type(rhs)} not supported as divisor"
            v1.__truediv__(rhs)
        self.assertEqual(str(e.exception), expected)

    def test_value_error_truediv_div_by_zero(self):
        with self.assertRaises(ValueError) as e:
            v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
            rhs = 0
            expected = f"Division by zero not supported"
            v1.__truediv__(rhs)
        self.assertEqual(str(e.exception), expected)

    def test_type_error_mul(self):
        with self.assertRaises(TypeError) as e:
            v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
            rhs = '42'
            expected = f"Type {type(rhs)} not supported as multiplicator"
            v1.__mul__(rhs)
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