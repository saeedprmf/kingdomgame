from ursina import *
from map import Map

class game(Entity):
    def __init__(self,map_given : bool = False, add_to_scene_entities=True, enabled=True, **kwargs):
        super().__init__(add_to_scene_entities, enabled, **kwargs)
        





