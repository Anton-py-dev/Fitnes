import pickle
from Fitnes.Persone import Persone

class PersonList:
    def __init__(self):
        try:
            with open("p.bin", "rb") as f:
                self.list = pickle.load(f)
        except FileNotFoundError:
            print("Створіть нового користувача")
            self.list = []
            self.newUser()

    def save(self):
        with open("p.bin", "wb") as f:
            pickle.dump(self.list, f)

    def newUser(self):
        self.list.append(Persone(input("Iм'я: "), int(input("Вага: "))))

    def choseUser(self):
        print("Оберіть користувача:")
        print("0. Створити новий профіль")
        for i in range(len(self.list)):
            print(f"{i+1}. {self.list[i].name}")
        ans = int(input())
        if ans == 0:
            self.newUser()
            return self.list[-1]
        return self.list[ans - 1]

    def delete(self, person):
        self.list.remove(person)