from datetime import datetime, date, time


class Activity:
    def __init__(self, p):
        self.persone = p  # Привязує активність до особи
        self.points = 0  # бали фізичної активності
        self.ccal = 0  # кількість каллорій спалених в даній активності
        self.date = date.today()
        self.time = time(0, 0, 0, 0)
        self.s = self.e = datetime.now()
        self.note = ""

    def __setPoints(self, points):
        self.points = points

    def set_time(self):
        print("Дата:")
        self.date = date(int(input("Рік: ")), int(input("Місяць: ")), int(input("День: ")))
        print("Початок:")
        self.s = datetime.combine(self.date, time(int(input("Години: ")), int(input("Хвилини: ")), 0, 0))
        print("Кінець:")
        self.e = datetime.combine(self.date, time(int(input("Години: ")), int(input("Хвилини: ")), 0, 0))
        self.time = self.e - self.s
        # self.note = input("Замітка: ")

    def start(self):
        self.s = datetime.now()

    def end(self):
        self.e = datetime.now()
        self.time = self.e - self.s
        # self.note = input("Замітка: ")


class MovingEx(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.setDistance(int(input("Метри:")) / 1000)

    def setDistance(self, d):
        self.distance = d  # Далність задається в кілометрах
        #self.persone.distanceS += self.distance


class Running(MovingEx):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Біг"
        self.multiplier()

    def multiplier(self):
        self.ccal = self.distance * self.persone.weight
        self.points = self.distance * 100
        #self.persone.pointS += self.points
        #self.persone.ccalS += self.ccal


class Walking(MovingEx):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Ходьба"
        self.multiplier()

    def multiplier(self):
        self.ccal = self.distance * self.persone.weight * 0.5
        self.points = self.distance * 50
        #self.persone.pointS += self.points
        #self.persone.ccalS += self.ccal


class Cycling(MovingEx):
    def __init__(self, p):
        super().__init__(p)
        self.speed = 0
        self.name = "Велосипед"
        self.setSpeed(int(input("km/h: ")))
        self.multiplier()

    def setSpeed(self, s):
        self.speed = s

    def multiplier(self):
        if self.speed > 25:
            self.ccal = self.distance / self.speed * self.persone.weight * 12
        elif self.speed > 20:
            self.ccal = self.distance / self.speed * self.persone.weight * 10
        elif self.speed > 15:
            self.ccal = self.distance / self.speed * self.persone.weight * 8
        else:
            self.ccal = self.distance / self.speed * self.persone.weight * 6

        self.points = self.distance * 10
        #self.persone.pointS += self.points
        #self.persone.ccalS += self.ccal
