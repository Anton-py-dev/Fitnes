from datetime import datetime, date, time

sec_to_min = 60


class Activity:
    def __init__(self, p):
        self._person = p  # Привязує активність до особи
        self._points = 0  # бали фізичної активності
        self._ccal = 0  # кількість каллорій спалених в даній активності
        self.date = date.today()
        self.time = time(0, 0, 0, 0)
        self.start = self.end = datetime.now()
        self.note = ""
        self.icon = "icons/temp.png"

    def get_points(self):
        return self._points

    def get_ccal(self):
        return self._ccal

    def start(self):
        self.start = datetime.now()

    def end(self):
        self.end = datetime.now()
        self.time = self.end - self.start

    def multiplier(self):
        pass


class MovingEx(Activity):
    def __init__(self, p):
        super().__init__(p)
        self._distance = 0

    def setDistance(self, d):
        self._distance = d  # Далність задається в кілометрах

    def get_distance(self):
        return self._distance


class HathaYoga(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.icon = "icons/yoga.png"
        self.name = "Хатха-йога"

    def multiplier(self):
        coefficient_ccal = 273
        coefficient_poins = 3
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class Bowling(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Боулінг"
        self.icon = "icons/bowling.png"

    def multiplier(self):
        coefficient_ccal = 270
        coefficient_poins = 3
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class AquaAerobics(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Аквааеробіка"

    def multiplier(self):
        coefficient_ccal = 240
        coefficient_poins = 3
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class Bodyflex(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Бодіфлекс"

    def multiplier(self):
        coefficient_ccal = 260
        coefficient_poins = 3
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class Gymnastics(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Гімнастика"

    def multiplier(self):
        coefficient_ccal = 350
        coefficient_poins = 5
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class JumpingRope(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Скакалка"

    def multiplier(self):
        coefficient_ccal = 680
        coefficient_poins = 8
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class Hoop(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Обруч"

    def multiplier(self):
        coefficient_ccal = 375
        coefficient_poins = 3
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class Pilates(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Пілатес"

    def multiplier(self):
        coefficient_ccal = 150
        coefficient_poins = 4
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class Callanetics(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Калланетика"

    def multiplier(self):
        coefficient_ccal = 310
        coefficient_poins = 3
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class ModernDances(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Сучасні танці"

    def multiplier(self):
        coefficient_ccal = 265
        coefficient_poins = 4
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class Ballet(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Балет"

    def multiplier(self):
        coefficient_ccal = 750
        coefficient_poins = 7
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class DiscoDancing(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Танці диско"

    def multiplier(self):
        coefficient_ccal = 400
        coefficient_poins = 7
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class FigureSkating(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Фігурне Катання"

    def multiplier(self):
        coefficient_ccal = 300
        coefficient_poins = 7
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class Skiing(MovingEx):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Ходьба на лижах"

    def multiplier(self):
        coefficient_ccal = 400
        coefficient_poins = 7
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class DownhillSkiing(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Швидкісний спуск на лижах"

    def multiplier(self):
        coefficient_ccal = 270
        coefficient_poins = 2
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class WaterPolo(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Водне поло"

    def multiplier(self):
        coefficient_ccal = 600
        coefficient_poins = 5
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class Swimming(Activity):
    def __init__(self, p):
        super().__init__(p)
        self._speed = 0
        self.name = "Плавання"


    def setSpeed(self, s):
        self._speed = s

    def multiplier(self):
        coefficient_poins = 4
        if self._speed >= 3:
            self._ccal = self.time.seconds / sec_to_min / sec_to_min * 500
        elif self._speed >= 2.4:
            self._ccal = self.time.seconds / sec_to_min / sec_to_min * 460
        elif self._speed >= 1.5:
            self._ccal = self.time.seconds / sec_to_min / sec_to_min * 320
        else:
            self._ccal = self.time.seconds / sec_to_min / sec_to_min * 210
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class Rowing(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Академічна гребля"

    def multiplier(self):
        coefficient_ccal = 210
        coefficient_poins = 3
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class WaterSkis(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Водні лижі"

    def multiplier(self):
        coefficient_ccal = 355
        coefficient_poins = 5
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class TaiBo(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Тай-бо"

    def multiplier(self):
        coefficient_ccal = 800
        coefficient_poins = 7
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class Badminton(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Бадмінтон"

    def multiplier(self):
        coefficient_ccal = 405
        coefficient_poins = 4
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class Golf(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Гольф"

    def multiplier(self):
        coefficient_ccal = 250
        coefficient_poins = 7
        self._ccal = self.time.seconds / sec_to_min / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class Aerobic(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Аеробіка"

    def multiplier(self):
        coefficient_ccal = 8
        coefficient_poins = 4
        self._ccal = self.time.seconds / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / sec_to_min * coefficient_poins


class CrossFit(Activity):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Кросфіт"

    def multiplier(self):
        coefficient_ccal = 15
        coefficient_poins = 1
        self._ccal = self.time.seconds / sec_to_min * coefficient_ccal
        self._points = self.time.seconds / 60 * coefficient_poins


class Running(MovingEx):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Біг"

    def multiplier(self):
        coefficient_ccal = 1
        coefficient_poins = 100
        self._ccal = self._distance * int(self._person.get_weightDynamic()[-1][0]) * coefficient_ccal / 1000
        self._points = self._distance * coefficient_poins / 1000


class Walking(MovingEx):
    def __init__(self, p):
        super().__init__(p)
        self.name = "Ходьба"

    def multiplier(self):
        coefficient_ccal = 0.5
        coefficient_poins = 50
        self._ccal = self._distance * int(self._person.get_weightDynamic()[-1][0]) * coefficient_ccal / 1000
        self._points = self._distance * coefficient_poins / 1000


class Cycling(MovingEx):
    def __init__(self, p):
        super().__init__(p)
        self._speed = 0
        self.name = "Велосипед"

    def setSpeed(self, s):
        self._speed = s

    def multiplier(self):
        if self._speed > 25:
            self._ccal = self._distance * self._speed * int(self._person.get_weightDynamic()[-1][0]) * 12 / 100000
        elif self._speed > 20:
            self._ccal = self._distance * self._speed * int(self._person.get_weightDynamic()[-1][0]) * 10 / 100000
        elif self._speed > 15:
            self._ccal = self._distance * self._speed * int(self._person.get_weightDynamic()[-1][0]) * 8 / 100000
        else:
            self._ccal = self._distance * self._speed * int(self._person.get_weightDynamic()[-1][0]) * 6 / 100000

        self._points = self._distance * 10 / 100
