from render import (
    Location,
    Render,
    Buffer,
)

class Entity:

    states = []
    initial_position = (0,0)

    def __init__(
            self,
            position: Location = None,
    ):
        self.states = [Buffer.from_stiring_list(data) for data in self.states]
        self.current_state = 0

        if position == None:
            position = self.initial_position

        self.x = position[0]
        self.y = position[1]
        self.buffer: Buffer = None

    def update(self):
        pass

    def draw(
            self,
            render: Render,
    ):
        self.update()
        self.buffer = self.states[self.current_state]
        render.set_rectangle(
            buffer=self.buffer,
            upper_left=(self.x, self.y),
        )