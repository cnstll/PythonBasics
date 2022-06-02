class Vector:
    def __init__(self, i):
        if isinstance(i, list):
            self.values = i
            if all(isinstance(e, float) for e in i):
                self.shape = (1, len(i))
            elif all(isinstance(e, list) and len(e) == 1 for e in i):
                self.shape = (len(i), 1)
            elif all(isinstance(f, float) for e in i for f in e):
                self.shape = (len(i), 1)
            else:
                raise TypeError("Illformed initializing argument")
        elif isinstance(i, int):
            self.values = [[float(x)] for x in range(0, i)]
            self.shape = (i, 1)
        elif isinstance(i, tuple) and len(i) == 2:
            self.values = [[float(x)] for x in range(i[0], i[1])]
            self.shape = (abs(i[1] - i[0]), 1)
        else:
            raise TypeError(f"{type(i)} is not a supported initializer type")

    def flatten_list(self, lst):
        return [item for sublist in lst for item in sublist]

    def reshape_list(self, lst):
        return [[item] for item in lst]

    def is_row_vector(self):
        return self.shape[0] == 1

    def is_column_vector(self):
        return self.shape[1] == 1

    def are_same_dimension(self, other):
        return self.shape == other.shape

    def __add__(self, rhs):
        if not isinstance(rhs, Vector):
            raise TypeError(f"Type {type(rhs)} not supported as an operand")
        elif self.is_row_vector() and self.are_same_dimension(rhs):
            self.values = [sum(x) for x in zip(self.values, rhs.values)]
        elif self.is_column_vector() and self.are_same_dimension(rhs):
            l1 = self.flatten_list(self.values)
            l2 = self.flatten_list(rhs.values)
            self.values = [sum(x) for x in zip(l1, l2)]
        else:
            msg = f"Cannot add vectors of different shapes: "
            msg += f"{self.shape} != {rhs.shape}"
            raise ValueError(msg)
        return self

    def __radd__(self, lhs):
        return lhs.__add__(self)

    def __sub__(self, rhs):
        if not isinstance(rhs, Vector):
            raise TypeError(f"Type {type(rhs)} not supported as an operand")
        elif self.is_row_vector() and self.are_same_dimension(rhs):
            self.values = [x[0] - x[1] for x in zip(self.values, rhs.values)]
        elif self.is_column_vector() and self.are_same_dimension(rhs):
            l1 = self.flatten_list(self.values)
            l2 = self.flatten_list(rhs.values)
            sub = [x[0] - x[1] for x in zip(l1, l2)]
            self.values = self.reshape_list(sub)
        else:
            msg = f"Cannot sub vectors of different shapes: "
            msg += f"{self.shape} != {rhs.shape}"
            raise ValueError(msg)
        return self

    def __rsub__(self, lhs):
        return lhs.__sub__(self)

    def __truediv__(self, rhs):
        if not isinstance(rhs, (float, int)):
            raise TypeError(f"Type {type(rhs)} not supported as divisor")
        elif rhs == 0:
            raise ValueError(f"Division by zero not supported")
        elif self.is_column_vector():
            l1 = self.flatten_list(self.values)
            self.values = self.reshape_list([x / rhs for x in l1])
        else:
            self.values = [x / rhs for x in self.values]
        return self

    def __rtruediv__(self, lhs):
        return self.__truediv__(lhs)

    def __mul__(self, rhs):
        if not isinstance(rhs, (float, int)):
            raise TypeError(f"Type {type(rhs)} not supported as multiplicator")
        elif self.is_column_vector():
            l1 = self.flatten_list(self.values)
            self.values = self.reshape_list([x * rhs for x in l1])
        else:
            self.values = [x * rhs for x in self.values]
        return self

    def __rmul__(self, lhs):
        return self.__mul__(lhs)

    def __str__(self):
        return f"Vector list: {self.values} and shape: {self.shape}"

    def __repr__(self):
        return f"Vector({self.values}, {self.shape})"

    def dot(self, rhs):
        if not isinstance(rhs, Vector):
            raise TypeError(f"Type {type(rhs)} not supported as operand")
        elif self.is_row_vector() and self.are_same_dimension(rhs):
            res = sum(map(lambda a, b: a * b, self.values, rhs.values))
            return res
        elif self.is_row_vector() and rhs.is_column_vector():
            lst = self.flatten_list(rhs.values)
            res = sum(map(lambda a, b: a * b, self.values, lst))
            return res
        else:
            raise ValueError("Invalid dot product")

    def T(self):
        if self.is_row_vector():
            self.values = self.reshape_list(self.values)
        elif self.is_column_vector():
            self.values = self.flatten_list(self.values)
        else:
            raise ValueError("Invalid vector")
        self.shape = tuple(reversed(self.shape))
        return self
