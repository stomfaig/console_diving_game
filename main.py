import time

from typing import Tuple, List


Size = Tuple[int, int]
Location = Tuple[int, int]

class Buffer:
    def __init__(self, size: Size):
        self.size = size
        width, height = self.size
        self.data = [[" " for w in range(width)] for h in range(height)]

    def __getitem__(self, idx: Location):
        x, y = idx
        return self.data[x][y]

    def __setitem__(self, idx: Location, val: str):
        x, y = idx
        self.data[x][y] = val

class Render:

    @staticmethod
    def Print(string):
        print(string, end="", flush=True)

    @staticmethod
    def Move_cursor_to(
        position: Location,
    ):
        x, y = position
        print("\033[" + str(y+1) + ";" + str(x+1) + ";H", end="")

    @staticmethod
    def Move_cursor_to_upper_left():
        Render.Move_cursor_to((0, 0))

    @staticmethod
    def Clear_screen():
        Render.Move_cursor_to_upper_left()
        print("\033[J", end="")

    @staticmethod
    def Draw_rectangle(
            buffer: Buffer,
            upper_left: Location,
            lower_right: Location,
    ):
        for y in range(upper_left[1], lower_right[1]):
            Render.Move_cursor_to((upper_left[0], y))
            Render.Print("".join(buffer[y,upper_left[0]:lower_right[0]]))

    @staticmethod
    def Draw_buffer(buffer: Buffer):
        Render.Draw_rectangle(
            buffer=buffer,
            upper_left=(0, 0),
            lower_right=buffer.size,
        )

    def __init__(
            self,
            size: Size,
    ):
        Render.Clear_screen()
        self.size = size
        self.buffer = Buffer(self.size)
        self.flush_buffer()

    def flush_rectangle(
            self,
            upper_left: Location,
            lower_right: Location,
    ):
        self._check_point_in_scene(upper_left)
        self._check_point_in_scene(lower_right)

        Render.Draw_rectangle(
            buffer=self.buffer,
            upper_left = upper_left,
            lower_right=lower_right,
        )

    def flush_buffer(self):
        Render.Draw_buffer(self.buffer)

    def set_buffer(
            self,
            buffer: Buffer
    ):
        self.buffer = buffer
        self.flush_buffer()

    def _check_point_in_scene(
            self,
            point: Location,
    ):
        x, y = point

        assert x >= 0, f"x coordinate must be greater than 0"
        assert x < self.size[0], f"x coordinate must be smaller than the width of the canvas"
        assert y >= 0, f"y coordinate must be greater than 0"
        assert y < self.size[1], f"y coordinate must be smaller than the width of the canvas"

    def __getitem__(self, idx: Location):
        return self.buffer.__getitem__(idx)

    def __setitem__(self, idx: Location, val: str):
        return self.buffer.__setitem__(idx, val)

class Drawer(Render):

    def __init__(
            self,
            size: Size,
    ):
        super().__init__(
            size
        )

    def print_text_at(
            self,
            text: str,
            position: Tuple[int, int],
    ):
        self._check_point_in_scene(position)
        self._check_point_in_scene((position[0] + len(text) - 1, position[1]))

        x, y = position
        for i, ch in enumerate(text):
            self[y,x + i] = ch
        
        self.flush_buffer()


WIDTH = 144
HEIGHT = 30

def main():

    render = Drawer((WIDTH, HEIGHT))
    time.sleep(2)

    render.print_text_at("Hello world!", (0,0))

    time.sleep(2)

    render.print_text_at("Or ... Goodbye world?", (0, 1))

    time.sleep(2)
    
    render.print_text_at("i can also write like here", (40, 10))

    time.sleep(2)

    render.print_text_at("bOnK bOnK bOnK secret text", (0, 0))

    time.sleep(2)

    Render.Clear_screen()

if __name__ == '__main__':
    main()