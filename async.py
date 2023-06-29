
import threading, time
import functools


def calltracker(func):
    @functools.wraps(func)
    def wrapper(*args):
        wrapper.has_been_called = True
        return func(*args)
    wrapper.has_been_called = False
    return wrapper

@calltracker
def doubler(number):
    print('Turn off shit called!')
    return number * 2

def foo(xtime):
    print(time.ctime(), xtime)
    xtime=+1
    return xtime
    
WAIT_TIME_SECONDS = .5
TIME_UNTIL_EXEC = 0

ticker = threading.Event()

while not ticker.wait(WAIT_TIME_SECONDS):
    TIME_UNTIL_EXEC += foo(TIME_UNTIL_EXEC)
    if not doubler.has_been_called:
        print("You haven't called this function yet")
    
    if (doubler.has_been_called):
        print('doubler has been called!')

    if (TIME_UNTIL_EXEC % 5 == 0):
        doubler(20)
    
    if (TIME_UNTIL_EXEC % 10 == 0):
        doubler.has_been_called = False
    