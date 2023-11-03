# Finding the Path of Non-Prime Values from Top to Bottom with Maximum Sum #

import sys

# Function to Detect Prime Numbers
def isPrime(num):
    if num <= 1:
        return False                   # Not Prime

    for i in range(2, num // 2 + 1):   # Checking Up to "num // 2" is Enough for Each num
        if (num % i) == 0:
            return False               # Not Prime

    return True                        # Prime Number


def main(filename=None):
    if filename == None:
        filename = input("\nFilename of the Pyramid Data: ").strip()

    try:
        file = open(filename, "r")
    except:
        print(f"\n{filename} File cannot Be Read!")
        return

    pyNumbers = []        # Complete List of Rows for the Pyramid 

    print()
    for line in file:
        pyNumbers.append([int(x) for x in line.rstrip().split()])      # Getting the Rows
        for i in pyNumbers[-1]: print(str(i).zfill(3), end=" ")        # Printing the Rows
        print()

    file.close()

    maxSum, maxPath = maxSumPath(pyNumbers, 0, 0)        # Calling the Recursive maxSumPath() Function
    for i in range(len(line) - 1): print("-", end="")    # Drawing a Line After Printing the Pyramid 
    print(f"\n\n{len(maxPath)} Elements of the Path with Maximum Sum = {maxSum}: ")
    print(*maxPath[::-1], sep=" => ")     # Printing the Elements of the Maximum Path with Separator: "=>"
    if len(maxPath) == 0:
        print("Prime Numbers Prevent Reaching the Bottom of the Pyramid, There is Not Any Path Available!")


def maxSumPath(pathList, i, j):
    # If the Visited Number is Prime, the Way is Shut. Change Your Path!
    if (isPrime(pathList[i][j])):
        return -1, []

    elif (i == len(pathList) - 1):           # If the Bottom is Reached and This Number is Not Prime
        return pathList[i][j], [pathList[i][j]]            # Return the Values of the Current Number

    leftValue, leftPath = maxSumPath(pathList, (i + 1), j)          # Collecting Values for leftPath
    rightValue, rightPath = maxSumPath(pathList, (i + 1), (j + 1))  # Collecting Values for rightPath

    # Checking Which Value is Greater and Not Prime
    if (leftValue > rightValue and leftValue != -1):
        leftValue += pathList[i][j]
        leftPath.append(pathList[i][j])

    elif (rightValue != -1):
        rightValue += pathList[i][j]
        rightPath.append(pathList[i][j])

    #######################################

    # Getting the Value of Non-Interrupted Path or the Greater Value If Both Paths Have the Same Length
    if (len(leftPath) > len(rightPath) or len(leftPath) == len(rightPath) and leftValue > rightValue):
        return leftValue, leftPath

    else:
        return rightValue, rightPath


if __name__ == '__main__':
    # filename = "input.txt"
    # main(filename)
    if len(sys.argv) == 1:
        main()
    else:
        main(sys.argv[1])