from ursina import *



class Map(Entity):
	def __init__(self ,scale ,position = None):
		if position:
			super().__init__(
			model = "quad",
			scael = scale,
			position = position
			)
			self.movem = False
		else:
			super().__init__(
			model = "quad",
			scael = scale,
			position = (0,0,0)
			)
			self.movem = True

	def move(self):
		if held_keys['w']:
			self.y += 5 * time.dt
		if held_keys['d']:
			self.x += 5 * time.dt
		if held_keys['s']:
			self.y -= 5 * time.dt
		if held_keys['a']:
			self.x -= 5 * time.dt
	def input(self,key):
		if key == "enter":
			self.movem = False

	def update(self):
		if self.movem:
			self.move()



