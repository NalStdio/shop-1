import os
Manager = [
    {'name': 'Oleg', 'position': "senior"},
    {'name': 'Lev', 'position': "junior"},
    {'name': 'Ilya', 'position': "middle"}
]
Customer = [
    {'name': 'Andrey'},
    {'name': 'Dima'},
    {'name': 'Misha'}
]
Televisor = [
    {'model': 'dexp', 'price': 15000, 'quality': 8},
    {'model': 'sony', 'price': 35000, 'quality': 15},
    {'model': 'xiaomi', 'price': 36000, 'quality': 13},
]

items = list()
people = list()
customer = list()


def create_tele_list(app_items):
    global items
    items = app_items


def create_item(model, price, quantity):
    global items
    items.append({'model': model, 'price': price, 'quality': quantity})


def read_item(model):
    global items
    myitems = list(filter(lambda x: x['model'] == model, items))
    if myitems:
        return myitems[0]




def read_items():
    global items
    return [item for item in items]

def read_names():
    global items
    return [item for item in items[0]]


# Добавить список менеджеров
def create_Manager_list(app_items):
    global people
    people = app_items

# Добавить список покупателей
def create_Customer_list(app_items):
    global customer
    customer = app_items


# Вывести список покупателей
def customer_list():
    global customer
    return [item for item in customer]


# Вывести список покупателей
def meneger_list():
    global people
    return [item for item in people]


# Функция, которая будет убирать телефизор, который купили
def buy_televisor(model):
    global items
    idxs_items = list(
        filter(lambda i_x: i_x[1]['model'] == model, enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]

def choice_name(choice):
    new_model = input("Введите модель телевизора: ")
    buyer.find(new_model)
    if read_item(new_model):
        ans = input("Хотите включить устройство? (Да/Нет): ")
        if ans == "Да":
            tech.turn_on()
        else:
            pass
        ans = input("Хотите его преобрести? (Да/Нет): ")
        if ans == "Да":
            buyer.buy("dexp")
        else:
            print("Хорошо, может быть рассмотрите другую модель")

#Класс Техника
class Technik:
    state = False

    def turn_on(self):
        if self.state == False:
            print("Включено!")
            self.state = True
        else:
            print("Устройство уже включено.")

    def turn_off(self):
        if self.state == True:
            print("Выключено!")
            self.state = True
        else:
            print("Устройство ещё не включено.")

    pass

#Класс ТВ (Дочерний от Техника)
class TV(Technik):
    pass

#Класс Ноутбук (Дочерний от Техника)
class Laptop(Technik):
    pass

#Класс Монитор (Дочерний от Техника)
class Monitor(Technik):
    pass

#Класс Микроволновка (Дочерний от Техника)
class Microwave(Technik):
    pass

#Класс Принтер (Дочерний от Техника)
class Printer(Technik):
    pass


#Класс Работник
class Worker:
    pass

#Класс Кассир (Дочерний от Работника)
class Cashier(Worker):
    pass

#Класс Кассир (Дочерний от Работника)
class Manager(Worker):
    pass

# Класс покупателя
class cust_buy:

    def __init__(self, name):
        self.name = name

    # Найти необходимый телевизор
    def find(self, model):
        self.model = model
        if read_item(model):
            print(self.name + ", у нас как раз есть такая модель в наличии!")
            return True
        else:
            print(self.name + ", к сожалению в наличии этой модели нет. Обратите внимание на другие артикулы.")

    # купить телевизор
    def buy(self, model):
        self.model = model
        if read_item(model):
            print(self.name + " ,поздравляю с покупкой!")
            buy_televisor(model)
        else:
            print("Таких телевизоров в нашем магазине нет.")



create_tele_list(Televisor)
create_Manager_list(Manager)
create_Customer_list(Customer)
print(read_names())


name = input("Введите ваше имя: ")
buyer = cust_buy(name)
tech = TV()
while True:
    choice = str(input("Вы можете выбрать модель телевизора, который хотите купить, либо посмотреть список доступных телевизоров(1/2) или напишите exit, чтобы выйти: "))
    if choice == '1':
        choice_name(choice)
    elif choice == '2':
        print("Список доступных телевизоров", read_items())
    elif choice == 'exit':
        break
    else:
        print("К сожалению я не понял вашего запроса.")
print("Ждём вас вновь :)")

