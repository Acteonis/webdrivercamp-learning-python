#!/usr/bin/python3

def calc_weight(list_=[]):
    if not list_:
        return 0.0

    total_score = sum(score * weight for score, weight in list_)
    total_weight = sum(weight for _, weight in list_)

    return total_score / total_weight

if __name__ == "__main":
    list_ = [(3, 2), (5, 9), (7, 7)]
    result = calc_weight(list_)
    print(f"Weight: {result:.2f}")
