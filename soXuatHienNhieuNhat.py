import sys

input_str = input()

def solve(input_str):
    res = max([input_str.count(i) for i in input_str])
    for i in input_str:
        if input_str.count(i)==res:
            return i
solve(input_str)
