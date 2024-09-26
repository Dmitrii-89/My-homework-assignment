def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = ('Urban', 1234, True)
print_params(*values_list)
values_dict = {'a': 'Urban', 'b': 1234, 'c': True}
print_params(**values_dict)

values_list_2 = [54.32, 'Urban']
print_params(*values_list_2, 42)
