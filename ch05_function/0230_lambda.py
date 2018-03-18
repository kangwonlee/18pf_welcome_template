add_two = lambda x, y: x + y

print("정수의 합  : ", add_two(10, 20))
print("정수의 합  : ", add_two(20, 20))

# filter 와 lambda 를 쓰지 않고 for 문을 사용한다면
seven_list = []
for i in range(1, 100):
    if 0 == (i % 7):
        seven_list.append(i)

print(seven_list)


# filter 와 lambda
# lambda x: 0 == (x % 7)
# 위 구문은 x 가 7 의 배수일 때만 참


def lambda_7(x):
    return 0 == (x % 7)


print(tuple(filter(lambda x: 0 == (x % 7), range(1, 100))))
print(tuple(map(lambda x: x * 2, list('abcd'))))


def lambda_2(x):
    return 2 * x
