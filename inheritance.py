class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power
        self.on = False

    def turn_on(self):
        self.on = True
        print("Устройство включено")

    def turn_off(self):
        self.on = False
        print("Устройство выключено")

    def info(self):
        print(f"Бренд: {self.brand}, Модель: {self.model}, Мощность: {self.power}")


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_tank):
        super().__init__(brand, model, power)
        self.water_tank = water_tank

    def make_coffee(self):
        if self.on:
            print("Кофе готов!")
        else:
            print("Включите кофемашину")

    def info(self):
        print(f"Кофемашина: {self.brand} {self.model}, {self.power} Вт, Вода: {self.water_tank} л")


class Blender(Device):
    def __init__(self, brand, model, power, speed):
        super().__init__(brand, model, power)
        self.speed = speed

    def blend(self):
        if self.on:
            print("Блендер измельчает")
        else:
            print("Включите блендер")

    def info(self):
        print(f"Блендер: {self.brand} {self.model}, {self.power} Вт, Скоростей: {self.speed}")


class MeatGrinder(Device):
    def __init__(self, brand, model, power, knife):
        super().__init__(brand, model, power)
        self.knife = knife

    def grind(self):
        if self.on:
            print("Мясорубка перемалывает мясо")
        else:
            print("Включите мясорубку")

    def info(self):
        print(f"Мясорубка: {self.brand} {self.model}, {self.power} Вт, Нож: {self.knife}")


class Ship:
    def __init__(self, name, country, year):
        self.name = name
        self.country = country
        self.year = year
        self.speed = 0

    def start(self):
        print(f"{self.name} отплыл")

    def stop(self):
        self.speed = 0
        print(f"{self.name} остановился")

    def info(self):
        print(f"Корабль: {self.name}, Страна: {self.country}, Год: {self.year}")


class Frigate(Ship):
    def __init__(self, name, country, year, missiles):
        super().__init__(name, country, year)
        self.missiles = missiles

    def fire(self):
        if self.missiles > 0:
            self.missiles -= 1
            print(f"Запущена ракета. Осталось {self.missiles}")
        else:
            print("Нет ракет")

    def info(self):
        print(f"Фрегат: {self.name}, Ракет: {self.missiles}")


class Destroyer(Ship):
    def __init__(self, name, country, year, torpedoes):
        super().__init__(name, country, year)
        self.torpedoes = torpedoes

    def fire_torpedo(self):
        if self.torpedoes > 0:
            self.torpedoes -= 1
            print(f"Торпеда запущена. Осталось {self.torpedoes}")
        else:
            print("Нет торпед")

    def info(self):
        print(f"Эсминец: {self.name}, Торпед: {self.torpedoes}")


class Cruiser(Ship):
    def __init__(self, name, country, year, guns):
        super().__init__(name, country, year)
        self.guns = guns

    def shoot(self):
        print(f"Крейсер стреляет из {self.guns} орудий")

    def info(self):
        print(f"Крейсер: {self.name}, Орудий: {self.guns}")


class Money:
    def __init__(self, valuta, rub, kop):
        self.valuta = valuta
        self.rub = rub
        self.kop = kop
        self.normal()

    def normal(self):
        if self.kop >= 100:
            self.rub = self.rub + self.kop // 100
            self.kop = self.kop % 100
        if self.kop < 0:
            self.rub = self.rub - 1
            self.kop = self.kop + 100

    def set_rub(self, rub):
        self.rub = rub

    def set_kop(self, kop):
        self.kop = kop
        self.normal()

    def set_all(self, rub, kop):
        self.rub = rub
        self.kop = kop
        self.normal()

    def get_rub(self):
        return self.rub

    def get_kop(self):
        return self.kop

    def show(self):
        if self.kop < 10:
            print(f"{self.rub}.0{self.kop} {self.valuta}")
        else:
            print(f"{self.rub}.{self.kop} {self.valuta}")


print("Проверка всех заданий")
print("Задание 1")
a = CoffeeMachine("Bosch", "T30", 1500, 1.5)
a.turn_on()
a.make_coffee()
a.info()

b = Blender("Philips", "HR3652", 800, 5)
b.turn_on()
b.blend()
b.info()

c = MeatGrinder("Zelmer", "987", 500, "нержавейка")
c.turn_on()
c.grind()
c.info()

print("Задание 2")
f = Frigate("Адмирал", "Россия", 2026, 16)
f.start()
f.fire()
f.info()

d = Destroyer("Трамп", "США", 2026, 8)
d.fire_torpedo()
d.info()

cr = Cruiser("Москва", "Россия", 1983, 130)
cr.shoot()
cr.info()

print("Задание 3")
m1 = Money("USD", 10, 50)
m1.show()

m2 = Money("EUR", 5, 150)
m2.show()

m3 = Money("RUB", 0, 99)
m3.show()

m3.set_rub(15)
m3.set_kop(5)
m3.show()

m3.set_all(20, 108)
m3.show()

print(m3.get_rub(), m3.get_kop())