class Cell:
    def __init__(self, status):
        self._status = status

    def status(self):
        return self._status


class Checkers:
    _start_char_index = ord('A')

    def __init__(self):
        self.matrix = []

        for col in range(8):
            for row in range(8):
                self.matrix.append(Cell("X"))

        self.init_values(0, 3, "W")
        self.init_values(5, 8, "B")

    def init_values(self, row_range_start, row_range_end, status):
        for col in "ABCDEFGH":
            for row in range(row_range_start, row_range_end):
                col_index = ord(col) - self._start_char_index
                if (col_index + row) % 2 != 0:
                    continue
                self.matrix[row * 8 + col_index] = Cell(status)

    def get_cell(self, pos):
        col_index = ord(pos[0]) - self._start_char_index
        row_index = int(pos[1]) - 1
        return self.matrix[row_index * 8 + col_index]

    def move(self, pos_from, pos_to):
        col_index_from = ord(pos_from[0]) - self._start_char_index
        row_index_from = int(pos_from[1]) - 1

        col_index_to = ord(pos_to[0]) - self._start_char_index
        row_index_to = int(pos_to[1]) - 1

        status = self.matrix[row_index_from * 8 + col_index_from].status()

        self.matrix[row_index_from * 8 + col_index_from] = Cell("X")
        self.matrix[row_index_to * 8 + col_index_to] = Cell(status)
