#!/usr/bin/env python3
#


from multiprocessing import Process, Lock


def f(l: Lock, i):
    # l.acquire()
    print('hello world', i)
    # l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(100):
        Process(target=f, args=(lock, num)).start()
