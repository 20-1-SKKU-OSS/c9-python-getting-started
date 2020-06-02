def decorator_function(original_function):
    def wrapper_function():
        print '{} function is not called yet.'.format(original_function.__name__)
        return original_function()
    return wrapper_function


@decorator_function
def display_1():
    print 'display_1 function is running.'


@decorator_function
def display_2():
    print 'display_2 function is funning.'


display_1()
print
display_2()
