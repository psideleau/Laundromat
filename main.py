def Main():

    raw_input("Enter your username")
    raw_input("Enter your password")

    #here we will send Credientials to login function
    #If login successful user can see the menu 

    def Menu():
        print "Welcome to AJ Laundry"
        print "1. Enter clothes to be washed"
        print "2. Show Reciept"
        print "3. Exit"

    loop = True

    while loop:
        print Menu()
        choice = input("Enter your choice: ")

        if choice ==1:
            #will ask user for input
            print("choice 1 selected: ")

        elif choice ==2:
            #will show the user the reciept
            print("choice 2 selected")

        elif choice ==3:
            loop = False

        else:
            raw_input("Wrong choice, Enter a valid choice")




if __name__ == '__main__':
    Main()
