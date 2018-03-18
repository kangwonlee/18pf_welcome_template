file_name, file_open_mode = "phones.txt", 'r'

infile = open(file_name, file_open_mode)
s = infile.read(10)
print(s)
infile.close()

with open(file_name, file_open_mode) as infile:
    s = infile.read(10)
    print(s)
# end infile block
