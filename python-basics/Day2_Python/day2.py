## Conditionals

## if elif else or and bool match

# x = int(input("What is x? "))
# y = int(input("What is y? "))

## Whether x is less than, greater than, or equal to y
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# else:
#     print("x is equal to y")

## ONLY Whether they are equal or not
# if x == y:
#     print("x is equal to y")
# else:
#     print("x is not equal to y")

## Conditionals for Letter Grade
score = int(input("Score: "))

if score <= 100 and score >= 90:
    print("Grade A")
elif score >= 80 and score <= 99:
    print("Grade B")
elif score >= 70 and score <= 89:
    print("Grade C")
elif score >= 65 and score <= 79:
    print("Grade D")
else:
    print("Grade F")

##If number is even or odd
def findEvenOrOdd():
    num = int(input("Please input a number... "))

    if isEven(num):
        print(num, "is an even number")
    else:
        print(num, "is an odd number")

def isEven(n):
    return n % 2 == 0
    
    # return True if n % 2 == 0 else Flase
    
    # if n % 2 == 0:
        # return True
    # else:
        # return False

findEvenOrOdd()

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")