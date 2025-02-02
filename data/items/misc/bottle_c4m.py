from data.items.item_base import ItemBase
from data.base.load_image import load_image

class C4m_bottle(ItemBase):

    def __init__(self):
        super().__init__()

        self.name = "Баночка C4m"
        self.description = ("Баночка белой жидкости, которую собирает Van\nсо своих slaves. Очень полезна для "
                            "real man.\nВосстанавливает 20 здоровья.")
        self.weight = 1
        self.texture_inv = load_image("textures/items/bottle_of_c4m.png", colorkey=(255, 255, 255))
        self.texture_floor = load_image("textures/items/bottle_of_c4m.png", colorkey=(255, 255, 255))
        self.type = 'medicine'
        self.add_to_hp = 20