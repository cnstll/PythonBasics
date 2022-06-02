import unittest
from vector import Vector
import numpy as np


class TestVectorOutput(unittest.TestCase):
    def setUp(self):
        self.lst1_col = [[0.0], [1.0], [2.0], [3.0], [4.0]]
        self.lst2_col = [[5.0], [6.0], [7.0], [8.0], [9.0]]
        self.lst1_row = [0.0, 1.0, 2.0, 3.0, 4.0]
        self.lst2_row = [5.0, 6.0, 7.0, 8.0, 9.0]
        self.v1_col = Vector(self.lst1_col)
        self.v2_col = Vector(self.lst2_col)
        self.v1_row = Vector(self.lst1_row)
        self.v2_row = Vector(self.lst2_row)
        self.arr1_col = np.array(self.lst1_col)
        self.arr2_col = np.array(self.lst2_col)
        self.arr1_row = np.array(self.lst1_row)
        self.arr2_row = np.array(self.lst2_row)
        self.s1 = 2

    # Testing vector initiation
    def test_init_vector_as_row(self):
        v1 = Vector(self.lst1_row)
        expected = np.array(self.lst1_row)
        self.assertListEqual(v1.values, list(expected))

    def test_init_vector_as_column(self):
        v1 = Vector(self.lst1_col)
        expected = list(np.array(self.lst1_col))
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
        expected = np.add(self.arr1_col, self.arr2_col)
        yours = self.v1_col.__add__(self.v2_col)
        self.assertListEqual(yours.values, list(expected))

    def test_aadd_sign_builtin_column_vector(self):
        expected = np.add(self.arr1_col, self.arr2_col)
        yours = self.v1_col + self.v2_col
        self.assertListEqual(yours.values, list(expected))

    def test_add_builtin_row_vector(self):
        expected = np.add(self.arr1_row, self.arr2_row)
        yours = self.v1_row.__add__(self.v2_row)
        self.assertListEqual(yours.values, list(expected))

    def test_add_sign_builtin_row_vector(self):
        expected = np.add(self.arr1_row, self.arr2_row)
        yours = self.v1_row + (self.v2_row)
        self.assertListEqual(yours.values, list(expected))

    def test_radd_builtin_column_vector(self):
        expected = np.add(self.arr2_col, self.arr1_col)
        yours = self.v1_col.__radd__(self.v2_col)
        self.assertListEqual(yours.values, list(expected))

    def test_radd_builtin_row_vector(self):
        expected = np.add(self.arr2_row, self.arr1_row)
        yours = self.v1_row.__radd__(self.v2_row)
        self.assertListEqual(yours.values, list(expected))

