class Orderprice:
    def dropTIme(self, droptime):
        if droptime in range(9, 15):
            print ("Drop time of " ,droptime, "hours OK")
        else:
            print ("Invalid Drop time")
        return droptime

    def expedite(self, expedite):
        if expedite == 1:
            Totaldue = Totaldue * 3
        else:
            

    def perfume(self, perfume):
        if perfume == 1:

        else:
            
    
    def comment(self, comment):
        comment = input("Enter any other information about your items: ")
        return comment
