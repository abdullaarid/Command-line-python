'''
your name: Abdulla Arid
the course code: ICS4U
file name:AArid_InheritenceTask01.py
Description of the program: Classes inheritence assignment
'''
#lists created to hold dog data
serviceDogs = []
petDogs = []


print("This is a program to keep track of your dogs details as well as the owners")
#parent dog class
class Dog:
    def __init__(self):
        #terms will be set to the input
        self.name = None
        self.breed = None
        self.weight = None
        self.sex = None
        self.dob = None
    #sets the function name
    def set_name(self, name):
        self.name = name
    def set_breed(self, breed):
        self.breed = breed
    def set_weight(self, weight):
        self.weight= weight
    def set_sex(self, sex):
        self.sex= sex
    def set_dob(self, dob):
        self.dob= dob
    #allows the program to print the inputs
    def get_name(self):
        return self.name
    def get_breed (self):
        return self.breed
    def get_weight(self):
        return self.weight
    def get_sex(self):
        return self.sex
    def get_dob(self):
        return self.dob

#PetDog subclass
class PetDog(Dog):
    def __init__(self):
        Dog.__init__(self)
        self.OwnerName = None
        self.OwnerAddress = None
    #sets the owner name
    def set_OwnerName(self, OwnerName):
        self.OwnerName= OwnerName
    #sets the address
    def set_OwnerAddress(self, OwnerAddress):
        self.OwnerAddress= OwnerAddress
    def get_OwnerName(self):
        return self.OwnerName
    def get_OwnerAddress(self):
        return self.OwnerAddress

#Service dog subclass
class ServiceDog(Dog):
    def __init__(self):
        #Dog.__init__(self)
        self.BusinessName = None
        self.BusinessAddress = None
    #sets the names from inputs
    def set_BusinessName(self, BusinessName):
        self.BusinessName= BusinessName
    def set_BusinessAddress(self, BusinessAddress):
        self.BusinessAddress= BusinessAddress
    def set_WorkType(self, WorkType):
        self.WorkType= WorkType
    #allows the printing of the inputs
    def get_BusinessName(self):
        return self.BusinessName
    def get_BusinessAddress(self):
        return self.BusinessAddress
    def get_WorkType(self):
        return self.WorkType
#function made rather than making clutter
def createPetDog():
    #allows the class to be set to an object
    dog = Dog()
    #Sets input then appends to the list
    dog.set_name(input("\nPlease enter your dog's name: "))
    petDogs.append(dog.get_name())
    dog.set_breed(input("Please enter your dog's breed: "))
    petDogs.append(dog.get_breed())
    dog.set_weight(input("Please enter your dog's weight: "))
    petDogs.append(dog.get_weight())
    dog.set_sex(input("Please enter your dog's sex: "))
    petDogs.append(dog.get_sex())
    dog.set_dob(input("Please enter your dog's date of birth: "))
    petDogs.append(dog.get_dob())
    #prints all the data
    print("\nName:",dog.get_name())
    print("Breed:",dog.get_breed())
    print("Weight:",dog.get_weight())
    print("Sex:",dog.get_sex())
    print("Date of Birth:",dog.get_dob())
    #Sets input then appends to the list
    petDog = PetDog()
    petDog.set_OwnerName(input("\nPlease enter the owner's name: "))
    petDogs.append(petDog.get_OwnerName())
    petDog.set_OwnerAddress(input("Please enter the owner's address: "))
    petDogs.append(petDog.get_OwnerAddress())
    #prints all the data
    print("\nOwner name:",petDog.get_OwnerName())
    print("Owner address:",petDog.get_OwnerAddress())
#function made rather than making clutter
def createServiceDog():
    dog = Dog()
    #Sets input then appends to the list
    dog.set_name(input("\nPlease enter your dog's name: "))
    serviceDogs.append(dog.get_name())
    dog.set_breed(input("Please enter your dog's breed: "))
    serviceDogs.append(dog.get_breed())
    dog.set_weight(input("Please enter your dog's weight: "))
    serviceDogs.append(dog.get_weight())
    dog.set_sex(input("Please enter your dog's sex: "))
    serviceDogs.append(dog.get_sex())
    dog.set_dob(input("Please enter your dog's date of birth: "))
    serviceDogs.append(dog.get_dob())
    #prints all the data
    print("\nName:",dog.get_name())
    print("Breed:",dog.get_breed())
    print("Weight:",dog.get_weight())
    print("Sex:",dog.get_sex())
    print("Date of Birth:",dog.get_dob())
    #Sets input then appends to the list
    serviceDog = ServiceDog()
    serviceDog.set_BusinessName(input("\nPlease enter the business name: "))
    serviceDogs.append(serviceDog.get_BusinessName())
    serviceDog.set_BusinessAddress(input("Please enter the business' address: "))
    serviceDogs.append(serviceDog.get_BusinessAddress())
    serviceDog.set_WorkType(input("Please enter the dog's work type: "))
    serviceDogs.append(serviceDog.get_WorkType())
    #prints all the data
    print("\nBusiness name:",serviceDog.get_BusinessName())
    print("Business address:",serviceDog.get_BusinessAddress())
    print("Work type:",serviceDog.get_WorkType())
#list that will appear at the end to show all the dogs entered
def finalList():
    #makes the petdog list into a 2d list that is grouped in 7s so that a description could be added to each one
    petDogs1 = [petDogs[i:i + 7] for i in range(0, len(petDogs), 7)]
    #goes through each dog
    for i in petDogs1:
        print("\nName: " ,i[0])
        print("Breed: ",i[1])
        print("Weight: ",i[2])
        print("Sex: ",i[3])
        print("Date of Birth: ",i[4])
        print("Owner name: ",i[5])
        print("Owner address: ",i[6])
    #makes the servicedog list into a 2d list that is grouped in 7s so that a description could be added to each one
    serviceDogs1 = [serviceDogs[i:i + 8] for i in range(0, len(serviceDogs), 8)]
    #goes through each dog
    for i in serviceDogs1:
        print("\nName: " ,i[0])
        print("Breed: ",i[1])
        print("Weight: ",i[2])
        print("Sex: ",i[3])
        print("Date of Birth: ",i[4])
        print("Business name: ",i[5])
        print("Business address: ",i[6])
        print("Work type: ",i[7])
while True:
    #determines the function to use
    PetOrService = input("\nWould you like to enter details for a pet or Service dog(Enter 'pet' or 'service'): ")
    if PetOrService == "pet" or PetOrService == "Pet":
        createPetDog()
    elif PetOrService == "Service" or PetOrService == "service":
        createServiceDog()
    #goes back to the beginning
    else:
        print("Please enter a valid option")
        continue
    Another = input("\nWould you like to add another dog(yes or no)?: ")
    if Another == "yes"or Another == "Yes":
        continue

    else:
        finalList()
        print("\nThank you for using using the program!")
        break
