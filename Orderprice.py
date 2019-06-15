class orderprice:
    class Orderprice:
    def dropTIme(self, droptime):
        if droptime in range(9, 15):
            print ("Drop time of " ,droptime, "hours OK")
        else:
            print ("Invalid Drop time")
        return droptime

    
    def comment(self):
        comment = input("Enter any other information about your items: ")
        return comment
