import math

length = input();
input = input();
str_arr = input.split(' ');
arr = [int(num) for num in str_arr]

# Find highest value in array
def findHighest(arr):
    highestValue = -math.inf
    for num in arr:
        if num > highestValue:
            highestValue = num;
    return highestValue

# Find value's index in array
def findIndex(arr, value):
    index = 0
    for i, num in enumerate(arr):
        if num == value:
            index = i
    return index

# Remove duplicate values from an array
def removeDuplicates(arr):
    return list(dict.fromkeys(arr))

# Get highest score value/index
highestScore = findHighest(arr)

# Clear duplicates of highest score
arr = removeDuplicates(arr)

highestScoreIndex = findIndex(arr, highestScore)

del arr[highestScoreIndex]

runnerUpScore = findHighest(arr)

print(runnerUpScore)
