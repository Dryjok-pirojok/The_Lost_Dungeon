from data.items.weapons.weapon_base import WeaponBase
from data.base.load_image import load_image

class Lash():

    def __init__(self):
        super().__init__()

        self.name = "Плетка"
        self.description = ("Плетка из очень плотной резины. Создана\nспециально чтобы наказывать "
                            "непослушных slaves\nДальность: 2\nУрон: 10-20")
        self.weight = 1
        self.texture_inv = load_image("textures/items/lash.png", colorkey=(255, 255, 255))
        self.texture_floor = load_image("textures/items/lash.png", colorkey=(255, 255, 255))
        self.range = 2
        self.min_damage = 10
        self.max_damage = 20
        self.crit_chance = 10
        self.use_ap = 5
        self.type = 'attackable'
        self.class_firearm = ("melee", "lash")