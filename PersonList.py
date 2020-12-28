import pickle
from Fitnes.Person import Person


class PersonList:
    def save(self):
        with open("p.bin", "wb") as f:
            pickle.dump(self.list, f)

    def newUser(self, name, weight):
        self.list.append(Person(name, weight))

    def choseUser(self):  # замість цієї функції буде функція, що повертає потрібний профіль з графічного інтерфейсу
        print("Оберіть користувача:")
        print("0. Створити новий профіль")
        for i in range(len(self.list)):
            print(f"{i + 1}. {self.list[i].get_name()}")
        ans = int(input())
        if ans == 0:
            self.newUser(input("Ім\'я:"), input("Вага:"))
            return self.list[-1]
        return self.list[ans - 1]

    def delete(self, person):
        self.list.remove(person)
