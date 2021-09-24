def subgen_receiver():
    message = yield
    print('subgen received:', message)

def subgen_sender():
    x = 'Готов принимать сообщения'
    message = yield x
    print('subgen send:', message)

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

class BlaBlaBla(Exception):
    pass

@coroutine
def generator_average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        except BlaBlaBla:
            print('........')
            break

        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

    return average

