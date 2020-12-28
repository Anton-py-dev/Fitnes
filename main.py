from Fitnes.PersonList import PersonList
import pickle
from Fitnes.Person import Person
from datetime import datetime, date, time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Fitnes.mw import Ui_MainWindow
from Fitnes.test2 import Ui_Dialog
from Fitnes.login import Ui_Dialog1
from Fitnes.registration import Ui_Dialog2
from Fitnes.Activity import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarSet, QBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter
import random


class FitProgram:
    def __init__(self):
        self.PL = PersonList()
        self.user = None # self.PL.choseUser()


class LogIn(QtWidgets.QDialog, Ui_Dialog1):
    def __init__(self, parent=None):
        super(LogIn, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.pushButton.clicked.connect(self.lIn)
        self.pushButton_2.clicked.connect(self.registration)

        try:
            with open("p.bin", "rb") as f:
                program.PL.list = pickle.load(f)
            self.showList()
        except FileNotFoundError:
            program.PL.list = []
            self.registration()

    def showList(self):
        i = 1
        for p in program.PL.list:
            newitem = QListWidgetItem()
            print(p.get_name())
            newitem.setText(p.get_name())
            path = "icons/" + str(i) + ".png"
            newitem.setIcon(QtGui.QIcon(path))
            self.listWidget.addItem(newitem)
            i += 1


    def closeEvent(self, event):
        program.PL.save()
        event.accept()

    def lIn(self):
        person = program.PL.list[int(self.listWidget.currentRow())]
        program.user = person
        self.showDialog()
        self.close()

    def showDialog(self):
        self.add = MainWindow()
        self.add.show()

    def registration(self):
        self.add1 = Registration()
        self.add1.show()
        self.listWidget.clear()


class Registration(QtWidgets.QDialog, Ui_Dialog2):
    def __init__(self, parent=None):
        super(Registration, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.accepted.connect(self.approve)
        self.spinBox.setMaximum(500)

    def approve(self):
        print(self.lineEdit.text())
        program.PL.newUser(self.lineEdit.text(), self.spinBox.value())
        application.showList()


class AddActWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(AddActWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.buttonBox.accepted.connect(self.addActivity)
        self.comboBox.currentIndexChanged.connect(self.showOrHide)

    def showOrHide(self):
        if self.comboBox.currentText() == "Біг" or self.comboBox.currentText() == "Прогулянка" or self.comboBox.currentText() == "Лижі":
            self.label_5.show()
            self.spinBox.show()
            self.label_7.hide()
            self.spinBox_2.hide()
        elif self.comboBox.currentText() == "Велосипед":
            self.label_7.show()
            self.spinBox_2.show()
            self.label_5.show()
            self.spinBox.show()
        else:
            self.label_5.hide()
            self.spinBox.hide()
            self.label_7.hide()
            self.spinBox_2.hide()


    def addActivity(self):
        print(self.comboBox.currentText())
        ans = self.comboBox.currentText()
        if ans == "Біг":
            newActivity = Running(program.user)
            newActivity.setDistance(self.spinBox.value())
        elif ans == "Велосипед":
            newActivity = Cycling(program.user)
            newActivity.setDistance(self.spinBox.value())
            newActivity.setSpeed(self.spinBox_2.value())
        elif ans == "Плавання":
            newActivity = Swimming(program.user)
        elif ans == "Хатха-Йога":
            newActivity = HathaYoga(program.user)
        elif ans == "Прогулянка":
            newActivity = Walking(program.user)
            newActivity.setDistance(self.spinBox.value())
        elif ans == "Лижі":
            newActivity = Skiing(program.user)
            newActivity.setDistance(self.spinBox.value())
        elif ans == "Боулінг":
            newActivity = Bowling(program.user)
        elif ans == "Аквааеробіка":
            newActivity = AquaAerobics(program.user)
        elif ans == "Бодіфлекс":
            newActivity = Bodyflex(program.user)
        elif ans == "Гімнастика":
            newActivity = Gymnastics(program.user)
        elif ans == "Мотузка":
            newActivity = JumpingRope(program.user)
        elif ans == "Круг":
            newActivity = Hoop(program.user)
        elif ans == "Пілатес":
            newActivity = Pilates(program.user)
        elif ans == "Сучасні танці":
            newActivity = ModernDances(program.user)
        elif ans == "Балет":
            newActivity = Ballet(program.user)
        elif ans == "Танці диско":
            newActivity = DiscoDancing(program.user)
        elif ans == "Фігурне катання":
            newActivity = FigureSkating(program.user)
        elif ans == "Спуск на лижах":
            newActivity = DownhillSkiing(program.user)
        elif ans == "Водне поло":
            newActivity = WaterPolo(program.user)
        elif ans == "Каленетика":
            newActivity = Callanetics(program.user)
        elif ans == "Академічна гребля":
            newActivity = Rowing(program.user)
        elif ans == "Водні лижі":
            newActivity = WaterSkis(program.user)
        elif ans == "Тай-Бо":
            newActivity = TaiBo(program.user)
        elif ans == "Бадмінтон":
            newActivity = Badminton(program.user)
        elif ans == "Гольф":
            newActivity = Golf(program.user)
        elif ans == "Аеробіка":
            newActivity = Aerobic(program.user)
        elif ans == "Кросфіт":
            newActivity = CrossFit(program.user)
        print(self.dateEdit.date())
        print(self.timeEdit.time())
        print(self.timeEdit_2.time())
        d = self.dateEdit.date()
        newActivity.date = date(int(d.toString("yyyy")), int(d.toString("M")), int(d.toString("d")))
        start = self.timeEdit.time()
        newActivity.start = datetime.combine(newActivity.date, time(int(start.toString("h")), int(start.toString("m")), 0, 0))
        end = self.timeEdit_2.time()
        newActivity.end = datetime.combine(newActivity.date, time(int(end.toString("h")), int(end.toString("m")), 0, 0))
        newActivity.time = newActivity.end - newActivity.start
        newActivity.note = self.textEdit.toPlainText()
        newActivity.multiplier()
        program.user.activityList.append(newActivity)
        program.user.calculate_last_day()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.pushButton_7.clicked.connect(self.showDialog)
        self.pushButton.clicked.connect(self.update)
        self.listWidget_2.itemClicked.connect(self.selectedItem)
        self.pushButton_6.clicked.connect(self.delete)
        self.pushButton_8.clicked.connect(self.userChanges)
        self.tabWidget_2.currentChanged.connect(self.updateMain)
        self.pushButton_5.clicked.connect(self.showGraph)
        self.dateEdit_5.setDate(QDate.currentDate())
        self.dateEdit_4.setDate(QDate.currentDate())
        self.update()
        program.user.calculate_last_day()
        self.username_2.setText(program.user.get_name())
        self.distanceBox_2.setValue(program.user.get_distanceGoal())
        self.ccalBox_2.setValue(program.user.get_ccalGoal())
        self.pointBox_2.setValue(program.user.get_pointGoal())
        self.weightBox_2.setValue(int(program.user.get_weight()))
        self.hightBox_2.setValue(program.user.height)
        if program.user.sex == "Чоловік":
            self.sexBox_2.setCurrentIndex(0)
        else:
            self.sexBox_2.setCurrentIndex(1)
        self.updateMain()

        self.dateEdit_6.setDate(program.user.birthday)
        self.ccalBar_2.setMinimum(0)
        self.ccalBar_2.setMaximum(program.user.get_ccalGoal())
        if int(program.user.get_ccalS()) > program.user.get_ccalGoal():
            self.ccalBar_2.setValue(program.user.get_ccalGoal())
        else:
            self.ccalBar_2.setValue(int(program.user.get_ccalS()))
        self.pointsBar_2.setMinimum(0)
        self.pointsBar_2.setMaximum(program.user.get_pointGoal())
        if int(program.user.get_pointS()) > program.user.get_pointGoal():
            self.ccalBar_2.setValue(program.user.get_pointGoal())
        else:
            self.ccalBar_2.setValue(int(program.user.get_pointS()))
        self.distanceBar_2.setMinimum(0)
        self.distanceBar_2.setMaximum(program.user.get_distanceGoal())
        if int(program.user.get_distanceS()) > program.user.get_distanceGoal():
            self.ccalBar_2.setValue(program.user.get_distanceGoal())
        else:
            self.ccalBar_2.setValue(int(program.user.get_distanceS()))

    def showGraph(self):
        s = self.dateEdit_4.date()
        e = self.dateEdit_5.date()
        start = date(int(s.toString("yyyy")), int(s.toString("M")), int(s.toString("d")))
        end = date(int(e.toString("yyyy")), int(e.toString("M")), int(e.toString("d")))
        self.gr = Graphic(start, end)
        self.gr.show()

    def userChanges(self):
        program.user.set_goals(self.pointBox_2.value(), self.ccalBox_2.value(), self.distanceBox_2.value())
        program.user.height = self.hightBox_2.value()
        program.user.setWeight(self.weightBox_2.value())
        program.user.birthday = self.dateEdit_6.date()
        if self.sexBox_2.currentIndex() == 0:
            program.user.sex = "Чоловік"
        else:
            program.user.sex = "Жінка"

    def updateMain(self):
        self.ccalBar_2.setMaximum(program.user.get_ccalGoal())
        if int(program.user.get_ccalS()) > program.user.get_ccalGoal():
            self.ccalBar_2.setValue(program.user.get_ccalGoal())
        else:
            self.ccalBar_2.setValue(int(program.user.get_ccalS()))
        self.pointsBar_2.setMaximum(program.user.get_pointGoal())
        if int(program.user.get_pointS()) > program.user.get_pointGoal():
            self.pointsBar_2.setValue(program.user.get_pointGoal())
        else:
            self.pointsBar_2.setValue(int(program.user.get_pointS()))
        self.distanceBar_2.setMaximum(program.user.get_distanceGoal())
        if int(program.user.get_distanceS()) > program.user.get_distanceGoal():
            self.distanceBar_2.setValue(program.user.get_distanceGoal())
        else:
            self.distanceBar_2.setValue(int(program.user.get_distanceS()))
        self.ccalNumber_2.display(int(program.user.get_ccalS()))
        self.pointsNumber_2.display(int(program.user.get_pointS()))
        self.distanceNumber_2.display(int(program.user.get_distanceS()))

    def closeEvent(self, event):
        program.PL.save()
        event.accept()

    def showDialog(self):
        self.add = AddActWindow()
        self.add.show()

    def update(self):
        self.listWidget_2.clear()
        ans = self.comboBox.currentIndex()
        if ans == 0:
            program.user.activityList.new_to_old_sort()
        elif ans == 1:
            program.user.activityList.old_to_new_sort()
        elif ans == 2:
            program.user.activityList.points_l_to_h_sort()
        elif ans == 3:
            program.user.activityList.points_h_to_l_sort()
        elif ans == 4:
            program.user.activityList.ccal_l_to_h_sort()
        elif ans == 5:
            program.user.activityList.ccal_h_to_l_sort()
        li = program.user.get_activityList()
        for it in li:
            newitem = QListWidgetItem()
            print(it.name)
            text = it.name + "   (" + it.date.strftime("%d %B") + ")"
            newitem.setText(text)
            newitem.setIcon(QtGui.QIcon(it.icon))
            self.listWidget_2.addItem(newitem)

    def selectedItem(self):
        act = program.user.activityList.li[int(self.listWidget_2.currentRow())]
        self.groupBox_2.setTitle(act.name)
        text = "Date: " + act.date.strftime("%d %B")
        self.label_22.setText(text)
        text = "Тривалість: " + str(act.time)
        self.label_24.setText(text)
        text = "Time: " + act.start.strftime("%H:%M") + " - " + act.end.strftime("%H:%M")
        self.label_23.setText(text)
        text = "Ccal: " + str(int(act.get_ccal()))
        self.label_26.setText(text)
        text = "Points: " + str(int(act.get_points()))
        self.label_27.setText(text)
        if act.name != "Біг" and act.name != "Велосипед" and act.name != "Ходьба" and act.name != "Лижі":
            self.label_28.hide()
        else:
            self.label_28.show()
            text = "Distance: " + str(int(act.get_distance())) + " м"
            self.label_28.setText(text)
        text = act.note
        self.textBrowser_2.setText(text)

    def delete(self):
        program.user.activityList.li.pop(int(self.listWidget_2.currentRow()))
        self.update()
        program.user.calculate_last_day()


class Graphic(QtWidgets.QMainWindow):
    def __init__(self, start, end):
        super().__init__()
        self.resize(800, 600)
        self.start = start
        self.end = end

        set0 = QBarSet("Points")
        set1 = QBarSet("Ccal")
        set2 = QBarSet("Distance")

        program.user.activityList.new_to_old_sort()
        today = self.end
        todayP = 0
        todayC = 0
        todayD = 0
        maxi = 0
        day = []
        fact = Activity(program.user)
        fact.date = date(int(self.end.strftime("%Y")), int(self.end.strftime("%m")), int(self.end.strftime("%d")))
        program.user.activityList.append(fact)
        for act in program.user.activityList.li:
            if self.start <= act.date <= self.end:
                if today == act.date:
                    todayP += int(act.get_points())
                    todayC += int(act.get_ccal())
                    try:
                        todayD += int(act.get_distance())
                    except:
                        pass
                else:
                    day.append(today.strftime("%d %B"))
                    set0.append(todayP)
                    set1.append(todayC)
                    set2.append(todayD)
                    todayP = 0
                    todayC = 0
                    todayD = 0
                    today = act.date
                    todayP += int(act.get_points())
                    todayC += int(act.get_ccal())
                    try:
                        todayD += int(act.get_distance())
                    except:
                        pass
                if todayD > maxi:
                    maxi = todayD
                if todayC > maxi:
                    maxi = todayC
                if todayP > maxi:
                    maxi = todayP


        series = QBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Stat")
        chart.setAnimationOptions(QChart.SeriesAnimations)


        asisX = QBarCategoryAxis()
        asisX.append(day)
        asisY = QValueAxis()
        asisY.setRange(0, maxi)

        chart.addAxis(asisX, Qt.AlignBottom)
        chart.addAxis(asisY, Qt.AlignLeft)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartViev = QChartView(chart)
        self.setCentralWidget(chartViev)
        program.user.activityList.li.pop()


program = FitProgram()
app = QtWidgets.QApplication([])
application = LogIn()
application.show()


sys.exit(app.exec_())


