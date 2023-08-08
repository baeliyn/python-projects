from abc import ABC, abstractmethod

class Bank(ABC):

    def basicinfo():
        print("This is a generic bank")
        return "Generic bank: 0"

    @abstractmethod
    def withdraw():
        pass

class Swiss(Bank):


    def __init__(self):
        self.bal = 1000

    def basicinfo(self):
        print("This is the Japanese Swiss Bank")
        return "Swiss Bank: " + str(self.bal)

    def withdraw(self, amount):
        if amount > self.bal:
            print("Insufficient funds")
            return self.bal
        else:
            self.bal = self.bal - amount
            print("Withdrawn amount: " + str(amount))
            print("New MeraBalance: " + str(self.bal))
            return self.bal


def main():
    assert issubclass(Bank, ABC)
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()