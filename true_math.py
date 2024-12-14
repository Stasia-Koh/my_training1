from math import inf

from module_3_5 import result


def divide (first, second):
    if second == 0:
        return inf
    else:
        return first / second

if __name__ == '__main__':
    result = divide(69, 3)
    print(result)
