def decorator(func):
    def inner():
        print('Before calling the function to be decorated')
        func()
        print('After calling the function to be decorated')
    return inner

def func2decorate():
    print('Function to be decorated')

func2decorate = decorator(func2decorate)
func2decorate()