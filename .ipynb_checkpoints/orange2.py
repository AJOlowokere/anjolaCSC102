class Orange:
     priceOfOranges = 5
     stock = 30
     def __init__(self, quantityToBuy):
        self.quantityToBuy = quantityToBuy

     def OrangeSelling(self):
        while self.quantityToBuy > Orange.stock:
            print(input("We do not have enough oranges, Please select a lesser quantity:"))
            if False:
                continue
            else:
                Orange.stock = Orange.stock - int(self.quantityToBuy)
                print (f"Your amount to pay is {int(self.quantityToBuy) * Orange.priceOfOranges} and we have {Orange.stock} oranges left.")

Buyer1 = Orange(int(input("Please input quantity to buy:")))
Buyer1.OrangeSelling()

