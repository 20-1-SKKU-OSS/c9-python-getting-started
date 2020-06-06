def decorator_function(original_function):
    def wrapper_function():
        print('{} function is about to be called'.format(original_function.__name__))
        return original_function()

    return wrapper_function


def display_1():
    print('display_1 function is running.')


def display_2():
    print('display_2 function is running.')


@decorator_function
def display_3():
    print('display_3 function is running.')


display_1 = decorator_function(display_1)

display_1()
print()

decorator_function(display_2)()
print()

display_2()
print()

display_3()
