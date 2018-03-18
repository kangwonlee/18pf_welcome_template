s = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15]]
cols = len(s[0])

sum_s = 0
for c in range(cols):  # 1번째 행의 합을 계산한다.
    sum_s += s[1][c]

print(sum_s)
