'''
your name: Abdulla Arid
the course code: ICS4U
file name:AArid_SearchAndSort.py
Description of the program: Dungeons and Dragons character creation
'''
import csv, random
nameList = []
print("This is a Dungeons and Drangons program")
with open("character2.csv","w",newline = "") as csvfile:
    writeCSV = csv.writer(csvfile)
    writeCSV.writerow(["Adventure's name","Class","Race","Strength","Constitution","Dexterity",
    "Intelligence","Wisdom","Charisma","Back Slot","Belt Slot","Right Hand","Left Hand","Pack"])

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
        return ', '.join(self.items)
def menu():
    while True:
        select = input("\nMenu:\n1.Create new character\n2.View charcter(s)\n3.Linear Search\n4.Exit\nSelection: ")
        if select == "1":
            if len(nameList) == 0:
                create()
            else:
                print("\nYou have already created a character! You can view the character in the menu.")
        elif select == "2":
            view()
        elif select == "3":
            isitFound = linearSearch()
            if isitFound == True:
                print("Found")
            else:
                print("Not found")
            continue
        elif select == "4":
            break
        else:
            print('Please enter a valid option by entering a number from the menu!')
def create():
        with open("character2.csv","a",newline = "") as csvfile:
            writeCSV = csv.writer(csvfile)
            first = input("Please enter the character's first name: ")
            last = input("Please enter the character's last name: ")
            name = str(first + " " + last)
            if name in nameList:
                print("That name has already been used!")
                return
            else:
                nameList.append(first+" "+last)
            characters = character()
            writeCSV.writerow([first+" "+last,characters.build["Class"],characters.build["Race"],characters.stats["Strength"],characters.stats['Constitution'],
            characters.stats['Dexterity'],characters.stats['Intelligence'],characters.stats['Wisdom'],characters.stats['Charisma'],characters.pickWeapon(),characters.pickWeapon(),
            characters.pickHands(),characters.pickHands(),characters.pickPack()])
def view():
    with open('character2.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
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
            if test != 0:
                pass
            elif test == 0:
                print("Please create a new character from the menu!")


def linearSearch():
    with open('character2.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        found = False
        position = 0
        itemSearched = 0
        for row in reader:
            x = row["Pack"].split(", ")

        print(x)
        print(len(x))
        myItem = input("What Item Are you looking for?: ")
        while position < len(x) and not found:
            if x[position] == myItem:
                found = True
            itemSearched += 1
            position += 1
        print("items searched:",itemSearched)
        return found

menu()
print("Thank you for using the program")
