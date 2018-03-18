# 막대 src 에 쌓여있는 n개의 원판을 막대 tmp를 사용하여 막대 dest로 옮긴다.

counter = 0


def hanoi_tower(n, src, tmp, dest, b_verbose=False):
    global counter
    counter += 1

    if (n == 1):
        if b_verbose: print("원판 1을", src, "에서", dest, "로 옮긴다.")
    else:
        hanoi_tower(n - 1, src, dest, tmp, b_verbose)
        if b_verbose: print("원판", n, "을", src, "에서", dest, "로 옮긴다.")
        hanoi_tower(n - 1, tmp, src, dest, b_verbose)


n_list = []
counter_list = []

for n in range(3, 20 + 1):
    hanoi_tower(n, 'A', 'B', 'C', b_verbose=False)
    print("n =", n, "# calls =", counter)
    n_list.append(n)
    counter_list.append(counter)

import pylab

pylab.semilogy(n_list, counter_list, '.')
pylab.grid(True)
pylab.show()
