

class Test_level_02:
    lvl_name: str = "test_02"
    col_x: int = 15
    col_y: int = 15
    cells: tuple = (2, 2, 2, 2, 2, 2, 1, 1, 2, 2,) * 30
    to_nest_level: tuple = ([10, 10], [11, 10], [10, 11], [11, 11])

    def __init__(self, level_1):
        for i in self.to_nest_level:
            i.append(level_1)