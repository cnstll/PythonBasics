def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    """
    if not callable(function_to_apply):
        raise TypeError("argument 2 to ft_map() must be callable")
    try:
        iter(iterable)
    except TypeError:
        raise TypeError("argument 2 to ft_map() must support iteration")
    for i in iterable:
        yield function_to_apply(i)


lst = [1, 2, 3, 4, 5]
gen = ft_map(lambda b: b + 5, lst)
print(gen)
print(list(gen))

lst = (5, 10, 15, 20, 25)
gen = ft_map(lambda a: a / 5, lst)
print(gen)
print(list(gen))

lst = "Hello world"
gen = ft_map(lambda a: a.upper(), lst)
print(gen)
print(list(gen))

lst = 42
# gen = ft_map(42, [1, 2])
# print(list(gen))
print(list(ft_map(lambda a: a / 5, lst)))
# print(list(gen))
