class SubclassA:
    @staticmethod
    def method():
        return 'A'


class SubclassB:
    @staticmethod
    def method():
        return 'B'


class SubclassC:
    @staticmethod
    def method():
        return 'C'


class Facade:
    def __init__(self):
        self.sub1 = SubclassA()
        self.sub2 = SubclassB()
        self.sub3 = SubclassC()
        self.result = ''

    def final(self):
        self.result += self.sub1.method()
        self.result += self.sub2.method()
        self.result += self.sub3.method()
        return self.result


if __name__ == '__main__':
    facade = Facade()
    print(facade.final())
   