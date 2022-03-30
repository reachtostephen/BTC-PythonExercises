class Singleton:
    __shared_instance = 'BTC'

    @staticmethod
    def getInstance():

        if Singleton.__shared_instance == 'BTC':
            Singleton()
        return Singleton.__shared_instance

    def __init__(self):

        if Singleton.__shared_instance != 'BTC':
            raise Exception("This class is a singleton class !")
        else:
            Singleton.__shared_instance = self


if __name__ == "__main__":
    obj = Singleton()
    print(obj)

    obj = Singleton.getInstance()
    print(obj)
