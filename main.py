

def Main():

    username = input("Enter your username")
    password = input("Enter your password")

    #here we will send Credientials to login function
    #If login successful user can see the menu 

    def Menu():
        print ("Welcome to AJ Laundry")
        print ("1. Enter clothes to be washed")
        print ("2. Show Reciept")
        print ("3. Exit")

    loop = True

    while loop:
        print (Menu())
        choice = input("Enter your choice: ")

        if choice == '1':
            
            #will ask user for input

            loop1 = True
            while loop1:
                tshirtCount = '0'
                shortCount = '0'
                socksCount = '0'
                pillowCaseCount = '0'
                jacketCount = '0'


                Clothes = input("Enter clothes you want to wash (when finish enter e): ")
                if Clothes == 'short':
                    shortCount = input("how many shorts: ")
                if Clothes == 'tshirt':
                    tshirtCount = input("how many tshirts: ")
                if Clothes == 'socks':
                    socksCount = input("how many socks: ")
                if Clothes == "pillow case":
                    pillowCaseCount = input("how many pillow cases: ")
                if Clothes == "Jacket":
                    jacketCount = input("how many Jakcets: ")
                if Clothes == 'e':
                    loop1 = False

                #After that we will send input of clothes count to a function that handle the prices




        elif choice == '2':
            #Here we will get the prices from the function that calaculate the prices
            #Then, we will show the user the reciept
            print("---------------Recipet-------------------")
            print("short:        " + shortCount)
            print("tshirts:      " + tshirtCount)
            print("Socks:        " + socksCount)
            print("pillow cases: " + pillowCaseCount)
            print("Jackets:      " + jacketCount)


        elif choice =='3':
            loop = False

        else:
            input("Wrong choice, Enter a valid choice")




if __name__ == '__main__':
    Main()
