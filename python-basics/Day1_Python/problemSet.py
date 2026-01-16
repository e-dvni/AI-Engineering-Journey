# In a file, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

def toLowerCase():
    string = input("Please enter a str... ")
    print(string.lower())

toLowerCase()

# Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

# In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

#create a function that collects user input string
def playback():
    inpt = input("Please type a sentence: ")
    #replace white space with "..."
    otpt = inpt.replace(" ", "... ")
    print(otpt)

playback()

# Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. Nowadays, programs tend to convert emoticons to emoji automatically!

# In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

# Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.

def convert(text):
    # replace happy and sad emoticons with emoji
    return text.replace(":)", "🙂").replace(":(", "🙁").replace("(:", "🙂").replace("):", "🙁")

def userInput():
    data = input("Please enter a string... ")
    print(convert(data))

userInput()

# Even if you haven’t studied physics (recently or ever!), you might have heard that 𝐸 =𝑚⁢𝑐2, wherein 𝐸 represents energy (measured in Joules), 𝑚 represents mass (measured in kilograms), and 𝑐 represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

# In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

# create E = mc2 Function
def enstein(mass_kg):
    c = 300_000_000
    e = mass_kg * c * c
    print(f"{e:.2e}", "Joules")

# take user input for mass
def mass():
    try:
        m = int(input("For E = mc2 please enter m... "))
    except ValueError:
        print("Please enter an integer mass in kilograms.")
        return
    (enstein(m))

mass()

# TIP CALCULATOR

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # strip whitespace and any leading '$', then convert to float
    return float(d.strip().replace("$", ""))


def percent_to_float(p):
    # strip whitespace and trailing '%', then convert to a decimal
    return float(p.strip().replace("%", "")) / 100.0

main()