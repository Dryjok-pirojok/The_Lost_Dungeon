import pygame
from levels.TEST_LEVELS.test_level_01 import Test_level_01
from levels.TEST_LEVELS.test_level_02 import Test_level_02
from levels.TEST_LEVELS.test_level_03 import Test_level_03
"""НАСТРОЙКИ ИГРЫ"""

global button_keys
button_keys = {"inventory": pygame.K_e, "menu": pygame.K_ESCAPE, "console": pygame.K_COMMA, "char": pygame.K_c}

global FPS
FPS = 144

global curr_level
a = Test_level_02(Test_level_03)
curr_level = a

levels = [a, Test_level_03]

SIZE = (1920, 1080)

VOLUME = 1