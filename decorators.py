def decorator_function(original_function):
    def sample_function():
        print('wrapper exec this before {}'.format(original_function.__name__))
        return original_function()
    return sample_function

@decorator_function
def display():
    print('display function ran')

#1 display=decorator_function(display)
display()

#instead of #1 code we use @decorator_function directly





