import sys
import re
if len(sys.argv) != 3:
    print("ERROR")
    exit(1)

try:
    string = sys.argv[1]
    n = int(sys.argv[2])
    # Using a raw string r'' for regex
    word_list = re.sub(r'[^\w]', ' ',  string).split()
    # Comprehension list on comparison between each word length (word)
    # and the number of char in the filter (n)
    list = [word for word in word_list if len(word) > n]
    print(list)
except ValueError:
    print("ERROR")
    exit(1)
