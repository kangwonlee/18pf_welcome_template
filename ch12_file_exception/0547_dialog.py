from tkinter.filedialog import askopenfilename

readFile = askopenfilename()
if readFile:
    infile = open(readFile, "r")

    for line in infile.readlines():
        line = line.strip()
        print(line)

    infile.close()
