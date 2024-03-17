class Programmer:
    _positions = ['Junior', 'Middle', 'Senior']
    _salary_map = {
        'Junior': 10,
        'Middle': 15,
        'Senior': 20,
    }
    _raise_delta = 1
    _current_money = 0
    _current_time_spent_working = 0

    def __init__(self, name, position):
        self._name = name
        self._current_salary = self._salary_map[position]
        self._current_position = position
        self._work_info = []

    def work(self, time):
        self._current_time_spent_working += time
        self._current_money += self._current_salary * time
        self._work_info.append(f"{self._name} {self._current_time_spent_working}ч. {self._current_money}тгр.")

    def info(self):
        return self._work_info[-1]

    def rise(self):
        if self._current_position == 'Senior':
            self._current_salary += 1
        else:
            position_index = self._positions.index(self._current_position) + 1
            self._current_position = self._positions[position_index]
            self._current_salary = self._salary_map[self._current_position]
