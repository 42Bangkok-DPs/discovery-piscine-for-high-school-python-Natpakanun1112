#!/usr/bin/env python3
x = [2, 8, 9, 48, 8, 22, -12, 2]
y = [x + 2 for x in x]
print(x + 2 for x in x)
print("New array:", y)
