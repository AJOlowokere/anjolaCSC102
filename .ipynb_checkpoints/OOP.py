class Coffee:

    def __init__(self, themilk, thesugar, thecoffeemate):
        self.milk = themilk
        self.sugar = thesugar
        self.coffeemate = thecoffeemate
        print(f"You now have your coffee with {self.milk} milk, {self.sugar} sugar {self.coffeemate} coffeemate")

mySugarFreeCoffee = Coffee(2,0,1)
myMuchSugarCoffee = Coffee(2, 10, 1)