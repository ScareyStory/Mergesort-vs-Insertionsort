import numpy as np
import time

def merge(left,right):

    # will hold final array to be returned
    sortedArray = []

    # while both lists are not empty
    # put the lower of each comparison into the sorted list
    while(len(left) > 0 and len(right) > 0):
        if(left[0] > right[0]):
            sortedArray.append(right[0])
            right.pop(0)
        else:
            sortedArray.append(left[0])
            left.pop(0)

    # Now either left or right will be empty

    # put the rest of left at the end of sortedArray
    while(len(left) > 0):
        sortedArray.append(left[0])
        left.pop(0)

    # put the rest of right at the end of sortedArray
    while(len(right) > 0):
        sortedArray.append(right[0])
        right.pop(0)

    # return the now sorted array
    return sortedArray


def mergesort(arr):

    # if array has been broken down to single elements
    # start popping call stack
    if(len(arr)<=1):
        return arr

    # find middle of array
    mid = len(arr) // 2

    # store left side of array and right side of array
    leftArray = arr[:mid]
    rightArray = arr[mid:]

    # recursively call mergesort on each side of array
    leftArray = mergesort(leftArray)
    rightArray = mergesort(rightArray)

    # call merge helper function
    return merge(leftArray,rightArray)

arrList = []

for i in range(0, 10):

    # generate a number between 0 and 10,000
    # amount of nums to be generated depends on current iteration
    # 1,16,81,256,...,10000 
    arr = np.random.randint(low=0, high=10000, size=((i+1)**4))
    arr = arr.tolist()

    # append array of size i^5 to arrList
    arrList.append(arr)

    # get time before running mergesort
    before = time.time()

    # call mergesort on current array
    sortedArray = mergesort(arrList[i])

    # get time after running mergesort
    after = time.time()

    # Time after minus time before gives us time elapsed
    sortTime = after-before

    # write each array size and time to sort to terminal
    print("\nArray size: "+str(len(arrList[i])))
    print("\nTime to sort: "+str('{:f}'.format(sortTime))+" seconds\n")
