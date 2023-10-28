#!/usr/bin/python3

def only_unique(list_=[]):
    unique_set = set()
    total = 0

    for num in list_:
        if num not in unique_set:
            unique_set.add(num)
            total += num

    return total

if __name__ == "__main__":
    list_ = [0, 1, 6, 3, 6, 4, 0, 2, 5, 4, 4]
    result = only_unique(list_)
    print(f"Sum of unique: {result}")
