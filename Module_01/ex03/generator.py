import random


def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    if not isinstance(text, str):
        yield "ERROR"
    elif not isinstance(sep, str) or len(sep) != 1:
        yield "ERROR"
    elif option is None:
        for w in text.split(sep):
            yield w
    elif option == "shuffle":
        length = len(text.split(sep))
        for w in random.sample(text.split(sep), length):
            yield w
    elif option == "ordered":
        for w in sorted(text.split(sep)):
            yield w
    elif option == "unique":
        for w in set(text.split(sep)):
            yield w
    else:
        yield "ERROR"


if __name__ == '__main__':

    print("<-------------NO_OPTION------------->")
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" "):
        print(word)
    print("<-------------OPTION_ORDERED------------->")
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print("<-------------OPTION_SHUFFLE------------->")
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print("<-------------OPTION_UNIQUE------------->")
    text = "Lorem Ipsum Lorem Ipsum"
    for word in generator(text, sep=" ", option="unique"):
        print(word)
    print("<-------------ERRORS------------->")
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" ", option="lol"):
        print(word)
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep="", option=""):
        print(word)
    text = ""
    for word in generator(text, sep=" ", option="lol"):
        print(word)
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=".", option=""):
        print(word)
    text = 1.0
    for word in generator(text, sep="."):
        print(word)
