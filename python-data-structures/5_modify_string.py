#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""

def remove_char(some_string):
	result = ""
    	for char in some_string:
        	if char.lower() != 'a':
            		result += char
    	return result


modified_string = remove_char(string)
print(modified_string)
