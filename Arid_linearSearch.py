def linearSearch(myItem,myList):
    found = False
    position = 0
    itemSearched = 0
    while position < len(myList) and not found:
        if myList[position] == myItem:
            itemSearched += 1
            found = True
    print("items searched:",itemSearched)
    return found

if __name__ == "__main__":
    shopping = ["apples","bananas","chocolate","pasta"]
    item = input("What item do you want to find?: ")
    isitFound = linearSearch(item,shopping)
    if isitFound is True:
        print("item found!")
    else:
        print("item not found")
        while True:
            add = input("Would you like to add this item to your list(Yes or No)?")
            if add == "yes" or add == "Yes":
                shopping.append(item)
                print(shopping)
                print("Item added!")
                break
            elif add == "no" or add == "No":
                print("Thank you for using the program!")
                break
            else:
                continue
