from data.base.game_loop import Loop
import multiprocessing
from data.base.main_menu import main_menu

if __name__ == "__main__":
    # process_draw = multiprocessing.Process(target=Loop())
    # process_math = multiprocessing.Process()
    # process_draw.start()
    # process_draw.join()
    main_menu()