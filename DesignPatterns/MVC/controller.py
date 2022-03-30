from model import Person
import view


def showAll():
    people_in_db = Person.getAll()
    # print(people_in_db)
    return view.showAllView(people_in_db)


def start():
    view.startView()
    i = input()
    if i.upper() == 'E':
        return showAll()
    elif i.upper() == 'B':
        return view.endView()


if __name__ == "__main__":
    start()
