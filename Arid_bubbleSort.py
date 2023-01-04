global totalComp
def bubbleSort(myList):
    moreSwaps = True
    while moreSwaps:
        moreSwaps = False
        for element in range(len(myList)-1):
            if myList[element]> myList[element+1]:
                totalComp.append(1)
                moreSwaps = True
                temp = myList[element]
                myList[element] = myList[element+1]
                myList[element+1] = temp
    return myList


def testbubbleSort():
    myList = [5,2,7,1,9,3,6]
    sortedList = bubbleSort(myList)
    print(sortedList)

totalComp = []
testbubbleSort()
print("Total comparisons:",sum(totalComp))
