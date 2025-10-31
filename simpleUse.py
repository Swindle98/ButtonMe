import ButtonMe.main

@ButtonMe.buttonize
def function1():
    print("Function 1 called")

@ButtonMe.buttonize
def function2():
    print("Function 2 called")

@ButtonMe.buttonize
def function3():
    print("Function 3 called")


if __name__ == "__main__":
    ButtonMe.run()