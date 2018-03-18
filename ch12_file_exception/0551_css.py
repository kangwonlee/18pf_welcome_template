# 파일을 연다.
with open("data.csv", "r") as f:
    # 파일 안의 각 줄을 처리한다.
    for line in f:

        line = line.strip()  # 공백 문자를 없앤다.

        print(line)  # 줄을 출력한다.

        parts = line.split(",")  # 줄을 쉼표로 분리한다.

        for part in parts:
            # 각 줄의 필드를 출력한다.
            print("   ", part)
