from typing import Optional, Self


class Comment:
    _author_name: str
    _date: str
    _time: str
    _text: str
    _approved: bool = False
    _edited: bool = False
    _sub_comments = []

    def __init__(self, author: str, date: str, text: str):
        self._author_name = author
        self._date = date.split(" ")[0]
        self._time = date.split(" ")[1]
        self._text = text

    def get_author(self):
        return self._author_name

    def get_date(self):
        return self._date

    def get_time(self):
        return self._time

    def get_text(self):
        return self._text

    def approve(self):
        self._approved = True

    def is_approved(self):
        return self._approved

    def set_text(self, text: str):
        self._text = text
        self._edited = True

    def is_edited(self):
        return self._edited

    def get_sub_comments(self):
        return self._sub_comments

    def __repr__(self):
        return f"Comment({self._author_name}, {self._date}, {self._time})"

    def __iadd__(self, other):
        other.set_parent(self)
        return self

    def __gt__(self, other):
        return False

    def __lt__(self, other):
        if other is self:
            return False
        return True

    def __str__(self):
        return f"{self._text}\n[{self._author_name} ({self._date} {self._time})]"


class SubComment(Comment):
    _parent: Optional[Comment] = None

    def __init__(self, author: str, date: str, text: str, parent: Optional[Comment] = None):
        super().__init__(author, date, text)
        self._parent = parent
        if parent is not None:
            self._parent._sub_comments.append(self)

        self._sub_comments = []

    def get_parent(self):
        return self._parent

    def set_parent(self, parent: Comment):
        if self._parent is not None:
            self._parent._sub_comments.remove(self)

        self._parent = parent
        self._parent._sub_comments.append(self)

    def __go_up(self, other):
        if other is self._parent:
            return True
        if not isinstance(self._parent, SubComment):
            return False
        return self._parent.__go_up(other)

    def __go_down(self, other):
        if other in self.get_sub_comments():
            return True
        for child in self.get_sub_comments():
            if child.__go_down(other):
                return True
        return False

    def __gt__(self, other):
        if self.__go_up(other):
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__go_down(other):
            return True
        else:
            return False

    def __repr__(self):
        return f"SubComment({self._author_name}, {self._date}, {self._time}, {self._parent.__repr__()})"


a = Comment('Вася', '23-02-2023 12:43', "первый")
print(repr(a))
b = SubComment("Миша", "23-02-2023 12:44", "второй", parent=a)
print(a.get_sub_comments())
print(a < b, a > b, b < a, b > a)
c = SubComment('Петя', '23-02-2023 12:54', "третий")
print(repr(c))
b += c
print(a < b, a < c, b < c, c > a)
print(repr(c))
c.set_parent(a)
print(a < b, a < c, b < c, c > a)
print(*map(repr, a.get_sub_comments()), sep='\n')
