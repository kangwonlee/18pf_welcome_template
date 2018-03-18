def call_by_value(s):
    s += " To You"
    print('call_by_value() : s =', s)


def call_by_reference(s):
    s += [100, 200]
    print('call_by_reference() : s =', s)


msg = "Happy Birthday"
msg += ' 0325'
print("msg before =", msg)
call_by_value(msg)
print("msg after =", msg)

numbers = [1, 2, 3, 4, 5]
print('numbers before =', numbers)
call_by_reference(numbers)
print('numbers after = ', numbers)
