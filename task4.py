# Создаем класс Банковский счет
class BankAccount:
    # Конструктор класса с параметром баланс по умолчанию 0
    def __init__(self, balance=0):
        self.balance = balance  # Устанавливаем начальный баланс
        self.history = []  # Создаем пустой список для хранения истории операций
    
    # Метод для пополнения счета (принимает amount - сумму пополнения)
    def add_money(self, amount):
        if amount > 0:  # Проверяем, что сумма положительная
            self.balance += amount  # Увеличиваем баланс
            self.history.append(f"+{amount}")  # Добавляем запись в историю
        else:
            print("Ошибка: сумма должна быть больше 0")  # Сообщение об ошибке
    
    # Метод для снятия денег (принимает amount - сумму снятия)
    def take_money(self, amount):
        if amount > 0:  # Проверяем, что сумма положительная
            if amount <= self.balance:  # Проверяем, достаточно ли средств
                self.balance -= amount  # Уменьшаем баланс
                self.history.append(f"-{amount}")  # Добавляем запись в историю
            else:
                print("Ошибка: недостаточно средств")  # Сообщение об ошибке
        else:
            print("Ошибка: сумма должна быть больше 0")  # Сообщение об ошибке
    
    # Метод для показа истории операций
    def show_history(self):
        return self.history  # Возвращаем список истории


# Создаем экземпляр класса BankAccount с начальным балансом 
account = BankAccount(900)  
# Пополняем счет 
account.add_money(550)       
# Выводим текущий баланс 
print(f"Баланс: {account.balance}")

# Снимаем со счета
account.take_money(400)      
# Выводим текущий баланс
print(f"Баланс: {account.balance}")

# Пытаемся снять больше, чем есть на счете 
account.take_money(2000)    

# Выводим историю операций
print("История:", account.show_history())
