class InvalidWithdrawal(Exception):
    def __init__(self,balance,amonut):
        super().__init__(f"account does not have ${amonut}")
        self.balance = balance
        self.amount = amonut

    def overage(self):
        return self.amount-self.balance

class Bank:
    def __init__(self,balance,amonut):
        self.balance = balance
        self.amount = amonut
    def withdrawal(self):
        if amount > balance :
            raise InvalidWithdrawal(self.balance,self.amount)
        else:
            return self.balance- self.amount



if __name__ == '__main__':
    amount = 5000
    balance = 200
    try:
        bank = Bank(balance, amount)
        bank.withdrawal()
    except InvalidWithdrawal as e:
        print("I'm sorry, but your withdrawal is "
               "more than your balance by "
               f"${e.overage()}")
        print(e.args)



