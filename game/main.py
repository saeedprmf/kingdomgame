from ursina import *
from map import Map
from ursina.prefabs.editor_camera import EditorCamera as ec
from menu import MainMenu


app = Ursina()

window.fullscreen = True

menu = MainMenu()

def input(key):
	if key == "q":
		exit()

app.run()
