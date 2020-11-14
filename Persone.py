import datetime
#from datetime import date
from Fitnes.ActivityList import ActivityList
from Fitnes.Activity import CrossFit, Cycling, Aerobic, Running, Walking

class Persone:
    def __init__(self, name, weight):
        self.name = name
        self.weightDynamic = [[weight, datetime.date.today()]]
        self.activityList = ActivityList()
        self.distanceS = 0
        self.pointS = 0
        self.ccalS = 0

    def addInfo(self):
        self.sex = int(input("Виберіть стать:\n 1.Чоловіча\n 2.Жіноча\n ->"))
        self.height = int(input("Зріст: "))
        self.birthday = datetime.date(int(input("Рік: ")), int(input("Місяць: ")), int(input("День: ")))

    def setWeight(self, weight):
        pair = [weight, datetime.date.today()]
        self.weightDynamic.append(pair)

    def lastMonthWeightDynamic(self):
        li = []
        for i in reversed(self.weightDynamic):
            m = datetime.date(datetime.date.today().year, datetime.date.today().month - 1, datetime.date.today().day)
            if i[1] < m:
                return li
            li.append(i)
        return li

    def lastYearWeightDynamic(self):
        li = []
        for i in reversed(self.weightDynamic):
            m = datetime.date(datetime.date.today().year - 1, datetime.date.today().month, datetime.date.today().day)
            if i[1] < m:
                return li
            li.append(i)
        return li

    def calculate_points(self, start, end): # start - end період, під час якого будуть рахуватись points
        points = 0
        for act in self.activityList.li:
            if end > act.date > start:
                points += act.points
        return points

    def calculate_ccal(self, start, end):
        ccal = 0
        for act in self.activityList.li:
            if end > act.date > start:
                ccal += act.ccal
        return ccal

    def calculate_distance(self, start, end):
        d = 0
        for act in self.activityList.li:
            if end > act.date > start:
                d += act.distance
        return d

    def calculate_last_day(self):
        self.activityList.last_day()
        self.distanceS = 0
        self.pointS = 0
        self.ccalS = 0
        for act in self.activityList.ldlist:
            self.pointS += act.points
            self.ccalS += act.ccal
            try:
                self.distanceS += act.distance
            except:
                pass
        return [self.pointS, self.ccalS, self.distanceS]

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