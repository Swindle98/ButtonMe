from ButtonMe import buttonize, run

@buttonize
def function1():
    print("Function 1 called")

@buttonize
def function2():
    print("Function 2 called")

@buttonize
def function3():
    print("Function 3 called")

@buttonize
def print_this(string_to_print="Hello, ButtonMe!"):
    print(f"Printed: {string_to_print}")


if __name__ == "__main__":
    run()