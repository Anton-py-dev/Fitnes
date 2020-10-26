from datetime import datetime


class ActivityList:
    def __init__(self):
        self.li = []
        self.ldlist = []

    def append(self, act):
        self.li.append(act)
        return

    def last_day(self):
        t = datetime.now()
        t = datetime(t.year, t.month, t.day - 1, t.hour, t.minute)
        self.ldlist.clear()
        for act in self.li:
            if act.s < t:
                break
            self.ldlist.append(act)

    def points_h_to_l_sort(self):  # sort main list
        self.li.sort(key=lambda act: act.points, reverse=True)

    def points_l_to_h_sort(self):
        self.li.sort(key=lambda act: act.points, reverse=False)

    def ccal_h_to_l_sort(self):  # sort main list
        self.li.sort(key=lambda act: act.ccal, reverse=True)

    def ccal_l_to_h_sort(self):
        self.li.sort(key=lambda act: act.ccal, reverse=False)

    def n_to_o_sort(self):
        self.li.sort(key=lambda act: act.s, reverse=True)

    def o_to_n_sort(self):
        self.li.sort(key=lambda act: act.s, reverse=False)

    def print(self):
        for act in self.li:
            print(act.date.strftime("%d %B"), ", ", act.s.strftime("%H:%M"), " - ", act.e.strftime("%H:%M"))
            print("Тривалість: ", act.time)
            try:
                print("Відстань: ", act.d);
            except:
                pass
            print("Калорії: ", act.ccal)
            print("Бали: ", act.points, "\n")
