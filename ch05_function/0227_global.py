PI = 3.14159265358979   # 전역 상수


def main():
    radius = float(input('원의 반지름을 입력하시오: '))
    print('원의 면적:', circle_area(radius))
    print('원의 둘레:', circle_circumference(radius))


def circle_area(radius):
    return PI*radius*radius


def circle_circumference(radius):
    return 2*PI*radius


if __name__ == '__main__':
    main()
