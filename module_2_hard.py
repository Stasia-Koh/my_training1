from random import randint

def trap(n):
    unique = ''
    for i in range(1, n):
        for j in range(i + 1 , n ):
            if n % (i + j) == 0:
                unique += str(i) + str(j)

    return unique

way_1 = n = randint(3, 20)
way_2 = n =int(input('Введи число, равное ссуме каждой пары' ))

i_jones = trap(n)

print(way_2)

print(i_jones)
