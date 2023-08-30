import time

from typing import Tuple, List


Size = Tuple[int, int]
Location = Tuple[int, int]

class Buffer:

    @staticmethod
    def with_size(size: Size):
        return Buffer(size)
    
    @staticmethod
    def with_content(data: List[List[str]]):
        # need a check
        buffer = Buffer((len(data), len(data[0])))
        buffer.data = data
        return buffer

    def from_stiring_list(data: List[str]):
        buffer_data = []
        for line in data:
            buffer_data.append([ch for ch in line])
        return Buffer.with_content(buffer_data)

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
    def Draw_rectangle_from_screen_buffer(
            buffer: Buffer,
            upper_left: Location,
            lower_right: Location,
    ):

        for y in range(upper_left[1], lower_right[1]):
            Render.Move_cursor_to((upper_left[0], y))
            Render.Print("".join(buffer[y,upper_left[0]:lower_right[0]]))

    @staticmethod
    def Draw_buffer(buffer: Buffer):
        Render.Draw_rectangle_from_screen_buffer(
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

        Render.Draw_rectangle_from_screen_buffer(
            buffer=self.buffer,
            upper_left = upper_left,
            lower_right=lower_right,
        )

    def flush_buffer(self):
        Render.Draw_buffer(self.buffer)

    def set_rectangle(
            self,
            buffer: Buffer,
            upper_left: Location,
    ):
        w, h = buffer.size

        for y in range(h):
            for x in range(w):
                self.buffer[x + upper_left[0], y + upper_left[1]] = buffer[x, y]

    def set_buffer(
            self,
            buffer: Buffer
    ):
        self.buffer = buffer
        self.flush_buffer()

    def clear_buffer(self):
        self.buffer = Buffer(self.buffer.size)

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