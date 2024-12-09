def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(3, 'кнопка', False)
print_params(27, 'море')
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [27, 'stasia', False]
values_dict = {'a': 481, 'b': 'роза', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [65.13, 'лейка']
print_params(*values_list_2, 42)