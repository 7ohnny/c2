import os


class Setup:
    def __init__(self):
        self.devices = dict()
        for d in os.listdir('./bots'):
            self.devices.update({d:Bot(False,'<p></p>')})

    def loadBots(self):
        pass

    def addBot(bot):
        pass


class Bot:
    def __init__(self, online, command):
        self.id = id
        self.online = False
        self.command = ''
        self.response = ''

    def update(self,payload):
        self.online = True
        self.command = payload

setup = Setup()
#print(setup.devices.get(str(22)))
#print(list(setup.devices.keys()))
