def a():
    return b()

def b():
    return c()

def c():
    return d()

def d():
    x = 0
    try:
        return 100/x
    except Exception as e:
        print(e)

a()