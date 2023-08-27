import time

from typing import Tuple, List

class Render:

    @staticmethod
    def _print(string):
        print(string, end="", flush=True)


    @staticmethod
    def _move_cursor_to(
        position: Tuple[int, int],
    ):
        x, y = position
        print("\033[" + str(y+1) + ";" + str(x+1) + ";H", end="")

    @staticmethod
    def _move_cursor_to_upper_left():
        Render._move_cursor_to((0, 0))

    @staticmethod
    def _clear_screen():
        Render._move_cursor_to_upper_left()
        print("\033[J", end="")

    @staticmethod
    def _draw_rectangle(
            buffer: List[List[str]],
            upper_left: Tuple[int, int],
            lower_right: Tuple[int, int],
    ):
        for y in range(upper_left[1], lower_right[1]):
            Render._move_cursor_to((upper_left[0], y))
            Render._print("".join(buffer[y][upper_left[0]:lower_right[0]]))

    @staticmethod
    def _draw_buffer(buffer: List[List[str]]):
        Render._draw_rectangle(
            buffer=buffer,
            upper_left=(0, 0),
            lower_right=(144, 30),
        )

    @staticmethod
    def _get_empty_buffer(
        width: int,
        height: int,
    ):
        return [[" " for w in range(width) ] for h in range(height)]

    def __init__(
            self,
            width: int,
            height: int
    ):
        Render._clear_screen()
        self.width = width
        self.height = height
        self.buffer = Render._get_empty_buffer(self.width, self.height)
        self.flush_buffer()

    def flush_rectangle(
            self,
            upper_left: Tuple[int, int],
            lower_right: Tuple[int, int],
    ):
        Render._draw_rectangle(
            self._draw_buffer(
                buffer=self.buffer,
                upper_left = upper_left,
                lower_right=lower_right,
            )
        )

    def flush_buffer(self):
        Render._draw_buffer(self.buffer)

    def __del__(self):
        Render._clear_screen()

    def __getitem__(self, idx):
        i, j = idx
        return self.buffer[i][j]

    def __setitem__(self, idx, val):
        i, j = idx
        self.buffer[i][j] = val

class Drawer(Render):

    def __init__(
            self,
            width: int,
            height: int
    ):
        super().__init__(
            width,
            height,
        )

    def print_text_at(
            self,
            text: str,
            position: Tuple[int, int],
    ):
        x, y = position
        for i, ch in enumerate(text):
            self[y,x + i] = ch
        
        self.flush_buffer()


WIDTH = 144
HEIGHT = 30

def get_empty_buffer():
    return [[" " for w in range(WIDTH) ] for h in range(HEIGHT)]

def main():

    render = Drawer(WIDTH, HEIGHT)
    time.sleep(2)

    render.print_text_at("Hello world!", (0,0))

    time.sleep(2)

    render.print_text_at("Or ... Goodbye world?", (0, 1))

    time.sleep(2)

    del render

if __name__ == '__main__':
    main()