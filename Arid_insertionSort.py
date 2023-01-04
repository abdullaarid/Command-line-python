global count
def insertionSort(list):
    for i in range (1,len(list)):
        term = list[i]
        comparison = i -1
        while comparison >= 0:
            if term < list[comparison]:
                count.append(1)
                list[comparison+1] = list[comparison]
                list[comparison] = term
                comparison = comparison - 1
            else:
                break
    print(myList)
count = []
myList = [5,2,7,1,9,3,6]
insertionSort(myList)
print("Total comparisons:", sum(count))
