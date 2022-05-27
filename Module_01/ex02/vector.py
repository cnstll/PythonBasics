class Vector:
    def __init__(self, i):
        if isinstance(i, list):
            self.values = i
            if all(isinstance(e, float) for e in i):
                self.shape = (1, len(i))
            elif all(isinstance(e, list) and len(e) == 1 for e in i) and all(isinstance(f, float) for e in i for f in e):
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

    def is_row_vector(self):
        return self.shape[0] == 1

    def is_column_vector(self):
        return self.shape[1] == 1

    def are_same_dimension(self, other):
        return self.shape == other.shape

    def __add__(self, rhs):
        if self.is_row_vector() and self.are_same_dimension(rhs):
            return [sum(x) for x in zip(self.values, rhs.values)]
        elif self.is_column_vector() and self.are_same_dimension(rhs):
            l1 = self.flatten_list(self.values)
            l2 = self.flatten_list(rhs.values)
            return [sum(x) for x in zip(l1, l2)]
        else:
            raise ValueError(f"Cannot add vectors of different shapes: {self.shape} != {rhs.shape}")

    def __radd__(self, lhs):
        return lhs.__add__(self)

# # add : only vectors of same dimensions. __sub__
# __rsub__
# # sub : only vectors of same dimensions. __truediv__
# __rtruediv__
# # div : only scalars.
# __mul__
# __rmul__
# # mul : only scalars.
# __str__
# __repr__