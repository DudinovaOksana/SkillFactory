# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов. Вам необходимо написать программу,
# которая позволит составить список гостей. В класс «Клиент» из задания 16_9_3 добавьте метод, который будет возвращать
# информацию только об имени, фамилии и городе клиента.Затем создайте список, в который будут добавлены все клиенты, и
# выведите его в консоль.

class Customer:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}.{self.city}.Баланс:{self.balance} руб.'

    def get_customers(self):
        return f'{self.name} {self.surname}.{self.city}'

customer1 = Customer("Витя", "Князев", "Москва", 30)
customer2 = Customer("Cлава", "Иванов", "Ярославль", 50)
guest_list = [customer1, customer2]

for guest in guest_list:
    print(guest.get_customers())
