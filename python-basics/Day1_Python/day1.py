def hello(to = "world"): ## setting default value of to, as world incase hello is called with no parameter
    print("hello " + to)

name = input("What is your name? ")
hello(name)
hello()