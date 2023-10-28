#!/usr/bin/python3

def dict_print(dict_):
    for key in sorted(dict_.keys()):
        value = dict_[key]
        print(f"{key}: {value}")

if __name__ == "__main":
    dict_ = {"libs": (1, 2, 3), "x": "Selenium", "lang": ["Java", "Python"], "frame": "Behave", "set": set()}
    dict_print(dict_)
