count_tested = 0
count_found = 0

up_to = 1000

for a in range(1, up_to + 1, 1):
    for b in range(1, up_to + 1, 1):
        for c in range(1, up_to + 1, 1):
            count_tested += 1
            if (a * a + b * b) == c * c:
                print(a, b, c)
                count_found += 1

print("count_evaluated =", count_tested)

print("count_found =", count_found)
