from Fitnes.PersonList import PersonList
from Fitnes.Person import Person
from Fitnes.Activity import Activity, Running, Walking, Cycling


class FitProgram:
    def __init__(self):
        self.PL = PersonList()
        self.user = self.PL.choseUser()

    def menu(self):
        while True:
            print("Меню: \n1.Глолвна \n2.Журнал \n3.Профіль \n4.Вихід")
            ans = int(input())
            if ans == 1:
                self.menu_main()
            elif ans == 2:
                self.user._activityList.print()
            elif ans == 3:
                self.profile()
            elif ans == 4:
                self.PL.save()
                return

    def menu_main(self):
        while True:
            print("\t", self.user._name)
            print("Вага: ", self.user._weightDynamic[-1][0])
            print("Бали: ", self.user._pointS)
            print("Км: ", self.user._distanceS)
            print("Ккал: ", self.user._ccalS)
            print("1.Додати активність")
            print("2.Назад")
            ans = int(input())
            if ans == 1:
                self.user.addActivity()
            elif ans == 2:
                return

    def profile(self):
        while True:
            print(self.user._name)
            try:
                print("Male" if self.user.sex == 1 else "Female")
            except:
                pass
            try:
                print("Ріст: ", self.user.height)
            except:
                pass
            try:
                print("Дата народження:", self.user.birthday.strftime("%d %b %Y"))
            except:
                pass
            print("1. Динаміка ваги \n2. Додати поточну вагу\n3. Назад\n4. Видалити поточний профіль")
            ans = int(input())
            if ans == 1:
                print("1. За рік \n2. За місяць")
                ans1 = int(input())
                if ans1 == 1:
                    li = self.user.lastYearWeightDynamic()
                    for i in li:
                        print(i)
                else:
                    li = self.user.lastMonthWeightDynamic()
                    for i in li:
                        print(i)
            if ans == 2:
                self.user.setWeight(int(input("Введіть поточну вагу:")))
            if ans == 4:
                self.PL.delete(self.user)
                if len(self.PL.list) == 0:
                    self.PL.newUser()
                self.user = self.PL.choseUser()
            else:
                return



program = FitProgram()
program.menu()
