class Onlinestore:
    def __init__ (self, numberOfitemsbought, totalcost):
        self.numberOfitemsbought = numberOfitemsbought
        self.totalcost = totalcost = totalcost

    def calculator(self):
        while int(self.totalcost) >= 100000:
            print ("You are eligible for a gift for a gift or a discount.")
            if int(self.numberOfitemsbought) < 10:
                totalcostwithdiscount = int(self.totalcost) * 0.01
                print(f"Total cost for less than 10 items is {self.totalcost}, with a 10% discount, you would pay" + " " + str(totalcostwithdiscount))
            else: 
                totalcostwithdiscount = int(self.totalcost) * 0.01
                print(f"Total cost for more than 10 items is {self.totalcost}, with a 10% discount, you would pay" + " "+ str(totalcostwithdiscount) + ". You have a gift.")
            break

        else:
            print (f"The total cost is {self.totalcost}")

Customer1 = Onlinestore(input("Number Of items bought:"), input("Total Cost:"))
Customer1.calculator()
               
               

            