import fibo

print('fibo.fib(1000)')
fibo.fib(1000)
print('fibo.__name__ =', fibo.__name__)

from fibo import fib

print('fib(500)')
print(fib(500))
