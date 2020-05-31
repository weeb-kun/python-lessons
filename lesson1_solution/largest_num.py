# e.g.
numList = [1, 4, 5, 7, 5, 3, 23, 13, 4, 18]

def largestNum(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max

print(largestNum(numList))
