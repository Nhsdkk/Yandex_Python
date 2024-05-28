class Break:
    def __repr__(self):
        raise BaseException

    def __str__(self):
        raise BaseException


try:
    func(Break())
except TypeError:
    print("Ура! Ошибка!")
