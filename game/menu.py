from ursina   import *
from requests import *
from conf 	  import get_conf


class MainMenu(Entity):
	def __init__(self):
		super().__init__()
		self.make_uis()

	def make_uis(self):
		self.uis = [
			Button(text = "start" , scale = (1,.2),y=.3 ,on_click = self.start),
			Button(text = "setting" , scale = (1,.2)),
			Button(text = "quit" , scale = (1,.2),y=-.3,on_click = self.quit)
		]
	def quit(self):
		exit()
	def start(self):
		self.destroy()
		if get_conf("logedin"):
			pass
		else:
			Login()
	def destroy(self):
		for i in self.uis:
			destroy(i)
		destroy(self)

class Sinup(Entity):
	def __init__(self):
		super().__init__()
		self.make_uis()
	def make_uis(self):
		self.uis = [
			Text("username:",text_color = color.white,x=-.40,y=.01),
			InputField(),
			Text("password:",text_color = color.white,x=-.40,y=-.09),
			InputField(y=-.1),
			Button(text="back",on_click = self.main_menu,scale = (.12,.05),y=-.2,x=-.1875),
			Button(text = "login",scale = (.25,.05),y=-.2,x=.125),
			Text("",y=.1,x=-.25),
		]
		self.status = self.uis[6]
		self.username = self.uis[1]
		self.password = self.uis[3]
		self.username.on_value_changed = self.check_username

	def check_username(self):
		print(self.username.text)
		df = post(f"{get_conf('url_server_1')}/username/check",json={'name':self.username.text})
		print(df.json())
		if df.json() == 1:
			self.status.text = 'username is valid'
			self.status.color = color.green
		else:
			self.status.text = "username is alredy there is"
			self.status.color = color.red
	def destroy(self):
		for i in self.uis:
			destroy(i)
		destroy(self)
	def main_menu(self):
		MainMenu()
		self.destroy()
class Login(Entity):
	def __init__(self):
		super().__init__()
		self.make_uis()
	def make_uis(self):
		p = Text(y=.15)
		self.uis = [
			Text("username:",text_color = color.white,x=-.40,y=.01,parent=p),
			InputField(parent = p),
			Text("password:",text_color = color.white,x=-.40,y=-.09,parent=p),
			InputField(y=-.11,parent=p),
			Button(text="back",on_click = self.main_menu,parent=p,scale = (.12,.05),y=-.2,x=-.1875),
			Button(text = "login",scale = (.25,.05),y=-.2,x=.125,parent=p),
			Text("",y=.1,x=-.25,parent=p),
			Button(text="create an acount",scale = (.5,.05),parent=p,y=-.25,x=-.15,color=color.rgba(0,0,0,0))
		]
		self.sinbtn = self.uis[7]
		self.status = self.uis[6]
		self.username = self.uis[1]
		self.password = self.uis[3]
		self.username.on_value_changed = self.check_username

	def check_username(self):
		print(self.username.text)
		df = post(f"{get_conf('url_server_1')}/username/check",json={'name':self.username.text})
		print(df.json())
		if df.json() == 1:
			self.status.text = 'username is not exists'
			self.status.color = color.red
		else:
			self.status.text = "username is valid"
			self.status.color = color.green
	def destroy(self):
		for i in self.uis:
			destroy(i)
		destroy(self)
	def main_menu(self):
		MainMenu()
		self.destroy()

