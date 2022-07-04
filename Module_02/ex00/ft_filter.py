def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    """
    if not callable(function_to_apply):
        raise TypeError("argument 2 to ft_filter() must be callable")
    try:
        iter(iterable)
    except TypeError:
        raise TypeError("argument 2 to ft_filter() must support iteration")
    for i in iterable:
        if function_to_apply(i):
            yield i


x = [1, 2, 3, 4, 5]
gen = ft_filter(lambda dum: not (dum % 2), x)
print(list(gen))

x = "Hello World"
gen = ft_filter(lambda c: not c == "o", x)
print(list(gen))
