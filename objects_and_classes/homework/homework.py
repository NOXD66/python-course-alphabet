"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""
import random
import constants
import uuid
from typing import List


class Car:

    def __init__(self, price: float, mileage: float):
        self.price = price
        self.type = random.choice(constants.CARS_TYPES)
        self.producer = random.choice(constants.CARS_PRODUCER)
        self.number = str(uuid.uuid4())
        self.mileage = mileage
        pass

    def __eq__(self, other):
        return self.price == other.price

    def __le__(self, other):
        return self.price <= other.price

    def __lt__(self, other):
        return self.price < other.price

    def number_replacement(self):
        self.number = str(uuid.uuid4())
        return self.number

    # all info about car
    def __str__(self):
        # print(self)
        return f" Price    : {self.price}\n Type     : {self.type}\n Producer : {self.producer}\n Number   : {self.number}\n Mileage  : {self.mileage}"

    """
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    __При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID
    """

    pass


class Garage:
    cars: List[Car]

    def __init__(self, cars=None, owner=None):
        self.town = random.choice(constants.TOWNS)
        self.cars = cars if cars is not None else []
        self.places = random.randint(3, 4)
        self.owner = uuid.UUID(str(owner)) if owner is not None else None
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.places < len(self.cars):
            res = self.cars[self.places]
            self.places += 1
            return res
        else:
            self.places = 0
            raise StopIteration

    def add(self, Car):
        if len(self.cars) < self.places:
            self.cars.append(Car)
            print("car added successfully")
        else:

            raise Exception("No free places!")

    def remove(self, Car):
        if Car in self.cars:
            self.cars.remove(Car)
        else:
            print("Error Car not in Garage")

    def hit_hat(self):
        cars_price = [self.cars[x].price for x in range(len(self.cars))]
        return sum(cars_price)

    def __str__(self):
        return f" \n City: {self.town}\n Cars in Garage: {self.cars}\n Places: {self.places} \n Owner: {self.owner}"

    """
    town - одне з перечислених значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі
    """
    pass


class Cesar:
    garages: List[Garage]

    def __init__(self, name: str, garages, register_id=None):
        self.name = name
        self.garages = garages if garages is not None else []
        self.register_id = register_id if register_id is not None else str(uuid.uuid4())
        pass

    def garages_count(self):
        return len(self.garages)

    def hit_hat(self):
        garage_cars_price = [self.garages[x].hit_hat() for x in range(len(self.garages))]
        return sum(garage_cars_price)

    def cars_count(self):
        # count_of_cars = len(self.garages[1].cars)
        count_of_cars = sum([len(self.garages[x].cars) for x in range(len(self.garages))])
        return count_of_cars

    def add_car(self, value: Garage, add_car: Car):
        free_places = [self.garages[x].places - len(self.garages[x].cars) for x in range(len(self.garages))]
        try:
            value.add(add_car)
        except Exception:
            if max(free_places):
                index = free_places.index(max(free_places))
                self.garages[index].add(add_car)
                print("_____________________________")
                return f"car added to other garage: {self.garages[index]}"
            else:
                return "No free places"

    def __str__(self):
        return f" \n Name: {self.name}\n All Garages: {self.garages}\n Owner reg_id: {self.register_id}"

    """
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    +hit_hat() - повертає ціну всіх його автомобілів.
    + garages_count() - вертає кількість гаріжів.
    + сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
    """
    pass


if __name__ == "__main__":
    car_1 = Car(200, 11000)
    car_2 = Car(300, 11000)
    car_3 = Car(400, 11000)
    # print(car_2)
    #print(car_2.number_replacement())
    # print(car_2)
    car_list = [car_1, car_2, car_3]

    garage_1 = Garage(cars=car_list, owner='c5d8abc6-2711-408c-94c4-62a82aa8bd22')
    garage_2 = Garage([car_1, car_2, car_3])

    # print(garage_1.hit_hat())
    # print("___________________________")
    Cesar_1 = Cesar("Maximus", [garage_1, garage_2])
    # print(Cesar_1)
    # print(Cesar_1.garages_count())
    # print(Cesar_1.hit_hat())
    # print(Cesar_1.cars_count())

    print(garage_1.cars)
    print(garage_2.cars)
    print("_________________")
    print(Cesar_1.cars_count())
    print(Cesar_1.add_car(garage_2, car_2))
    print(Cesar_1.cars_count())
    print("_________________")

    print(garage_1.cars)
    print(garage_2.cars)
