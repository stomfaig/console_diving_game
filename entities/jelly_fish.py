from entities.entity import Entity

class JellyFish(Entity):

    states = [ 
        [
            "  __  ",
            " OOOO ",
            "OOOOOO",
            " /  \\ ",
        ], 
        [
            "  __  ",
            " OOOO ",
            "OOOOOO",
            " \\  / ",
        ]
    ]

    def update(self):

        self.current_state += 1
        self.current_state %= 2

        self.x += 2
        self.y += 3
