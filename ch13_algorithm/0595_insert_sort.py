# coding: utf-8
def insertionSort(my_list):
    """
    See: https://www.youtube.com/watch?v=ROalU379l3U (4:03)
    https://www.youtube.com/watch?v=ROalU379l3U

    Created at Sapientia University, Tirgu Mures (Marosvásárhely), Romania.
    Directed by Kátai Zoltán and Tóth László. 
    In cooperation with "Maros Művészegyüttes", Tirgu Mures (Marosvásárhely), Romania.
    Choreographer: Füzesi Albert. 
    Video: Lőrinc Lajos, Körmöcki Zoltán. 
    Supported by "Szülőföld Alap", MITIS (NGO) and evoline company.

    :param list(number) alist: 
    :return: 
    """

    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > key:
            my_list[j+1] = my_list[j]
            j = j - 1
        my_list[j + 1] = key

my_list = [5, 2, 4, 6, 1, 3]
insertionSort(my_list)
print(my_list)
