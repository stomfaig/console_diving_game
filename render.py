from __future__ import annotations

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
        rows_lens = [len(row) for row in data]
        assert min(rows_lens)==max(rows_lens), f"Inconsistent line lengths"
        buffer = Buffer((len(data[0]), len(data)))
        buffer.data = data
        return buffer

    @staticmethod
    def from_stiring_list(data: List[str]):
        buffer_data = []
        for line in data:
            buffer_data.append([ch for ch in line])
        return Buffer.with_content(buffer_data)

    @staticmethod
    def _empty_data_with_size(size: Size):
        w, h = size
        data = [[" " for w in range(w)] for h in range(h)]
        return data

    def __init__(self, size: Size):
        self.size = size
        self.data = Buffer._empty_data_with_size(size)

    def __getitem__(self, idx: Location):
        x, y = idx
        return self.data[y][x]

    def __setitem__(self, idx: Location, val: str):
        x, y = idx
        self.data[y][x] = val

    def set_buffer(
            self,
            buffer: Buffer,
    ):
        assert self.size==buffer.size
        self.data = buffer.data

    def clear(self):
        self.data = Buffer._empty_data_with_size(self.size)

    def set_rectangle(
            self,
            buffer: Buffer,
            upper_left: Location,
    ):
        w, h = buffer.size

        for y in range(h):
            for x in range(w):
                self[x + upper_left[0], y + upper_left[1]] = buffer[x, y]

    def _check_point_in_scene(
            self,
            point: Location,
    ):
        x, y = point

        assert x >= 0, f"x coordinate must be greater than 0"
        assert x < self.size[0], f"x coordinate ({x}) must be smaller than the width ({self.size[0]}) of the canvas"
        assert y >= 0, f"y coordinate must be greater than 0"
        assert y < self.size[1], f"y coordinate ({y}) must be smaller than the height ({self.size[1]}) of the canvas"

    def print_text_at(
            self,
            text: str,
            position: Location,
    ):
        self._check_point_in_scene(position)
        self._check_point_in_scene((position[0] + len(text) - 1, position[1]))

        x, y = position
        for i, ch in enumerate(text):
            self[x + i, y] = ch

class Render(Buffer):

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
            for x in range(upper_left[0], lower_right[0]):
                Render.Print(buffer[x, y])

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
        super().__init__(size)
        Render.Clear_screen()
        self.flush_buffer()

    def flush_rectangle(
            self,
            upper_left: Location,
            lower_right: Location,
    ):
        self._check_point_in_scene(upper_left)
        self._check_point_in_scene(lower_right)

        Render.Draw_rectangle_from_screen_buffer(
            buffer=self,
            upper_left = upper_left,
            lower_right=lower_right,
        )

    def flush_buffer(self):
        Render.Draw_buffer(self)