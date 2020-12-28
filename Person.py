import datetime
from PyQt5.QtCore import QDate
# from datetime import date
from Fitnes.ActivityList import ActivityList
from Fitnes.Activity import CrossFit, Cycling, Aerobic, Running, Walking


class Person:
    def __init__(self, name, weight):
        self.birthday = QDate(2000, 1, 1)
        self.height = 0
        self.sex = "Чоловік"
        self._name = name
        self._weightDynamic = [[weight, datetime.date.today()]]
        self.activityList = ActivityList()
        self._distanceS = 0
        self._pointS = 0
        self._ccalS = 0
        self._pointGoal = 1000
        self._ccalGoal = 1000
        self._distanceGoal = 1000

    def set_goals(self, points, ccal, distance):
        self._pointGoal = points
        self._ccalGoal = ccal
        self._distanceGoal = distance

    def set_name(self, name):
        self._name = name

    def get_pointGoal(self):
        return self._pointGoal

    def get_ccalGoal(self):
        return self._ccalGoal

    def get_distanceGoal(self):
        return self._distanceGoal

    def get_name(self):
        return self._name

    def get_distanceS(self):
        return self._distanceS

    def get_pointS(self):
        return self._pointS

    def get_ccalS(self):
        return self._ccalS

    def get_weightDynamic(self):
        return self._weightDynamic

    def get_weight(self):
        return self._weightDynamic[-1][0]

    def get_activityList(self):
        return self.activityList.li

    def setWeight(self, weight):
        pair = [weight, datetime.date.today()]
        self._weightDynamic.append(pair)

    def lastMonthWeightDynamic(self):
        li = []
        for i in reversed(self._weightDynamic):
            m = datetime.date(datetime.date.today().year, datetime.date.today().month - 1, datetime.date.today().day)
            if i[1] < m:
                return li
            li.append(i)
        return li

    def lastYearWeightDynamic(self):
        li = []
        for i in reversed(self._weightDynamic):
            m = datetime.date(datetime.date.today().year - 1, datetime.date.today().month, datetime.date.today().day)
            if i[1] < m:
                return li
            li.append(i)
        return li

    def calculate_points(self, start, end):  # start - end період, під час якого будуть рахуватись points
        points = 0
        for act in self.activityList.li:
            if end > act.date > start:
                points += act.get_points()
        return points

    def calculate_ccal(self, start, end):
        ccal = 0
        for act in self.activityList.li:
            if end > act.date > start:
                ccal += act.get_ccal()
        return ccal

    def calculate_distance(self, start, end):
        d = 0
        for act in self.activityList.li:
            if end > act.date > start:
                d += act.get_distance()
        return d

    def calculate_last_day(self):
        self.activityList.last_day()
        self._distanceS = 0
        self._pointS = 0
        self._ccalS = 0
        for act in self.activityList.lastDayList:
            self._pointS += act.get_points()
            self._ccalS += int(act.get_ccal())
            try:
                self._distanceS += act.get_distance()
            except:
                pass
        return [self._pointS, self._ccalS, self._distanceS]

    def addActivity(self):
        print("1.Біг\n2.Прогулянка\n3.Велосипед")
        print("4.Аеробіка\n5.Кросфіт")
        ans = int(input())
        if ans == 1:
            newActivity = Running(self)
        elif ans == 2:
            newActivity = Walking(self)
        elif ans == 3:
            newActivity = Cycling(self)
        elif ans == 4:
            newActivity = Aerobic(self)
        elif ans == 5:
            newActivity = CrossFit(self)
        newActivity.set_time()
        newActivity.multiplier()
        self.activityList.append(newActivity)
        self.calculate_last_day()
