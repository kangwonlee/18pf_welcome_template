import time

n = int(input("정수를 입력하시오:  "))

start_time_sec = time.clock()

# 반복을 이용한 팩토리얼 구하기
fact = 1.0
for i in range(1, n + 1):
    fact = fact * i

print(n, "!은", fact, "이다.")

end_time_sec = time.clock()
print('계산에 걸린 시간 = %g (sec)' % (end_time_sec - start_time_sec))
