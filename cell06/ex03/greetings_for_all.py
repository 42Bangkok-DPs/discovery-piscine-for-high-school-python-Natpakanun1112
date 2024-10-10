#!/usr/bin/env python3

def greetings(n="noble straanger"):
    if not isinstance(n, str):
       print("Error! It was not a name.")
    else:
        print(f"Hello, {n}.")

greetings('Alexandra') 
greetings('Will')  
greetings()
greetings(42)
