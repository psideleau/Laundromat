class Orderprice:
        
        def totaldue(self,total):
            self.Totaldue = total

        def droptime(self, droptime):
            self.droptime = droptime
                
            if droptime in range(9, 15):
                print ("Drop time of ", droptime, "hours OK")
            else:
                print ("Invalid Drop time")
            
        def expedite(self, expedite):
            if expedite == 1:
                self.estimatedtime = self.droptime +3
                self.Totaldue = self.Totaldue * 2
            else:
                self.estimatedtime = self.droptime + 7
            
        def prefume(self, perfume):
            if perfume == 1:
                self.Totaldue = self.Totaldue + 3
            else:
                self.Totaldue = self.Totaldue
            
        def iron(self, ironing):
            if ironing == 1:
                self.Totaldue = self.Totaldue+3
            else:
                self.Totaldue = self.Totaldue
       
        

        def printTotaldue(self):
            print("Total price = ", self.Totaldue)
            print("Estimated Time = ", self.estimatedtime)
            print("drop time = ", self.droptime)
