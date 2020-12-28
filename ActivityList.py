from datetime import datetime


class ActivityList:
    def __init__(self):
        self.li = []
        self.lastDayList = []

    def append(self, act):
        self.li.append(act)
        return

    def last_day(self):
        t = datetime.now()
        t = datetime(t.year, t.month, t.day - 1, t.hour, t.minute)
        self.lastDayList.clear()
        self.new_to_old_sort()
        for act in self.li:
            if act.start < t:
                break
            self.lastDayList.append(act)

    def points_h_to_l_sort(self):  # sort main list
        self.li.sort(key=lambda act: act.get_points(), reverse=True)

    def points_l_to_h_sort(self):
        self.li.sort(key=lambda act: act.get_points(), reverse=False)

    def ccal_h_to_l_sort(self):  # sort main list
        self.li.sort(key=lambda act: act.get_ccal(), reverse=True)

    def ccal_l_to_h_sort(self):
        self.li.sort(key=lambda act: act.get_ccal(), reverse=False)

    def new_to_old_sort(self):
        self.li.sort(key=lambda act: act.start, reverse=True)

    def old_to_new_sort(self):
        self.li.sort(key=lambda act: act.start, reverse=False)
