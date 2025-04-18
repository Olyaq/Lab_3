class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.history = []
    
    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"+{amount}")
        else:
            print("Ошибка: сумма должна быть больше 0")
    
    def take_money(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.history.append(f"-{amount}")
            else:
                print("Ошибка: недостаточно средств")
        else:
            print("Ошибка: сумма должна быть больше 0")
    
    def show_history(self):
        return self.history


account = BankAccount(900)  
account.add_money(550)       
print(f"Баланс: {account.balance}")

account.take_money(400)      
print(f"Баланс: {account.balance}")

account.take_money(2000)    

print("История:", account.show_history())
