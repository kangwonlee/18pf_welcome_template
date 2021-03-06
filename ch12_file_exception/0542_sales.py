# 입력 파일 이름과 출력 파일 이름을 받는다. 
infilename = input("입력 파일 이름: ")
outfilename = input("출력 파일 이름: ")

# default file names
if not infilename:
    infilename = 'sales.txt'
if not outfilename:
    outfilename = 'summary.txt'

# 입력을 위한 파일을 연다.
infile = open(infilename, "r")

# 합계와 횟수를 위한 변수를 정의한다. 
sum = 0
count = 0

# 입력 파일에서 한 줄을 읽어서 합계를 계산한다. 
for line in infile:
    dailySale = int(line)
    sum = sum + dailySale
    count = count + 1

infile.close()

# 출력을 위한 파일을 연다.
outfile = open(outfilename, "w")

# 총매출과 일평균 매출을 출력 파일에 기록한다. 
outfile.write("총매출 = " + str(sum) + "\n")
outfile.write("평균 일매출 = " + str(sum / count))

outfile.close()
