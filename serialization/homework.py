"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""
import random

from ruamel import yaml
import constants
import uuid
from typing import List
import json
import pickle


class Car:

    def __init__(self, price: float, mileage: float, car_type=None, producer=None, number=None):
        self.price = price
        self.type = car_type if car_type is not None else random.choice(constants.CARS_TYPES)
        self.producer = producer if producer is not None else random.choice(constants.CARS_PRODUCER)
        self.number = number if number is not None else str(uuid.uuid4())
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

    # def to_json(self):
    #     if isinstance(self, Car):
    #         car_data = {"price": self.price, "car_type": self.type, "producer": self.producer, "number": self.number,
    #                     "mileage": self.mileage}
    #         return car_data
    #
    # def car_from_json(data):
    #     price = data['price']
    #     car_type = data['car_type']
    #     producer = data['producer']
    #     number = data['number']
    #     mileage = data['mileage']
    #     car_load = Car(price=price, car_type=car_type, producer=producer, number=number, mileage=mileage)
    #     return car_load

    def json_dump(self):
        try:
            with open("car.json", "w") as write_file:
                json.dump(self, write_file, default=to_json, indent=4)
        except TypeError as e:
            print(e)

    def json_dumps(self):
        try:
            return json.dumps(self, default=to_json)
        except TypeError as e:
            print(e)

    def pickle_dump(self):
        try:
            with open("car.txt", "wb") as write_file:
                pickle.dump(self, write_file)
        except TypeError as e:
            print(e)

    def pickle_dumps(self):
        try:
            return pickle.dumps(self)
        except TypeError as e:
            print(e)

    def yaml_dump(self):
        try:
            with open("car.yaml", "w") as write_file:
                yaml.dump(self, write_file)
        except TypeError as e:
            print(e)

    def yaml_dumps(self):
        try:
            return yaml.dump(self)
        except TypeError as e:
            print(e)

    @staticmethod
    def json_load():
        try:
            with open("car.json", "r") as read_file:
                data = json.load(read_file, object_hook=car_from_json)
                return data
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def json_loads(read_str):
        try:
            return json.loads(read_str, object_hook=car_from_json)
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def pickle_load():
        try:
            with open("car.txt", "rb") as read_file:
                data = pickle.load(read_file)
                return data
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def pickle_loads(read_str):
        try:
            return pickle.loads(read_str)
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def yaml_load():
        try:
            with open("car.yaml", "r") as read_file:
                data = yaml.load(read_file)
                return data
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def yaml_loads(read_str):
        try:
            return yaml.load(read_str)
        except TypeError as e:
            print(f"ERROR {e}")

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

    # def to_json(self):
    #     if isinstance(self, Car):
    #         garage_data = {"cars": str(self.cars), "owner": str(self.owner)}
    #         return garage_data

    # def garage_from_json(data):
    #     cars = data['cars']
    #     owner = data['owner']
    #     garage_load = Garage(cars=cars, owner=owner)
    #     return garage_load

    def json_dump(self):
        try:
            with open("garage.json", "w") as write_file:
                json.dump(self, write_file, default=to_json, indent=4)
        except TypeError as e:
            print(e)

    def json_dumps(self):
        try:
            return json.dumps(self, default=to_json, indent=4)
        except TypeError as e:
            print(e)

    def pickle_dump(self):
        try:
            with open("garage.txt", "wb") as write_file:
                pickle.dump(self, write_file)
        except TypeError as e:
            print(e)

    def pickle_dumps(self):
        try:
            return pickle.dumps(self)
        except TypeError as e:
            print(e)

    def yaml_dump(self):
        try:
            with open("garage.yaml", "w") as write_file:
                yaml.dump(self, write_file)
        except TypeError as e:
            print(e)

    def yaml_dumps(self):
        try:
            return yaml.dump(self)
        except TypeError as e:
            print(e)

    @staticmethod
    def json_load():
        try:
            with open("garage.json", "r") as read_file:
                data = json.load(read_file, object_hook=garage_from_json)
                return data
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def json_loads(read_str):
        try:
            return json.loads(read_str, object_hook=garage_from_json)
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def pickle_load():
        try:
            with open("garage.txt", "rb") as read_file:
                data = pickle.load(read_file)
                return data
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def pickle_loads(read_str):
        try:
            return pickle.loads(read_str)
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def yaml_load():
        try:
            with open("garage.yaml", "r") as read_file:
                data = yaml.load(read_file)
                return data
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def yaml_loads(read_str):
        try:
            return yaml.load(read_str)
        except TypeError as e:
            print(f"ERROR {e}")

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

    def __init__(self, name: str, garages, reg_id=None):
        self.name = name
        self.garages = garages if garages is not None else []
        self.reg_id = reg_id if reg_id is not None else str(uuid.uuid4())
        pass

    def __eq__(self, other):
        return self.hit_hat() == other.hit_hat()

    def __le__(self, other):
        return self.hit_hat() <= other.hit_hat()

    def __lt__(self, other):
        return self.hit_hat() < other.hit_hat()

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
                print("_" * 30)
                return f"car added to other garage: {self.garages[index]}"
            else:
                return "No free places"

    # def to_json(self):
    #     if isinstance(self, Cesar):
    #         cesar_data = {"name": self.name, "garages": str(self.garages), "reg_id": str(self.reg_id)}
    #         return cesar_data
    #
    # def cesar_from_json(data):
    #     name = data['name']
    #     garages = data['garages']
    #     reg_id = data['reg_id']
    #     cesar_load = Cesar(name=name, garages=garages, reg_id=reg_id)
    #     return cesar_load

    def json_dump(self):
        try:
            with open("Cesar.json", "w") as write_file:
                json.dump(self, write_file, default=to_json, indent=4)
        except TypeError as e:
            print(e)

    def json_dumps(self):
        try:
            return json.dumps(self, default=to_json, indent=4)
        except TypeError as e:
            print(e)

    def pickle_dump(self):
        try:
            with open("Cesar.txt", "wb") as write_file:
                pickle.dump(self, write_file)
        except TypeError as e:
            print(e)

    def pickle_dumps(self):
        try:
            return pickle.dumps(self)
        except TypeError as e:
            print(e)

    def yaml_dump(self):
        try:
            with open("Cesar.yaml", "w") as write_file:
                yaml.dump(self, write_file)
        except TypeError as e:
            print(e)

    def yaml_dumps(self):
        try:
            return yaml.dump(self)
        except TypeError as e:
            print(e)

    @staticmethod
    def json_load():
        try:
            with open("Cesar.json", "r") as read_file:
                data = json.load(read_file, object_hook=cesar_from_json)
                return data
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def json_loads(read_str):
        try:
            return json.loads(read_str, object_hook=cesar_from_json)
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def pickle_load():
        try:
            with open("Cesar.txt", "rb") as read_file:
                data = pickle.load(read_file)
                return data
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def pickle_loads(read_str):
        try:
            return pickle.loads(read_str)
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def yaml_load():
        try:
            with open("Cesar.yaml", "r") as read_file:
                data = yaml.load(read_file)
                return data
        except TypeError as e:
            print(f"ERROR {e}")

    @staticmethod
    def yaml_loads(read_str):
        try:
            return yaml.load(read_str)
        except TypeError as e:
            print(f"ERROR {e}")

    def __str__(self):
        return f" \n Name: {self.name}\n All Garages: {self.garages}\n Owner reg_id: {self.reg_id}"

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


