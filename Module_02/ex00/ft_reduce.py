def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    """
    r = iterable[0]
    for i in iterable:
        if i != iterable[0]:
            r = function_to_apply(r, i)
    return r


# Find max in list
lst = [1, 2, 3, 5, 4]
gen = ft_reduce(lambda a, b: a if a > b else b, lst)
print(gen)

# Accumulate all elements
lst = [1, 2, 3]
gen = ft_reduce(lambda a, b: a + b, lst)
print(gen)

# Find min in list
lst = [1, 2, 3, 5, 4]
gen = ft_reduce(lambda a, b: a if a < b else b, lst)
print(gen)

# Find the max ascii code
lst = "HELLO WORLD"
gen = ft_reduce(lambda a, b: a if a > b else b, lst)
print(gen)

# Join elements in the list
lst = ['H', 'E', 'L', 'L', 'O']
gen = ft_reduce(lambda a, b: a + b, lst)
print(gen)

# Join elements in the list
lst = ['H']
gen = ft_reduce(lambda a, b: a + b, lst)
print(gen)
