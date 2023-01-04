'''
your name: Abdulla Arid
the course code: ICS4U
file name:AArid_SearchAndSort.py
Description of the program: Dungeons and Dragons character creation program with search and sort
'''
import csv, random
from datetime import datetime
nameList = []
print("This is a Dungeons and Drangons program")
#line will always be called when running the program and creates the headers
with open("character.csv","w",newline = "") as csvfile:
    writeCSV = csv.writer(csvfile)
    writeCSV.writerow(["Adventure's name","Class","Race","Strength","Constitution","Dexterity",
    "Intelligence","Wisdom","Charisma","Back Slot","Belt Slot","Right Hand","Left Hand","Pack"])
#creates random stats, weapons and items
class character:
    def __init__(self):
        self.build = {"Class" : random.choice(['Fighter', 'Wizard', 'Thief', 'Healer', 'Ranger']),"Race" : random.choice(["Human", "Elf", "Dwarf", "Halfling", "Gnome"])}
        self.stats = {'Strength' : random.randint(1,20), 'Constitution' : random.randint(1,20),'Dexterity' : random.randint(1,20),'Intelligence' : random.randint(1,20),
        'Wisdom' : random.randint(1,20),'Charisma' : random.randint(1,20)}
    def pickWeapon(self):
        weapon = random.choice(["Small Axe","Medium Axe","Large Axe","Small Sword","Medium Sword","Large Sword","Crossbow", "Short Bow", "Longbow"])
        return weapon
    def pickHands(self):
        item = random.choice(["Torch", "Lamp", "Key", "Map", "Empty","Wand", "Scroll", "Ring"])
        return item
    def pickPack(self):
        list = ["Torch", "Lamp", "Key", "Map", "Empty","Wand", "Scroll", "Ring","Red Potion", "Blue Potion", "Green Potion",
        "Gems", "Coins", "Artifact","Food", "Healing Potions"]
        self.items = random.sample(list,10)
        #returns as a string without the list brackets
        return ', '.join(self.items)
def menu():
    #program will always return to the menu after each selection
    while True:
        select = input("\nMenu:\n1.Create new character\n2.View character(s)\n3.Linear Search\n4.Binary Search\n5.Insertion Sort\n6.Bubble Sort\n7.Exit\nSelection: ")
        if select == "1":
            create()
        elif select == "2":
            view()
        elif select == "3":
            linearSearch()
        elif select == "4":
            binarySearch()
        elif select == "5":
            insertionSort()
        elif select == "6":
            bubbleSort()
        elif select == "7":
            break
        else:
            print('Please enter a valid option by entering a number from the menu!')
#mennu #1. Creates a chara
def create():
        with open("character.csv","a",newline = "") as csvfile:
            writeCSV = csv.writer(csvfile)
            first = input("Please enter the character's first name: ")
            #if the name is blank takes to menu
            if first == "":
                print("You must enter a first name!")
                return
            last = input("Please enter the character's last name: ")
            #if the name is blank takes to menu
            if last == "":
                print("You must enter a last name!")
                return
            #adds the names together so it is has its own header for the names combined
            name = str(first + " " + last)
            #if the name has already been added to a list the stores names, it returns to menu
            if name in nameList:
                print("That name has already been used!")
                return
            #if the name hasnt been used, it adds it to the list of names
            else:
                nameList.append(first+" "+last)
            characters = character()
            #creates a new row in the csv that contains all the data in the order of the headers
            writeCSV.writerow([first+" "+last,characters.build["Class"],characters.build["Race"],characters.stats["Strength"],characters.stats['Constitution'],
            characters.stats['Dexterity'],characters.stats['Intelligence'],characters.stats['Wisdom'],characters.stats['Charisma'],characters.pickWeapon(),characters.pickWeapon(),
            characters.pickHands(),characters.pickHands(),characters.pickPack()])
