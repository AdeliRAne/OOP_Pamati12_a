class BankAccount:
    def __init__(self, balance=0):
        # Privātā īpašības konta atlikumsm
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'{amount} Eur noguldīti kontā.')
        else:
            print('Noguldīšanas summa jābūt pozitīvai.')

    def withdraw(self, amount):
        if amount > self.__balance:
            print('Nepietiekami līdzekļi izņemšana.')
        elif amount <=0:
            print('Izņemošanas summa jābūt pozitīvasi.')
        else:
            self.__balance -= amount
            print(f'{amount} Eur izņemti no konta.')
    
account = BankAccount(100)
print('Pašreizējais atlikums:', account.get_balance())
account.deposit(50)
print('Pašreizējais atlikums pēc noguldījuma:', account.get_balance())
account.withdraw(200)
account.withdraw(30)
print('Pašreizējais atlikums pēc izņemšanas: ', account.get_balance())