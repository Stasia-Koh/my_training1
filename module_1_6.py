mu_dict = {'Alex': 1993, 'Meri': 1999}
print(mu_dict)
print(mu_dict.get('Alex'))
print(mu_dict.get('Saha'))
mu_dict.update({'Lika': 2001,
                'Mira': 1995})
print(mu_dict)
del mu_dict['Meri']
print(mu_dict)

my_set = {6,'Доска',78.491,6,5,4,8,3,9}
print(my_set)
my_set.update({12,53})
print(my_set)
print(my_set.remove(3))
print(my_set)