def view():
    #reads file
    with open('character.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        #in order to see if the there are characters already created or not.
        test = 0
        for row in reader:
            print("\nName:",row["Adventure's name"])
            print("Class:",row["Class"])
            print("Race:",row["Race"])
            print("Strength:",row["Strength"])
            print("Constitution:",row["Constitution"])
            print("Dexterity:",row["Dexterity"])
            print("Intelligence:",row["Intelligence"])
            print("Wisdom:",row["Wisdom"])
            print("Charisma:",row["Charisma"])
            print("Back Slot:",row["Back Slot"])
            print("Belt Slot:",row["Belt Slot"])
            print("Right Hand:",row["Right Hand"])
            print("Left Hand:",row["Left Hand"])
            print("Pack:",row["Pack"])
            test += 1
        else:
            #if there are characters, it passes
            if test != 0:
                pass
            #if there arent it tells the user to create one
            elif test == 0:
                print("Please create a new character from the menu!")


def linearSearch():
    with open('character.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        found = False
        position = 0
        if len(nameList) == 0:
            print("Please create a new character in the menu to begin searching items!")
            return
        search = input("\nPlease enter a character's full name: ")
        if search not in nameList:
            print("That character has not been created! You can create a new character in the menu.")
            return
        for row in reader:
            if row["Adventure's name"] == search:
                newList = row["Pack"].split(", ")
        myItem = input("What Item Are you looking for(case sensitive)?: ")
        while position < len(newList) and not found:
            #if position 0 is the item, found is true. else, it continues and adds 1 to position then chaecks to see if found is true
            if newList[position] == myItem:
                found = True
            position += 1
        #prints if item is found or not
        if found == True:
            print("Item found")
        elif found == False:
            print("Item not found")

def binarySearch():
    with open('character.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        #reader2 = csv.DictReader(csvfile)
        found = False
        bottom = 0
        #if there are no characters created
        if len(nameList) == 0:
            print("Please create a new character in the menu to begin searching items!")
            return
        search = input("\nPlease enter a character's full name: ")
        if search not in nameList:
            print("That character has not been created! You can create a new character in the menu.")
            return
        for row in reader:
            if row["Adventure's name"] == search:
                newList = [int(row["Strength"]), int(row["Constitution"]), int(row["Dexterity"]), int(row["Intelligence"]), int(row["Wisdom"]), int(row["Charisma"])]
        #prints out the stat titles without any numbers
        print("\nStrength:")
        print("Constitution:")
        print("Dexterity:")
        print("Intelligence:")
        print("Wisdom:")
        print("Charisma:")
        sortedList = newList.sort()
        #list needs to be sorted in order to search using the binary search method
        top = len(newList) - 1
        #user needs to enter a number, or the program will return to menu
        try:
            numChoice = int(input("\nChoose a stat value that you would like to find: "))
        except ValueError:
            print("Please enter a number!")
            return
        #binary search method
        while bottom <= top and not found:
            middle = (bottom + top)//2
            if newList[middle] == numChoice:
                found = True
            elif newList[middle] < numChoice:
                bottom = middle + 1
            else:
                top = middle - 1
        if found == True:
            print("\nValue found in stats")
        elif found == False:
            print("\nValue not found in stats")
    #resets csv by reopening as seek doesnt work with DictReader
    with open('character.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        #prints characters details when finished
        for row1 in reader:
            if row1["Adventure's name"] == search:
                print("Strength:",row1["Strength"])
                print("Constitution:",row1["Constitution"])
                print("Dexterity:",row1["Dexterity"])
                print("Intelligence:",row1["Intelligence"])
                print("Wisdom:",row1["Wisdom"])
                print("Charisma:",row1["Charisma"])

def insertionSort():
    with open('character.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        #if no charcters have been entered
        if len(nameList) == 0:
            print("Please create a new character in the menu to begin searching items!")
            return
        search = input("\nPlease enter a character's full name: ")
        if search not in nameList:
            print("That character has not been created! You can create a new character in the menu.")
            return
        #creates a list with the names and values of the stats
        for row in reader:
            if row["Adventure's name"] == search:
                newList = [["Strength",int(row["Strength"])],["Constitution",int(row["Constitution"])], ["Dexterity",int(row["Dexterity"])],["Intelligence", int(row["Intelligence"])], ["Wisdom",int(row["Wisdom"])], ["Charisma",int(row["Charisma"])]]
        #allows for time to be claculated
        startTime = datetime.now()
        #insertion sort method
        for i in range (1,len(newList)):
            #the name also moves with the value
            term = newList[i][1]
            statname = newList[i][0]
            comparison = i -1
            while comparison >= 0:
                if term < newList[comparison][1]:
                    #value changing line and then name changing line
                    newList[comparison+1][1] = newList[comparison][1]
                    newList[comparison+1][0] = newList[comparison][0]
                    #value changing line and then name changing line
                    newList[comparison][0] = statname
                    newList[comparison][1] = term
                    comparison = comparison - 1
                else:
                    break
        print("\nSorted List:")
        for stat in newList:
            #prints the name then stat
            print(str(stat[0])+": "+str(stat[1]))
        #prints the time taken
        print ("Total Time Taken: " ,datetime.now() - startTime)

def bubbleSort():
    with open('character.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        #if no characters have been created
        if len(nameList) == 0:
            print("Please create a new character in the menu to begin searching items!")
            return
        search = input("\nPlease enter a character's full name: ")
        #if the name hasnt been created
        if search not in nameList:
            print("That character has not been created! You can create a new character in the menu.")
            return
        for row in reader:
            if row["Adventure's name"] == search:
                newList = [["Strength",int(row["Strength"])],["Constitution",int(row["Constitution"])], ["Dexterity",int(row["Dexterity"])],["Intelligence", int(row["Intelligence"])], ["Wisdom",int(row["Wisdom"])], ["Charisma",int(row["Charisma"])]]
        #variable for determining if list needs to continue switching
        moreSwaps = True
        #used to determine time taken
        startTime = datetime.now()
        #Bubble sort method
        while moreSwaps:
            moreSwaps = False
            for element in range(len(newList)-1):
                if newList[element][1]> newList[element+1][1]:
                    moreSwaps = True
                    temp = newList[element][1]
                    tempName = newList[element][0]
                    #value changing line and then name changing line
                    newList[element][1] = newList[element+1][1]
                    newList[element][0] = newList[element+1][0]
                    #value changing line and then name changing line
                    newList[element+1][1] = temp
                    newList[element+1][0] = tempName
        print("\nSorted List:")
        #prints the name then stat
        for stat in newList:
            print(str(stat[0])+": "+str(stat[1]))
        print ("Total Time Taken:",datetime.now() - startTime)
#main program calls menu
menu()
print("Thank you for using the program!")
