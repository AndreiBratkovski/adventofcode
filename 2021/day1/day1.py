#!/usr/bin/env python3

my_input =  open("day1-input.txt", "r")
depth_inputs = [int(n) for n in my_input.read().splitlines()]
previous_depth = -1
result = 0
for current_depth in depth_inputs:
    if current_depth > previous_depth and previous_depth != -1:
        result += 1
    previous_depth = current_depth

print(result)
