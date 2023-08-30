from render import Render
from entities.jelly_fish import JellyFish
from entities.data_screen import DataScreen
import time

entities = []

def draw(render: Render):

    for entity in entities:
        entity.draw(render)

def main():

    entities.append(JellyFish())
    entities.append(DataScreen())

    render = Render((144, 30))

    for _ in range(5):
        render.clear()
        draw(render)
        render.flush_buffer()

        time.sleep(1)

    time.sleep(2)

    Render.Clear_screen()

if __name__ == "__main__":
    main()