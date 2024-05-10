class Test():
    def __init__(self):
        self.public = "публичный атрибут"
        self._protected = "защищенный атрибут"
        self.__privat = "приватный атрибут"

    def get_privat(self):
        return self.__privat

    def set_privat(self, value):
        self.__privat = value


test = Test()
print(test.public)
print(test._protected)

print(test.get_privat())
test.set_privat("получили значение приватного атрибута\n")
print(test.get_privat())


class Test():
    def public_func(self):
        print("публичный мктод")

    def _protected_func(self):
        print("защищенный метод")

    def __privat_func(self):
        print("приватный метод")

    def test_privat(self):
        self.__privat_func()

test = Test()
test.public_func()

test._protected_func()

test.test_privat()
