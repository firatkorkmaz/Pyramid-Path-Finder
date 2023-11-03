# OPTIONAL: Pyramid-Shaped Integer Data Generator with Different Rows of Random Numbers Between 001 and 999
# Re-Generate the File If the Main Program Gives 0-Element Path (Prime Numbers Prevent Reaching the Bottom)

from random import *

def generate_pyramid(depth, max_value):
    content = ""                # String for the Whole File

    for i in range(1, depth + 1):
        line = ""               # String for Each Line

        for j in range(i):
            if j != 0:
                line += " "     # Putting Space Between the Numbers
            line += str(randint(1, max_value)).zfill(3)  # zfill(3): 1 >> 001 || 11 >> 011

        content += line + '\n'  # Adding Each Line to the Big Content String

    return content              # Returning the Content of the File


while True:
    depth = input("\nDepth of Pyramid Data: ").strip()
    if not depth.isdigit():
        print("Please Enter An Integer!\n")
        continue
    else:
        depth = int(depth)
        break
    
filename = "random_pyramid.txt"
max_value = 999                 # Numbers with Up to 3 Digits

with open(filename, 'w') as file:
    content = generate_pyramid(depth, max_value)
    file.write(content)         # Writing the Randomly Generated Integer Pyramid to File
    print("\nNew Pyramid Data with Random Numbers:")
    print(f"Depth: {depth}, File: \"random_pyramid.txt\"")