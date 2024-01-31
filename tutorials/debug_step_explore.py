"""
A brief tutorial in how to use the debug navigation in VSCode.
The navigation options are step over, step into, step out, and continue.

Step over:
- Step over is used to execute the current line of code and move to the next line, 
without stepping into any function calls on the current line.

Step into:
- Step into is used to execute the current line of code and move to the next line,
stepping into any function calls on the current line.

Step out:
- Step out is used to execute the remaining lines of the current function and return to the caller,
without stepping through each line of the function.

Continue:
- Continue is used to resume execution of the program until the next breakpoint is encountered.

To run the code ignoring any subsequent breakpoints, you can disable all breakpoints by clicking on the "Breakpoints" section in the debugging panel and unchecking them. 
"""


def step_out_function():
    print("Begin step out function")

    y = 10

    print("End step out function")


def step_into_function():
    print("Begin step into function")

    x = 5
    step_out_function()

    print("End step into function")


def step_over_function():
    print("Begin step over function")

    z = 15

    print("End step over function")


if __name__ == "__main__":
    step_into_function()
    step_over_function()
    print("End of program")
