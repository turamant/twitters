import threading


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

class BlaBlaException(Exception):
    pass

def subgen():
    for i in 'oleg':
        yield i

def delegator(g):
    for i in g:
        yield i


def sub_gen():
    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print('.......', message)
    return 'Возвращает из sub_gen()'

@coroutine
def delegator_gen(g):
    '''while True:
        try:
            data = yield
            g.send(data)
        except BlaBlaException as e:
            g.throw(e)'''
    '''result = yield from g
    print(result)'''

    yield from g   # await  в других языках