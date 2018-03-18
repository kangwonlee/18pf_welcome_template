import os.path

output_file_name = "phones0.txt"
write_mode = 'w'

if os.path.exists(output_file_name):
    print("동일한 이름의 파일이 이미 존재합니다. ")
else:
    outfile = open(output_file_name, write_mode)

    outfile.write("홍길동 010-1234-5678\n")
    outfile.write("김철수 010-1234-5679\n")
    outfile.write("김영희 010-1234-5680\n")

    outfile.close()
