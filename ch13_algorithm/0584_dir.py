import os


def calcDirSize(name):
    totalSize = 0

    if os.path.isfile(name):
        totalSize += os.path.getsize(name)
    else:
        fileList = os.listdir(name)
        # 서브 디렉토리의 용량을 계산하여 모두 합한다.  
        for subDir in fileList:
            # recursion
            totalSize += calcDirSize(os.path.join(name, subDir))

    return totalSize


def calc_size_os_walk(root):
    total_size = 0
    for path, dir_names, file_names in os.walk(root):
        for file_name in file_names:
            full_path = os.path.join(path, file_name)
            total_size += os.path.getsize(full_path)
    return total_size


name = input("디렉터리 이름을  입력하시오:")
print(calcDirSize(name))
print(calc_size_os_walk(name))
