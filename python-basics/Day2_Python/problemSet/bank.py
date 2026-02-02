# In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

# Ask user for greeting input
def greeting():
    inpt = input("Please greet a new client ")
    # create variable for "h"
    letter_to_find = "h"
    # Taking out white space and case sensitivity if the greeting is "hello", output $0
    if inpt.strip(" ").lower() == "hello":
        print("$0")
    # Taking out white space and case senssitivity if the greeting starts with an "h", output $20
    elif letter_to_find in inpt.strip(" ").lower():
        print("$20")
    # If neither output $100
    else:
        print("$100")

greeting()