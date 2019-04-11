import os


class Setup:
    def __init__(self):
        self.devices = dict()
        for d in os.listdir('./bots'):
            self.devices.update({d:Bot(False,'<p></p>')})


class Bot:
    def __init__(self, online, command):
        self.id = id
        self.online = online
        self.command = command
        self.response = ''

    def update(self,payload):
        self.online = True
        self.command = payload

setup = Setup()
