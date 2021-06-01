class BankOfAJ:
    loggedinCounter = 0
    def __init__(self, theatmpin, theaccountbalance, thename):
        self.atmpin = theatmpin
        self.accountbalance = theaccountbalance
        self.name = thename
        BankOfAJ.loggedinCounter = BankOfAJ.loggedinCounter + 1
    
    def CollectMoney(self, ammounttowithdraw):
        if(ammounttowithdraw > self.accountbalance):
            print("Insufficient Funds oporrrr!")
        else:
            print("Alaye collect your cashh...may you get out.")

    def ChangePin(self, newPin):
        self.atmpin = newPin
        print("You don change your pin may you no forget am oo")
@classmethod
def NoofCustomersLoggedin(cls):
        print(" A total of" + str(cls.loggedinCounter) + "don come collect money.")

f = open("")
#print(f.readline())
password = []
accountB = []
name = []
breaker = []
for x in f:
    breaker = x.split(" ")
    password.append(breaker[0])
    accountB.append(breaker[1])
    name.append(breaker[2])
    break

print('may you put your pin.....')
pasw = input()

if(pasw == password[0]):
    customer = BankOfAJ(password[0], accountB[0], name[0])
else:
    print('sorry your password no correct oo')