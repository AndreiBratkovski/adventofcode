#!/usr/bin/env python3
my_input =  open("day2-input.txt", "r")
move_inputs = [s for s in my_input.read().splitlines()]
horizontal = 0
depth = 0
for move_input in move_inputs:
    split_move_input = move_input.split()
    direction = split_move_input[0]
    value = int(split_move_input[1])
    if direction == "forward":
        horizontal += value
    elif direction == "up":
        depth -= value
    elif direction == "down":
        depth += value
print(f"horizontal: {horizontal}")
print(f"depth: {depth}")
multiplied = horizontal * depth
print(f"multiplied: {multiplied}")
