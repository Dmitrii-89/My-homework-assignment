my_dict = {'Kazan': 420000, 'Samara': 443000, 'Sochi': 354340}     # Город-индекс
print(my_dict)
print(my_dict['Samara'])
print(my_dict.get('Omsk'))
my_dict.update({'Omsk': 644000, 'Voronezh': 394000})
code = my_dict.pop('Sochi')
print(code)
print(my_dict)

my_set = {1,2,3,4,4, 'Ivan',2,1,3,'Ivan', (1,2,3)}
print(my_set)
my_set.add(5)
my_set.add(6)
my_set.discard(1)
print(my_set)