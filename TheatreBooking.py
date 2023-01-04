'''
your name: Abdulla Arid
the course code: ICS4U
file name:aarid_movieSystem.py
description of the program:Movie ticket assignment.
'''
#global lists for movie seats based on time
#movie at 6:55
time6 = [['0','1','2','3','4','5','6'],
         ['0','1','2','x','4','5','6'],
         ['0','1','2','3','4','5','6'],
         ['0','1','2','3','4','5','6'],
         ['0','x','x','3','4','5','6']]
#movie at 9
time9 = [['0','1','2','3','4','5','6'],
         ['0','1','2','3','4','5','6'],
         ['0','1','2','3','x','x','x'],
         ['0','x','2','3','4','5','6'],
         ['0','1','2','3','4','5','6']]

print("This is a movie ticket program that allows you to choose your seats at the ByTowne Movie Theatre! ")
#main menu function
def mainMenu():
    global movieSelect
    #allowing time to be set to another variable later on
    time = 0
    movieSelect = input("\nNow Playing:\n[1]Jojo Rabbit-March 2 @ 6:55pm\n[2]Jojo Rabbit-March 3 @ 9:00pm\nPlease select your choice of movie and time: ")
    #First movie is selected so we edit the seats for the first movie
    if movieSelect == '1':
        time = time6
    #Second movie is selected so we edit the seats for the second movie
    if movieSelect == '2':
        time = time9
    #while the user enters in invalid option it asks them again
    while movieSelect != '1' and movieSelect != '2':
        print("That is an invalid selection. Please select a number from the choices below")
        movieSelect = (input("\nNow Playing:\n[1]Jojo Rabbit-March 2 @ 6:55pm\n[2]Jojo Rabbit-March 3 @ 9:00pm\nPlease select your choice of movie and time: "))
    #sends the user to the next function
    return tickets(time)
#number of tickets
def tickets(time):
    global ask, tickAmountList, ticketAmount, ticketSelect, ticketSelectList
    ticketSelect = input('\nPlease enter your ticket selection:\n[1] $12.00 for Non-Members\n[2] $8.00 for ByTowne Members (with card)\n[3] $6.00 for Children under 12\nEnter your selection: ')
    #if the input isnt a valid entry, it asks them again
    while ticketSelect != '1' and ticketSelect != '2' and ticketSelect != '3':
        print("That is an invalid selection. Please select a number from the choices below")
        ticketSelect = input('\nPlease enter your ticket selection:\n[1] $12.00 for Non-Members\n[2] $8.00 for ByTowne Members (with card)\n[3] $6.00 for Children under 12\nEnter your selection: ')
    ticketSelectList = []
    #appends the ticket type to a list which will allow for price calculations
    ticketSelectList.append(ticketSelect)
    ticketAmount = int(input("Enter the number of tickets to purchase: "))
    #appends the ticket amount to a list which will allow for price calculations
    tickAmountList = []
    tickAmountList.append(ticketAmount)
    ask = input("Would you like to purchase more tickets? (y/n): ")
    #while the user wants to continue with another entry
    while ask == 'y':
        ticketSelect = input('\nPlease enter your ticket selection:\n[1] $12.00 for Non-Members\n[2] $8.00 for ByTowne Members (with card)\n[3] $6.00 for Children under 12\nEnter your selection: ')
        while ticketSelect != '1' and ticketSelect != '2' and ticketSelect != '3':
            print("That is an invalid selection. Please select a number from the choices below")
            ticketSelect = input('\nPlease enter your ticket selection:\n[1] $12.00 for Non-Members\n[2] $8.00 for ByTowne Members (with card)\n[3] $6.00 for Children under 12\nEnter your selection: ')
        ticketSelectList.append(ticketSelect)
        ticketAmount = int(input("Enter the number of tickets to purchase: "))
        tickAmountList.append(ticketAmount)
        ask = input("Would you like to purchase more tickets? (y/n): ")
        while ask != 'n' and ask != 'y':
            print('That is an invalid selection. Please select from the options below.')
            ask = input("Would you like to purchase more tickets? (y/n): ")
            tickAmountList.pop()
        #shows how many tickets were selected
    print("You have selected",sum(tickAmountList),"ticket(s).")
    #sends the user to the seat selection function
    return seatSelect(time)
def seatSelect(time):
    print("\n----------------Please choose a seat to book----------------\n") # This will have to use data from the seating list
    #top header
    print('\t1\t2\t3\t4\t5\t6\t7')
    #counts the number of seats printed
    counter = 0
    #counts how many times the for loop iterated
    counter2 = 0
    #for each row of seats
    for entry in time:
        counter2 += 1
        #this formats the list to print on the same line
        print(counter2, end = " ")
        for seat in entry:
            #keeps track of counted seats printed in each row
            counter += 1
            #if the seat is not taken and its in range of the columns it makes it a '.'
            if seat != 'x' and counter <= 6:
                print('\t.', end = " ")
                continue
            if seat != 'x' and counter > 6:
                counter = 0
                print('\t.')
                continue
            if seat == 'x' and counter <= 6:
                print('\tx', end = " ")
                continue
            if seat == 'x' and counter > 6:
                counter = 0
                print('\tx')
                continue
    print("\nNote that seats indicated by an 'x' are not available for purchase")
    #loops asks the user which seats they would like based on how many seats they pruchased
    for i in range(sum(tickAmountList)):
        #allows the program to re-ask if there are any invalid inputs
        while True:
            row = int(input("\nPlease select seat "+ str(i+1)+ " row: "))
            column = int(input("Please select seat "+ str(i+1)+ " column: "))
            if row < 1 or row > 5 or column < 1 or column > 7:
                print('Invalid input')
                continue
            #if the seat chosen is already taken
            if time[row - 1][column- 1] == 'x': # If the seat is taken, don't let user buy tickets
                print('\nSeat already taken!')
                continue
            else:
                time[row - 1][column - 1] = 'x'
                break
    #sends the user to the price function
    return(totalCost())
def totalCost():
    total = []
    #checks each index
    for i in range(0,len(tickAmountList)):
        if ticketSelectList[i] == '1' and tickAmountList[i] >= 1:
            print(tickAmountList[i], "non-member tickets: $", format(12*tickAmountList[i], '.2f'))
            total.append(12*tickAmountList[i])
        elif ticketSelectList[i] == '2' and tickAmountList[i] >= 1:
            print(tickAmountList[i], "member tickets: $", format(8*tickAmountList[i], '.2f'))
            total.append(8*tickAmountList[i])
        elif ticketSelectList[i] == '3' and tickAmountList[i] >= 1:
            print(tickAmountList[i], "child tickets: $", format(6*tickAmountList[i], '.2f'))
            total.append(6*tickAmountList[i])
    print('Total: $',format(sum(total),'.2f'))
    print('Taxes: $',format((sum(total)*1.13)-sum(total),'.2f'))
    print('Total price: $',format(sum(total)*1.13,'.2f'))
    print("Your credit card has been charged the above total. The charge will be from ByTowne Cineplex. Enjoy your viewing experience!")
    return(mainMenu())

mainMenu()
