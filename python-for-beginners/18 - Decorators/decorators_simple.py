# Simple decorator function that print function name before it called
def decorator_function(original_function):
    def wrapper_function():
        print('{} function is about to be called'.format(original_function.__name__))
        return original_function()

    return wrapper_function

# Define normal function that print one line
def display_1():
    print('display_1 function is running.')

# Define normal function that print one line
def display_2():
    print('display_2 function is running.')

# Define with @decorator_function
@decorator_function
def display_3():
    print('display_3 function is running.')

# Reassign display_1 function to use decorator function
display_1 = decorator_function(display_1)

# This will be called with decorator function, because of reassigning
display_1()
print()

# This will be called with decorator function
decorator_function(display_2)()
print()

# This will be called without decorator function
display_2()
print()

# This will be called with decorator function, because of @decorator_function
display_3()
