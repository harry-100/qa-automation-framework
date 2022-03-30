from json import loads


def loadConfig():
	with open("config/config.json", "r") as fp:
		return loads(fp.read())
