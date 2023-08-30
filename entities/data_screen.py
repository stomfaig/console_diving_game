from entities.entity import Entity
from render import Render


class DataScreen(Entity):

    initial_position = (0, 0)

    states = [
        [
            "    .____.____.    ",
            "   /  \  H  /  \\  ",
            "  /    \ | /    \\ ",
            " / E --- . --- F \\",
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

    def draw(
            self,
            render: Render,
    ):
        pass