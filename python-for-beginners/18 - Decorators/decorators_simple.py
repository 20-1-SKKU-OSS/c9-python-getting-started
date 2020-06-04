def decorator_function(original_function):
    def wrapper_function():
        print ('{} function is not called yet.'.format(original_function.__name__))
        return original_function()
    return wrapper_function


def display_1():
    print ('display_1 function is running.')


@decorator_function
def display_2():
    print ('display_2 function is running.')


display_1 = decorator_function(display_1)

display_1()
print()
display_2()
