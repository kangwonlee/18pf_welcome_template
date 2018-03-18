infile = open("phones.txt", "r")
s = infile.readline()
print(s)
s = infile.readline()
print(s)
s = infile.readline()
print(s)
infile.close()

infile = open("phones.txt", "r")
for line in infile:
    print(line)

infile.close()
