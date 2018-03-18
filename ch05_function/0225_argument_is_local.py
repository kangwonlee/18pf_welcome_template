def sub(my_list):
    my_list[0] = 'change'
    my_list = [1, 2, 3, 4]
    print('함수 내부에서의 my_list =', my_list)
    return


my_list_global = [10, 20, 30, 40]
print("함수 외부에서의 my_list (전) =", my_list_global)
sub(my_list_global)
print("함수 외부에서의 my_list (후) =", my_list_global)
