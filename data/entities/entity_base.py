class EntityBase:
    ref_id: int  # для обращения во время игры, у каждого объекта свой id
    base_id: int  # для создания объектов, у каждого типа объектов свой id
    # (например: лезермен имеет base_id =  10, ref_id = 1069)
    display_name: str
    # characteristics

    # charact. end
    inventory: dict
    current_hp: int
    current_ap: int
    

    def __init__(self):
        pass


