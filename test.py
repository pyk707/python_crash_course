def is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper

def foobar(username="someone"):
    """무엇인가를 하자"""
    pass

print(foobar.__doc__)
print(foobar.__name__)

@is_admin
def foobar(username="someone"):
    """무엇인가를 하자"""
    pass

print(foobar.__doc__)
print(foobar.__name__)