# FIND MAXIMUM 
## Give an integer array, return the largest element

import random

while True :
    # Request Array size 
    n = input("Array Size: ")
    # Validate n is a coorect value
        
    if n.isdigit():
        # Define Array
        n = int(n)
        if n <= 10:
            
        else:  
            array = [None] * n
        
        break
    else: 
        print(f"The value {n} is not valid, please enter a integer number.")