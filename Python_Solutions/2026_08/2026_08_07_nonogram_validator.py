def is_valid_nonogram(clue, cells):
    cells_str = "".join([str(" ") if d == 0 else str(d) for d in cells]).strip()
    cells_str = "0".join(cells_str.split())

    clue_str = "0".join("1" * n for n in clue)

    return clue_str == cells_str

# print(is_valid_nonogram([3, 2], [1, 1, 1, 0, 1, 1]))
# print(is_valid_nonogram([3, 2], [0, 1, 1, 1, 1, 1]))
# print(is_valid_nonogram([1, 1, 1, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1]))
# print(is_valid_nonogram([1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]))
# print(is_valid_nonogram([3, 2, 3], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]))
# print(is_valid_nonogram([3, 2, 3], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]))