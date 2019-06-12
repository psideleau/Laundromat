class orderprice:
    def dropTIme(self):  
        print ("Enter a dropoff time between 900hours and 1500hours:")
        droptime = raw_input("> ")

        if droptime in range(9, 3):
            print ("Drop time of " ,droptime, "hours OK")

        else:
            print ("Invalid Drop time")
        return droptime

    
    def comment(self):
        comment = input("Enter any other information about your items: ")
        return comment
