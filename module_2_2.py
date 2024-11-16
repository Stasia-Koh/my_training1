first = int(input('Введите целое число'))
second = int(input('Введите целое число'))
third = int(input('Введите целое число'))

if first == second == third:
       print(3)

elif  first == second:
      print(2)
elif first == third:
      print(2)
elif second == third:
      print(2)
else:
      print(0)