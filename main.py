from Fitnes.Persone import Persone
from Fitnes.Activity import Activity, Running, Walking, Cycling


class FitProgram:
    def __init__(self):
        self.user = Persone("Default", 70)

    def menu(self):
        while True:
            print("Меню: \n1.Глолвна \n2.Журнал \n3.Профіль \n4.Вихід")
            ans = int(input())
            if ans == 1:
                self.menu_main()
            elif ans == 2:
                self.user.activityList.print()
            elif ans == 3:
                pass
            elif ans == 4:
                return

    def menu_main(self):
        while True:
            print("\t", self.user.name)
            print("Вага: ", self.user.weight)
            print("Бали: ", self.user.pointS)
            print("Км: ", self.user.distanceS)
            print("Ккал: ", self.user.ccalS)
            print("1.Додати активність")
            print("2.Назад")
            ans = int(input())
            if ans == 1:
                self.user.addActivity()
            elif ans == 2:
                return


program = FitProgram()
program.menu()
