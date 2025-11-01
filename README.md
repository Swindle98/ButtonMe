# ButtonMe

A python libary to quickly make a Qt GUI with buttons out of a function. Uses PySide6.

## Installation

To install as a part of your python project:

### PyPi - WIP

WIP.

### From github - WIP

## Usage:

1. Import the ButtonMe functions `buttonize` and `run`
2. Decorate the function to buttonize with the `@buttonize` decorator.
3. append the script with `run()`

Example.

``` python
From ButtonMe import buttonize, run #Import the functions

# Create a simple function that will print to the console when the button is pressed
@buttonize  #Decorate the function. This tells ButtonMe to add this function to the gui.
def print_function_1():
    print("this is a demo function")

if __name__=="__main__"
    run() # This function collects all the functions and runs all the boilerplate code to generate a push button for each function decorated.

```

This example will create a window with a single button labeled "print_function_1" which prints to the console when pressed.

Have fun!