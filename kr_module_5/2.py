class Comment:
    _author_name: str
    _date: str
    _time: str
    _text: str
    _approved: bool = False
    _edited: bool = False

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

    def __str__(self):
        return f"{self._text}\n[{self._author_name} ({self._date} {self._time})]"
