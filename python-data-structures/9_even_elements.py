#!/usr/bin/python3
my_list = [5, 4, 3, 2, 1]
even_odd_tuple = tuple(x % 2 == 0 for x in my_list)

print(my_list)
print(even_odd_tuple)	
