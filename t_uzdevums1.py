class BankAccount:
    def __init__(self, balance=0):
        # Privātā īpašības konta atlikumsm
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
account = BankAccount(1000)
print('Pašreizējais atlikums:', account.get_balance())