def to_json(self):
    if isinstance(self, Car):
        car_data = {"price": self.price, "car_type": self.type, "producer": self.producer, "number": self.number,
                    "mileage": self.mileage}
        return car_data

    if isinstance(self, Garage):
        garage_data = {"cars": str(self.cars), "owner": str(self.owner)}
        return garage_data

    if isinstance(self, Cesar):
        cesar_data = {"name": self.name, "garages": str(self.garages), "reg_id": str(self.reg_id)}
        return cesar_data


def car_from_json(data):
    price = data['price']
    car_type = data['car_type']
    producer = data['producer']
    number = data['number']
    mileage = data['mileage']
    car_load = Car(price=price, car_type=car_type, producer=producer, number=number, mileage=mileage)
    return car_load


def garage_from_json(data):
    cars = data['cars']
    owner = data['owner']
    garage_load = Garage(cars=cars, owner=owner)
    return garage_load


def cesar_from_json(data):
    name = data['name']
    garages = data['garages']
    reg_id = data['reg_id']
    cesar_load = Cesar(name=name, garages=garages, reg_id=reg_id)
    return cesar_load


if __name__ == "__main__":
    car_1 = Car(200, mileage=11000)
    car_2 = Car(300, 11000)
    car_3 = Car(400, 11000)

    car_list = [car_1, car_2, car_3]

    garage_1 = Garage(cars=car_list, owner='c5d8abc6-2711-408c-94c4-62a82aa8bd22')
    garage_2 = Garage([car_1, car_2, car_3])

    Cesar_1 = Cesar("Maximus", [garage_1, garage_2])
    Cesar_2 = Cesar("Ulius", [garage_2])

###  JSON

    # car_1.json_dump()
    # print(car_2.json_load())
    #
    # garage_1.json_dump()
    # print(garage_2.json_load())
    #
    # Cesar_1.json_dump()
    # print(Cesar_2.json_load())
    #
    # print(type(car_1.json_dumps()), car_1.json_dumps())
    # print(car_1.json_loads(car_1.json_dumps()))
    #
    # print(type(garage_1.json_dumps()), garage_1.json_dumps())
    # print(garage_2.json_loads(garage_1.json_dumps()))
    #
    # print(type(Cesar_1.json_dumps()), Cesar_1.json_dumps())
    # print(Cesar_2.json_loads(Cesar_1.json_dumps()))
    #

### PICKLE

    # car_1.pickle_dump()
    # print(car_2.pickle_load())
    #
    # garage_1.pickle_dump()
    # print(garage_2.pickle_load())
    #
    # Cesar_1.pickle_dump()
    # print(Cesar_2.pickle_load())

    # print(type(car_1.pickle_dumps()), car_1.pickle_dumps())
    # print(car_1.pickle_loads(car_1.pickle_dumps()))
    #
    # print(type(garage_1.pickle_dumps()), garage_1.pickle_dumps())
    # print(garage_2.pickle_loads(garage_1.pickle_dumps()))
    #
    # print(type(Cesar_1.pickle_dumps()), Cesar_1.pickle_dumps())
    # print(Cesar_2.pickle_loads(Cesar_1.pickle_dumps()))

### YAML

    # car_1.yaml_dump()
    # print(car_2.yaml_load())
    #
    # garage_1.yaml_dump()
    # print(garage_2.yaml_load())
    #
    # Cesar_1.yaml_dump()
    # print(Cesar_2.yaml_load())

    # print(type(car_1.yaml_dumps()), car_1.yaml_dumps())
    # print(car_1.yaml_loads(car_1.yaml_dumps()))
    #
    # print(type(garage_1.yaml_dumps()), garage_1.yaml_dumps())
    # print(garage_2.yaml_loads(garage_1.yaml_dumps()))
    #
    # print(type(Cesar_1.yaml_dumps()), Cesar_1.yaml_dumps())
    # print(Cesar_2.yaml_loads(Cesar_1.yaml_dumps()))
