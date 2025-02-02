from data.items.item_base import ItemBase
from data.base.load_image import load_image

class Test_item(ItemBase):

    def __init__(self):
        super().__init__()

        self.name = "Тестовый предмет"
        self.description = "Это Тестовый предмет\nДальность: 10\nУрон: 10-20"
        self.weight = 1
        self.texture_inv = load_image("textures/items/test_item.png", colorkey=(255, 255, 255))
        self.texture_floor = load_image("textures/items/test_item.png", colorkey=(255, 255, 255))
        self.range = 10
        self.min_damage = 10
        self.max_damage = 20
        self.crit_chance = 50
        self.use_ap = 1
        self.type = 'attackable'
        self.class_firearm = ("melee", "lash")


