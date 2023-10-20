#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
list_origin = list_.copy()
index = 1
element_to_replace = 5
if 0<=index<=len(list_):
        list_[index] = 5
        print(f"Copy:     {list_}")
else:
        print(list_)
print(f"Original: {list_origin}")

