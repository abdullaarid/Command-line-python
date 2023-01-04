roomList = []
room = ["You are in the Second Bedroom.",None,1,None,None]
roomList.append(room)
room = ["You are in the South Hall.",4,2,None,0]
roomList.append(room)
room = ["You are in the Dining Room.",5,None,None,1]
roomList.append(room)
room = ["You are in the First Bedroom.",None,4,None,None]
roomList.append(room)
room = ["You are in the North hall.",6,5,1,3]
roomList.append(room)
room = ["You are in the Kitchen",None,None,2,4]
roomList.append(room)
room = ["You are in the Balcony.",None,None,4,None]
roomList.append(room)

currentRoom = 0

print("Exit anytime by entering 'exit'")
done = True
while True:
    print()
    print(roomList[currentRoom][0])
    choice = input("What direction would you like to go(n,e,s,w)?: ")
    if choice == "n" or choice == "N" or choice == "North" or choice == "north":
        nextRoom = roomList[currentRoom][1]
        #print(nextRoom)
        if nextRoom == None:
            print("You can't go that way!")
        else:
            currentRoom = nextRoom
    elif choice == "e" or choice == "E" or choice == "East" or choice == "east":
        nextRoom = roomList[currentRoom][2]
        if nextRoom == None:
            print("You can't go that way!")
        else:
            currentRoom = nextRoom
    elif choice == "s" or choice == "S" or choice == "South" or choice == "south":
        nextRoom = roomList[currentRoom][3]
        if nextRoom == None:
            print("You can't go that way!")
        else:
            currentRoom = nextRoom
    elif choice == "w" or choice == "W" or choice == "West" or choice == "west":
        nextRoom = roomList[currentRoom][4]
        if nextRoom == None:
            print("You can't go that way!")
        else:
            currentRoom = nextRoom
    elif choice == "exit" or "Exit":
        break
    else:
        print("\nPlease enter a valid option!")
print("Thank you for using the program!")
