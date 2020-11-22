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

    def start(self):
        self.s = datetime.now()

    def end(self):
        self.e = datetime.now()
        self.time = self.e - self.s

    def multiplier(self):
        pass


class MovingEx(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.setDistance(int(input("Метри:")) / 1000)

    def setDistance(self, d):
        self.distance = d  # Далність задається в кілометрах


class HathaYoga(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Хатха-йога"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 273
        self.points = self.time.seconds / 60 * 3


class Bowling(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Боулінг"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 270
        self.points = self.time.seconds / 60 * 3


class AquaAerobics(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Аквааеробіка"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 240
        self.points = self.time.seconds / 60 * 3


class Bodyflex(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Бодіфлекс"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 260
        self.points = self.time.seconds / 60 * 3


class Gymnastics(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Гімнастика"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 350
        self.points = self.time.seconds / 60 * 5


class JumpingRope(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Скакалка"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 680
        self.points = self.time.seconds / 60 * 8


class Hoop(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Обруч"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 375
        self.points = self.time.seconds / 60 * 3


class Pilates(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Пілатес"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 150
        self.points = self.time.seconds / 60 * 4


class Callanetics(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Калланетика"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 310
        self.points = self.time.seconds / 60 * 3


class ModernDances(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Сучасні танці"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 265
        self.points = self.time.seconds / 60 * 4


class Ballet(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Балет"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 750
        self.points = self.time.seconds / 60 * 7


class DiscoDancing(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Танці диско"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 400
        self.points = self.time.seconds / 60 * 7


class FigureSkating(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Фігурне Катання"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 300
        self.points = self.time.seconds / 60 * 7


class Skiing(MovingEx):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Ходьба на лижах"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 400
        self.points = self.time.seconds / 60 * 7


class DownhillSkiing(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Швидкісний спуск на лижах"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 270
        self.points = self.time.seconds / 60 * 2


class WaterPolo(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Водне поло"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 600
        self.points = self.time.seconds / 60 * 5


class Swimming(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Плавання"
        self.setSpeed(int(input("km/h: ")))

    def setSpeed(self, s):
        self.speed = s

    def multiplier(self):
        if self.speed >= 3:
            self.ccal = self.time.seconds / 60 / 60 * 500
        elif self.speed >= 2.4:
            self.ccal = self.time.seconds / 60 / 60 * 460
        elif self.speed >= 1.5:
            self.ccal = self.time.seconds / 60 / 60 * 320
        else:
            self.ccal = self.time.seconds / 60 / 60 * 210
        self.points = self.time.seconds / 60 * 4


class Rowing(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Академічна гребля"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 210
        self.points = self.time.seconds / 60 * 3


class WaterSkis(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Водні лижі"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 355
        self.points = self.time.seconds / 60 * 5


class TaiBo(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Тай-бо"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 800
        self.points = self.time.seconds / 60 * 7


class Badminton(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Бадмінтон"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 405
        self.points = self.time.seconds / 60 * 4


class Golf(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Гольф"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 / 60 * 250
        self.points = self.time.seconds / 60 * 7


class Aerobic(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Аеробіка"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 * 8
        self.points = self.time.seconds / 60 * 4


class CrossFit(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Кросфіт"

    def multiplier(self):
        self.ccal = self.time.seconds / 60 * 15
        self.points = self.time.seconds / 60


class Running(MovingEx):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Біг"

    def multiplier(self):
        self.ccal = self.distance * self.persone.weightDynamic[-1][0]
        self.points = self.distance * 100


class Walking(MovingEx):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Ходьба"

    def multiplier(self):
        self.ccal = self.distance * self.persone.weightDynamic[-1][0] * 0.5
        self.points = self.distance * 50


class Cycling(MovingEx):
    def __init__(self, p):
        super().__init__(p)
        self.speed = 0
        self.name = "Велосипед"
        self.setSpeed(int(input("km/h: ")))

    def setSpeed(self, s):
        self.speed = s

    def multiplier(self):
        if self.speed > 25:
            self.ccal = self.distance / self.speed * self.persone.weightDynamic[-1][0] * 12
        elif self.speed > 20:
            self.ccal = self.distance / self.speed * self.persone.weightDynamic[-1][0] * 10
        elif self.speed > 15:
            self.ccal = self.distance / self.speed * self.persone.weightDynamic[-1][0] * 8
        else:
            self.ccal = self.distance / self.speed * self.persone.weightDynamic[-1][0] * 6

        self.points = self.distance * 10