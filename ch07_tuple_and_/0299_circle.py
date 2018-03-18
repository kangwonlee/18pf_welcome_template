import math


def cal_circle(r):
    # 반지름이 r인 원의 넓이와 둘레를 동시에 반환하는 함수  (area, circumference)
    area = math.pi * r * r
    circumference = 2 * math.pi * r
    return area, circumference


radius = float(input("원의 반지름을 입력하시오: "))
(a, c) = cal_circle(radius)
# output
print("원의 넓이는 "+str(a)+"이고 원의 둘레는"+str(c)+"이다.")
