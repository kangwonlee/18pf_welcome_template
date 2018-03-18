def sub():
    global s  # 전역 변수인 s 를 사용한다고 명시함
    print('sub() 의 첫번째 s =', s)
    s = '바나나가 좋음!'
    print('sub() 의 두번째 s =', s)


s = '사과가 좋음!'
print('전역의 첫번째 s =', s)
sub()
print('전역의 마지막 s =', s)
