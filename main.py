from login_service import login
from Orderprice import *

def Main():


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
            tshirtCount = 0
            shortCount = 0
            socksCount = 0
            pillowCaseCount = 0
            jacketCount = 0
            
            #will ask user for input

            loop1 = True
            while loop1:
                


                Clothes = input("Enter clothes you want to wash (when finish enter e): ")
                if Clothes == 'short':
                    shortCount = int(input("how many shorts: "))
                if Clothes == 'tshirt':
                    tshirtCount = int(input("how many tshirts: "))
                if Clothes == 'socks':
                    socksCount = int(input("how many socks: "))
                if Clothes == "pillow case":
                    pillowCaseCount = int(input("how many pillow cases: "))
                if Clothes == "Jacket":
                    jacketCount = int(input("how many Jakcets: "))
                if Clothes == 'e':
                    loop1 = False

            exedite = int(input("Do you want expedited cleaning or normal (enter 1 for expedite 2 for normal=> "))
            iron = int(input("Enter 1 for ironing 2 for no ironing => " ))
            prefume = int(input("Enter 1 for prefume 2 for no => "))
            droptime = int(input("Enter Drop time => "))
            comment = input("Enter any other information about your items=> ")

                #After that we will send input of clothes count to a function that handle the prices
                #After geting the cleaning price we will send the choices to a function
                #that will calculate the time will take for cleaning the clothes and final price
            shortcost = shortCount * 2
            tshirtcost = tshirtCount * 2
            sockscost = socksCount * 1
            pillowcost = pillowCaseCount * 2
            jacketcost = jacketCount * 2
            total = shortcost + tshirtcost +sockscost + pillowcost + jacketcost
            orderprice = Orderprice()
            orderprice.totaldue(total)
            orderprice.droptime(droptime)
            orderprice.expedite(exedite)
            orderprice.prefume(prefume)
            orderprice.iron(iron)
            orderprice.comment(comment)

            



        elif choice == '2':
            #Here we will get the prices from the function that calaculate the prices
            #Then, we will show the user the reciept
            print("---------------Recipet-------------------")
            print("short:        " , shortCount,      "---------> $", shortcost)
            print("tshirts:      " , tshirtCount,    "---------> $", tshirtcost)
            print("Socks:        " , socksCount,     "---------> $", sockscost)
            print("pillow cases: " , pillowCaseCount, "---------> $", pillowcost)
            print("Jackets:      " , jacketCount,     "---------> $", jacketcost)
            print("***************************************")
            
            orderprice.printTotaldue()


        elif choice =='3':
            loop = False

        else:
            input("Wrong choice, Enter a valid choice")




if __name__ == '__main__':
    Main()
