def get_description(): #смотрите строку докментации
    """Return random weather, just like a pros"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)

