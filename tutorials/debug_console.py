"""
A short tutorial for how to use the debug console in VSCode. 
The debug console lets you run code in the context of your program,
and is useful for debugging and testing. The debug console lets you 
run python code at breakpoints in your function while the debugger is active,
being a useful tool to figure out what's going on in your code, and fix the bugs. 
It can access all Python variables, global, local, and built-in, and can 
modify the state of the program at the breakpoint.

The debug console is the first and best place to start when fixing and debugging code, 
not a jupyter notebook or a python shell where you try to import and run the code. 
This is because the debug console makes sure you don't repeat yourself and have the same 
code written twice, and that you can run the code in the context of your program, and you 
can see all variabes. It's easy and fast to use, it just takes a few seconds to set up, and 
some knowledge of how to use it.
"""


def buggy_function(n):
    """
    A function that is supposed to calculate the factorial of a number,
    but contains a bug.
    """
    result = 1
    for i in range(n + 1):
        result *= i
    return result


# To debug this function using the debug console in VSCode, follow these steps:
# 1. Set a breakpoint on the line with the 'for' loop by clicking to the left of the line number.
# 2. Start the debugger by clicking on the Run icon in the Activity Bar and then clicking on 'Start Debugging'.
# 3. When the execution stops at the breakpoint, you can use the debug console to inspect variables and run code.
#    You can open the debug console by clicking on 'View' in the menu and then 'Debug Console'.
# 4. In the debug console, you can type the name of a variable to see its value. For example, type 'i' to see the current value of 'i'.
# 5. You can also run code in the debug console. For example, try running 'result * i' to see what the next value of 'result' will be.
# 6. By inspecting the variables and running code in the debug console, you can see that the bug in the function is that the 'for' loop starts at 0 instead of 1.
#    This causes 'result' to become 0 on the first iteration, which is not correct for calculating a factorial.
#    You can set result to 1 by typing 'result = 1' in the debug console, fixing it for that iteration. Handy!
# 7. To fix the bug, change the 'for' loop to 'for i in range(1, n + 1)'.
# 8. After fixing the bug, you can stop the debugger by clicking on the red square in the Activity Bar.
# 9. You can then run the function with different inputs to verify that it works correctly.

"""Tips and Tricks
- You can use the up and down arrow keys to cycle through previous commands in the debug console.
- You can use the tab key to autocomplete variable names in the debug console.
- You can use the debug console to run any Python code, not just inspecting variables.
- You can use the debug console to modify the state of your program at the breakpoint, which can be useful for testing.
- You can use the debug console to run code that is not part of your program, such as importing a module or running a function.
- You can use the debug console to run code in the context of your program, which can be useful for debugging and testing.
- You can edit variables in the variabes tab in VSCode also!
- Shift + Enter lets you write multiple lines of code in the debug console. Handy!
- There's a "Toggle All Active Breakpoints" button in the debug console, which lets you disable all breakpoints at once."""


if __name__ == "__main__":
    result = buggy_function(5)
    # Notice if you run this code, it fails,
    # but if you fix it in the debug console, it works.
    assert result == 120, f"Expected 120, but got {result}"
