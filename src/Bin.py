class Outcome:
    def __init__(self):
        self.outcomelist = []
        for b in range(37):
            # if b > 0:
            #     c = (str(b-1) +" to "+ str(b))
            #     self.outcomelist.append(str(c))
            # if b > 1
            self.outcomelist.append(b)
        self.outcomelist.append("00")
        self.outcomelist.extend(["1 to 2 row 36","1 to 2 row 35","1 to 2 row 34", "Odd", "Even", "Black", "Red", "1 to 12", "13 to 24", "25 to 36","1 to 18", "19 to 36"])

        #dict_outcome = {}
        

    def printoutcomes(self):
        print("These are your possible bets")
        print(self.outcomelist.index(4))
        for a, item in enumerate(self.outcomelist):
            print(a, item)

    def findoutcome(self, num):
        for a, item in enumerate(self.outcomelist):
            if a == num:
                return a, item
#class Bin:



b = Outcome()

#b.printoutcomes()
