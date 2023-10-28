#!/usr/bin/python3

def divide_list_safe(list_1, list_2, list_len):
    result = []

    for i in range(list_len):
        try:
            if i >= len(list_1) or i >= len(list_2):
                result.append(0)
                print("out of range")
            else:
                element1 = list_1[i]
                element2 = list_2[i]
                if not (isinstance(element1, (int, float)) and isinstance(element2, (int, float))):
                    result.append(0)
                    print("wrong type")
                elif element2 == 0:
                    result.append(0)
                    print("division by 0")
                else:
                    result.append(element1 / element2)
        except (ZeroDivisionError, TypeError):
            result.append(0)
        finally:
            continue

    return result

if __name__ == "__main":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2))
    print(res)
    print(10 * "_")
    print()

    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2))
    print(res)
