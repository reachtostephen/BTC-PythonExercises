from model import Person


def showAllView(li):
    print('In our company we have %i Employees. Here they are:' % len(li))
    for item in li:
        print(item)


def startView():
    print('Welcome to our Company')
    print('Press E for our Employee List, Press B for exit')


def endView():
    print('Goodbye!')
