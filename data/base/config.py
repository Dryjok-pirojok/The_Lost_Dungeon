import pygame
from levels.TEST_LEVELS.test_level_01 import Test_level_01
from levels.TEST_LEVELS.test_level_02 import Test_level_02
"""НАСТРОЙКИ ИГРЫ"""

button_keys = {"inventory": pygame.K_e, "menu": pygame.K_ESCAPE, "console": pygame.K_COMMA}

FPS = 144

curr_level = Test_level_02

levels = [Test_level_01, Test_level_02]