# Create a function called text_analyzer that
# displays the sums of upper-case characters,
# lower-case characters, punctuation characters
# and spaces in a given text.


def count_lower_char(text):
    return sum(1 for c in text if c.islower())


def count_upper_char(text):
    return sum(1 for c in text if c.isupper())


def count_spaces(text):
    return sum(1 for c in text if c.isspace())


def count_punctuation(text):
    punctuation_marks = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    return sum(1 for c in text if punctuation_marks.find(c) != -1)


def count_and_print_all(text):
    if text == "":
        print("The text is empty, nothing to analyze here.")
    else:
        print("The text contains " + str(len(text)) + " characters:")
        print("- " + str(count_upper_char(text)) + " upper letters")
        print("- " + str(count_lower_char(text)) + " lower letters")
        print("- " + str(count_punctuation(text)) + " punctuation marks")
        print("- " + str(count_spaces(text)) + " spaces")


def text_analyzer(*args):
    """Function that parse and analyze characters in a text.

    This function counts the number of character, upper characters,
    lower characters, punctuation and spaces in a given text.
    Counters are printed in a formated way.

    Args:
        *args: can accept multiple arguments but expect 1 non-empty
            string as argument.
    """

    if len(args) == 0:
        print("What is the text to analyse?")
    elif len(args) > 1:
        print("ERROR")
    else:
        count_and_print_all(args[0])
