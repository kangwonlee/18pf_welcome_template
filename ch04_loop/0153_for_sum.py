import time

#  반복을 이용한 정수합 프로그램
limit = int(input("어디까지 계산할까요: "))

start_time_sec = time.clock()
sum = 0
for i in range(1, limit + 1):
    sum += i
print("1부터 ", limit, "까지의 정수의 합= ", sum)
end_time_sec = time.clock()
print('계산에 걸린 시간 = %g (sec)' % (end_time_sec - start_time_sec))
