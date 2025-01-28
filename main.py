from data.base.game_loop import Loop
import multiprocessing
from data.base.main_menu import main_menu
from data.base.config import *

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    process_draw = multiprocessing.Process(target=Loop, args=(queue,))
    process_math = multiprocessing.Process()
    process_draw.start()
    process_draw.join()
    global curr_level
    while True:
        if not process_draw.is_alive():
            if queue.get()["status_end"] == "open_new":
                process_draw = multiprocessing.Process(target=Loop, args=(queue,))
                process_draw.start()
                process_draw.join()
    # main_menu()