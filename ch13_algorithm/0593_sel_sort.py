# coding: utf-8
def selectionSort(alist):
    """
    See: Select-sort with Gypsy folk dance (7:06)
    https://www.youtube.com/watch?v=Ns4TPTC8whw
    
    Created at Sapientia University, Tirgu Mures (Marosvásárhely), Romania.
    Directed by Kátai Zoltán and Tóth László. 
    In cooperation with "Maros Művészegyüttes", Tirgu Mures (Marosvásárhely), Romania.
    Choreographer: Füzesi Albert. 
    Video: Lőrinc Lajos, Körmöcki Zoltán. 
    Supported by "Szülőföld Alap", MITIS (NGO) and evoline company.
    
    :param list(number) alist: 
    :return: 
    """
    for i in range(len(alist)):
        minPos = getMinPos(alist, i)
        temp = alist[minPos]
        alist[minPos] = alist[i]
        alist[i] = temp


def getMinPos(alist, start):
    minPos = start
    for i in range(start + 1, len(alist)):
        if alist[i] < alist[minPos]:
            minPos = i
    return minPos


alist = [1, 4, 5, 9, 8, 2, 7]
selectionSort(alist)
print(alist)
