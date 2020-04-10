import time

def timer(f):
    def show_time(*args):
        start = time.time()
        f(*args)
        print(f"Function time: {time.time()-start}")
    return show_time


@timer
def fun(n):
    x=12
    for i in range(10**6):
        x = (x * i) % 212


fun(100)