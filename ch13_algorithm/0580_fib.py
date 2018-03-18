counter = 0


def fib(n):
    global counter
    counter += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n_list = []
counter_list = []
for n in range(5, 10):
    print(n, "번째 피보나치 수는  ", fib(n))
    print("fib() 호출 횟수 =", counter)
    n_list.append(n)
    counter_list.append(counter)

import pylab
pylab.plot(n_list, counter_list, '.')
pylab.grid(True)
pylab.show()
