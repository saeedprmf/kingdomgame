from ursina import *


class menu(Entity):
	def __init__(self,camera):
		super().__init__()
		print("saed")
		self.btns = []
		adb = self.adb
		@adb 
		Button(text = "saeed")
		print(self.btns[0].text)
	def adb(self,b):
		self.btns.append(b)

	def destroy(self):
		pass

