from entities.entity import Entity

class DataScreen(Entity):

    initial_position = (121, 18)
    called = 1

    states = [
        [
            "    .____.____.    ",
            "   /  \  H  /  \\   ",
            "  /    \ | /    \\  ",
            " / E --- . --- F \\ ",
            "+-----------------+",
            "| Gas left: .......",
            "| Depth:    .......",
            "| Time:     .......",
            "| Time:     .......",
            "| Time:     .......",
            "----+----+----+----",
            "[T1]| T2 | T3 | T4 ",
        ]
    ]

    def update(self):
        self.called *= 10
        self.states[0].print_text_at(str(self.called), (12, 5))