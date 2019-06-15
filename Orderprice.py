class Orderprice:
    def Totaldue(self, Total):
        Total
        
    def dropTIme(self, droptime):
        if droptime in range(9, 15):
            print ("Drop time of " ,droptime, "hours OK")
        else:
            print ("Invalid Drop time")
        return droptime

    def expedite(self, expedite):
        if expedite == 1:
            estimatedtime = droptime + 3
            Total = Total * 2
        else:
            estimatedtime = droptime + 7
        return estimatedtime, Total

    def perfume(self, perfume):
        if perfume == 1:
            Total = Total + 3
        else:
            Total = Total

    def ironing(self, ironing):
        if ironing == 1:

        else
    
    def comment(self, comment):
        comment = input("Enter any other information about your items: ")
        return comment
