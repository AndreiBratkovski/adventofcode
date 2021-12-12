#!/usr/bin/env python3

my_input =  open("day1-input.txt", "r")
depth_inputs = [int(n) for n in my_input.read().splitlines()]
previous_depth_group_sum = -1
result = 0
for i in range(0, len(depth_inputs)):
    current_depth_group_sum = sum(depth_inputs[i:i+3])
    if current_depth_group_sum > previous_depth_group_sum and previous_depth_group_sum != -1:
        result += 1
    previous_depth_group_sum = current_depth_group_sum

print(result)