# Testing vector subtraction
    def test_sub_builtin_column_vectors(self):
        expected = np.subtract(self.arr1_col, self.arr2_col)
        yours = self.v1_col.__sub__(self.v2_col)
        self.assertListEqual(yours.values, list(expected))

    def test_sub_builtin_row_vectors(self):
        expected = np.subtract(self.arr1_row, self.arr2_row)
        yours = self.v1_row.__sub__(self.v2_row)
        self.assertListEqual(yours.values, list(expected))

    def test_sub_sign_builtin_column_vectors(self):
        expected = np.subtract(self.arr1_col, self.arr2_col)
        yours = self.v1_col - self.v2_col
        self.assertListEqual(yours.values, list(expected))

    def test_sub_sign_builtin_row_vectors(self):
        expected = np.subtract(self.arr1_row, self.arr2_row)
        yours = self.v1_row - self.v2_row
        self.assertListEqual(yours.values, list(expected))

    def test_rsub_builtin_column_vectors(self):
        expected = np.subtract(self.arr2_col, self.arr1_col)
        yours = self.v1_col.__rsub__(self.v2_col)
        self.assertListEqual(yours.values, list(expected))

    def test_rsub_builtin_row_vectors(self):
        expected = np.subtract(self.arr2_row, self.arr1_row)
        yours = self.v1_row.__rsub__(self.v2_row)
        self.assertListEqual(yours.values, list(expected))

    def test_truediv_builtin_column_vectors(self):
        expected = np.true_divide(self.arr1_col, self.s1)
        yours = self.v1_col.__truediv__(self.s1)
        self.assertListEqual(yours.values, list(expected))

    def test_truediv_builtin_row_vectors(self):
        expected = np.true_divide(self.arr1_row, self.s1)
        yours = self.v1_row.__truediv__(self.s1)
        self.assertListEqual(yours.values, list(expected))

    def test_truediv_sign_builtin_column_vectors(self):
        expected = np.true_divide(self.arr1_col, self.s1)
        yours = self.v1_col / self.s1
        self.assertListEqual(yours.values, list(expected))

    def test_truediv_sign_builtin_row_vectors(self):
        expected = np.true_divide(self.arr1_row, self.s1)
        yours = self.v1_row / self.s1
        self.assertListEqual(yours.values, list(expected))

    def test_rtruediv_builtin_column_vectors(self):
        expected = np.true_divide(self.arr1_col, self.s1)
        yours = self.v1_col.__rtruediv__(self.s1)
        self.assertListEqual(yours.values, list(expected))

    def test_rtruediv_builtin_row_vectors(self):
        expected = np.true_divide(self.arr1_row, self.s1)
        yours = self.v1_row.__rtruediv__(self.s1)
        self.assertListEqual(yours.values, list(expected))

    def test_mul_builtin_column_vectors(self):
        expected = np.multiply(self.arr1_col, self.s1)
        yours = self.v1_col.__mul__(self.s1)
        self.assertListEqual(yours.values, list(expected))

    def test_mul_builtin_row_vectors(self):
        expected = np.multiply(self.arr1_row, self.s1)
        yours = self.v1_row.__mul__(self.s1)
        self.assertListEqual(yours.values, list(expected))

    def test_mul_sign_builtin_column_vectors(self):
        expected = np.multiply(self.arr1_col, self.s1)
        yours = self.v1_col * self.s1
        self.assertListEqual(yours.values, list(expected))

    def test_mul_sign_builtin_row_vectors(self):
        expected = np.multiply(self.arr1_row, self.s1)
        yours = self.v1_row * self.s1
        self.assertListEqual(yours.values, list(expected))

    def test_rmul_builtin_column_vectors(self):
        expected = np.multiply(self.arr1_col, self.s1)
        yours = self.v1_col.__rmul__(self.s1)
        self.assertListEqual(yours.values, list(expected))

    def test_rmul_builtin_row_vectors(self):
        expected = np.multiply(self.arr1_row, self.s1)
        yours = self.v1_row.__rmul__(self.s1)
        self.assertListEqual(yours.values, list(expected))

    def test_str_magic_method(self):
        values_expected = [0.0, 1.0, 2.0, 3.0, 4.0]
        shape_expected = (1, 5)
        expected = f"Vector list: "
        expected += f"{values_expected} and shape: {shape_expected}"
        yours = self.v1_row.__str__()
        self.assertEqual(yours, expected)

    def test_str_ctor_magic_method(self):
        values_expected = [0.0, 1.0, 2.0, 3.0, 4.0]
        shape_expected = (1, 5)
        expected = f"Vector list: "
        expected += f"{values_expected} and shape: {shape_expected}"
        yours = str(self.v1_row)
        self.assertEqual(yours, expected)

    def test_repr_magic_method(self):
        values_expected = [0.0, 1.0, 2.0, 3.0, 4.0]
        shape_expected = (1, 5)
        expected = f"Vector({values_expected}, {shape_expected})"
        yours = self.v1_row.__repr__()
        self.assertEqual(yours, expected)

    def test_dot_row_x_col_vector(self):
        expected = np.dot(self.arr1_row, self.arr2_col)
        yours = self.v1_row.dot(self.v2_col)
        self.assertEqual(yours, expected)

    def test_dot_row_vector(self):
        expected = np.dot(self.arr1_row, self.arr2_row)
        yours = self.v1_row.dot(self.v2_row)
        self.assertEqual(yours, expected)

    def test_transpose_row_vector(self):
        expected = np.transpose(self.arr1_row)
        expected_shape = (5, 1)
        yours = self.v1_row.T()
        self.assertListEqual(yours.values, list(expected))
        self.assertEqual(yours.shape, expected_shape)

    def test_transpose_col_vector(self):
        expected = self.arr1_row
        expected_shape = (1, 5)
        yours = self.v1_col.T()
        self.assertListEqual(yours.values, list(expected))
        self.assertEqual(yours.shape, expected_shape)


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
