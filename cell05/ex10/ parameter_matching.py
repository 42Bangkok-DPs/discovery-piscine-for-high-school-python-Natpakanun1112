#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
    print("none")
else:
    x = sys.argv[1]

    y = input("what was the parameter? ")

    if y == x:
        print("good job!")
    else:
        print("Nope, sorry...")
            