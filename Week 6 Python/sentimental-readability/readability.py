# TODO
# Import cs50 library get_string function
from cs50 import get_string

# Get user input, and set variables
text = get_string("Enter your text: ")
letters = 0
words = 1
sentences = 0

# Counts and verifies the number and type of letters,
# using the isalpha function
for str in text:
    if str.isalpha():
        letters += 1
    elif str == ' ':
        words += 1
    elif str in ['.', '!', '?']:
        sentences += 1

# This is part of the logic for calculating
# the Coleman-Liau index.
L = letters / words * 100
S = sentences / words * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

# This block calculates the average number of letters and
# returns the result as calculated by the Coleman-Liau formula
if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")