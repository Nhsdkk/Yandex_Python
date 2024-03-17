class RedButton:
    cnt = 0

    def click(self):
        print("Тревога!")
        self.cnt += 1

    def count(self):
        return self.cnt
