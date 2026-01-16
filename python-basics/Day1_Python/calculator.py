# x = float(input('Input x: '))
# y = float(input('Input y: '))

# z = round(x + y)

# print(x + y)
# print(f"{z:,}")

def main():
    x = int(input("What's x? "))
    print(x, "squared is", square(x))

def square(n):
    return n * n

main()