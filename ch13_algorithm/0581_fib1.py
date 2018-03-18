fibo_dict = {0: 0, 1: 1}

counter = 0


def fibm(n):
    global counter
    counter += 1
    if not n in fibo_dict:
        fibo_dict[n] = fibm(n - 1) + fibm(n - 2)
    return fibo_dict[n]


n_list = []
counter_list = []
for n in range(5, 10):
    print(n, "번째 피보나치 수는  ", fibm(n))
    print("fib() 호출 횟수 =", counter)
    n_list.append(n)
    counter_list.append(counter)

import pylab

pylab.plot(n_list, counter_list, '.')
pylab.grid(True)
pylab.show()
