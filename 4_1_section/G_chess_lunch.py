def can_eat(start_pos: tuple[int], end_pos: tuple[int]):
    diffs = [1, 2]
    variants = []

    for x_diff in diffs:
        for y_diff in diffs:
            if x_diff != y_diff:
                variants += [(x_diff, -y_diff), (-x_diff, y_diff), (x_diff, y_diff), (-x_diff, -y_diff)]

    for item in variants:
        start_x, start_y = start_pos[0], start_pos[1]
        start_x += item[0]
        start_y += item[1]

        if start_x == end_pos[0] and start_y == end_pos[1]:
            return True

    return False
