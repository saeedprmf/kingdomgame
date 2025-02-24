from json import dump,load

def get_conf(key):
	with open("configs.json") as file:
		configs = load(file)
		return(configs[key])
def set_conf(key,value):
	with open("configs.json") as file:
		configs = load(file)
	configs[key] = value
	with open("configs.json",mode="w") as file:
		dump(configs,file)
