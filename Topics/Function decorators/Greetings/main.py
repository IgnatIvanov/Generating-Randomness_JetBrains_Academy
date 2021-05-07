def morning(func):
    def wrapper(name):
        func(name)
        print('Good morning, {}'.format(name))
    
    return wrapper
