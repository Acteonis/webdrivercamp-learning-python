#!/usr/bin/python3

def tuple_addition(first_arg=(0, 0), second_arg=(0, 0)):
    result = (first_arg[0] + second_arg[0], first_arg[1] + second_arg[1])
    return result


if __name__ == "__main":
    first_arg, second_arg = (1, 99), (-1, 1)
    result = tuple_addition(first_arg, second_arg)
    print(result)
    print(tuple_addition(first_arg, (1,)))
    print(tuple_addition((1, 2, 3, 4), (-1, -2, -3, -4))
    print(tuple_addition((), first_arg))
    print(tuple_addition())
