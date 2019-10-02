import numpy as np
import time

def insertsort(arr):

    for i in range(0, len(arr)):

        # val is value at current index
        val = arr[i]

        # j holds the previous index
        j = i-1

        # while j is a valid index and the value at current index is
        # less than the value at previous index
        # swap the values
        while(j >= 0 and val < arr[j]):
            arr[j+1] = arr[j]
            j-=1

        # store val at where j+1 sorted to
        arr[j+1] = val

    return arr

arrList = []

for i in range(0, 10):

    # generate a number between 0 and 10,000
    # amount of nums to be generated depends on current iteration
    # 1,32,243,1024,...,10000 
    arr = np.random.randint(low=0, high=10000, size=((i+1)**4))
    arr = arr.tolist()

    # append array of size i^5 to arrList
    arrList.append(arr)

    # get time before running mergesort
    before = time.time()

    # call mergesort on current array
    sortedArray = insertsort(arrList[i])

    # get time after running mergesort
    after = time.time()

    # Time after minus time before gives us time elapsed
    sortTime = after-before

    # write each array size and time to sort to terminal
    print("\nArray size: "+str(len(arrList[i])))
    print("\nTime to sort: "+str('{:f}'.format(sortTime))+" seconds\n")