from . import register

@register.filter
def myupper(value, *args):
    return value.upper()


@register.filter
def mylower(value, *args):
    return value.lower()

# register.filter(name='mylower', filter_func=mylower)