class Coffee:
    coffeeCupCounter = 0
    def __init__(self, themilk, thesugar, thecoffeemate):
        self.milk = themilk
        self.sugar = thesugar
        self.coffeemate = thecoffeemate
        Coffee.coffeeCupCounter = Coffee.coffeeCupCounter +1
        print(f"You now have your coffee with {self.milk} milk, {self.sugar} sugar {self.coffeemate} coffeemate")

mySugarFreeCoffee = Coffee(2,0,1)
print(mySugarFreeCoffee.sugar)
myMuchSugarCoffee = Coffee(2, 10, 1)
print(myMuchSugarCoffee.sugar)
print(f"we have made {Coffee.coffeeCupCounter} coffee cups so farr!")
print(f"we have made {mySugarFreeCoffee.coffeeCupCounter} coffee cups so farr!")
print(f"we have made {myMuchSugarCoffee.milk} coffee cups so farr!")
print(f"we have made {myMuchSugarCoffee.coffeeCupCounter} coffee cups so farr!")