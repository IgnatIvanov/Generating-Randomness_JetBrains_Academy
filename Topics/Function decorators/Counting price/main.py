def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))

    return wrapper  

@price_string
def new_price(old_price):
    return old_price * 0.9
