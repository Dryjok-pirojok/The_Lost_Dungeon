from data.base.game_loop import Loop, Game_main
import multiprocessing
from data.base.main_menu import main_menu
from data.base.config import *
from data.base.load_image import load_image

if __name__ == "__main__":

    queue = multiprocessing.Queue()
    process_draw = multiprocessing.Process(target=Game_main, args=(queue,))
    process_math = multiprocessing.Process()
    process_draw.start()
    process_draw.join()
    global curr_level
    while True:
        if not process_draw.is_alive():
            # if queue.get()["status_end"] == "open_new":
            #     process_draw = multiprocessing.Process(target=Game_main, args=(queue,))
            #     process_draw.start()
            #     process_draw.join()
            if queue.get()["status_end"] == "game_ended":
                break
    # main_menu()