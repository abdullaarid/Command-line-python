def binarySearch(myItem,myList):
    found = False
    bottom = 0
    itemSearched = []
    top = len(myList) - 1
    while bottom <= top and not found:
        middle = (bottom + top)//2
        if myList[middle] == myItem:
            itemSearched.append(1)
            found = True
        elif myList[middle] < myItem:
            itemSearched.append(1)
            bottom = middle + 1
        else:
            itemSearched.append(1)
            top = middle - 1

    print("searches done:",sum(itemSearched))
    return found


if __name__ == "__main__":
    numberList = [1,4,6,8,12,15,18,19,24,27,31,42,43,58]
    num = int(input("What number are you looking for?: "))
    isitFound = binarySearch(num,numberList)
    if isitFound is True:
        print("Your number is in the list!")
    else:
        print("Your number is not in the list")
