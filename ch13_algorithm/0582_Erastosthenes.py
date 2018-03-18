def eratosthenes(n):
    filtered_set = set()
    for i in range(2, n+1):
        if i not in filtered_set:
            # found a prime number
            yield i
            filtered_set.update(range(i * i, n + 1, i))
 
print(list(eratosthenes(100)))
