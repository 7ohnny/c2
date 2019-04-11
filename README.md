# C2_alpha

command and control via http

# Requirements

* Python 3.6
* Flask (http://flask.pocoo.org)
* Flask Auto-Index (https://pythonhosted.org/Flask-AutoIndex/)
* Cmd2 (https://cmd2.readthedocs.io/)

# Features

* Backend 
    * Directory listing
    * Upload function
    * Server commands
* Shell cmd2
    * List bots
    * Send command to the bots 
    * Se the log of the command's results

* Client side
    * Payload script POC
    
# Usage

-- POC --

python main.py
&
python payload_poc.py

![](test.gif)

    
# TODO

* Improve the logResult feature in the shell
* Handle requests with POST Method
* Encrypt data
* Screenshot
* Keylogger
* Powershell version 2 payload
* Payload .exe