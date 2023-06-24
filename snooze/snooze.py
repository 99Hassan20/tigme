import os
from sys import argv, exit
import platform
from flask import Flask
import datetime as dt
from dont_move import dont_move

app = Flask(__name__)

def take_picture():
    datetime = get_current_datetime()
    file_path = f"~/intruders/z*ml_{datetime}.jpg"
    os.system(f"imagesnap {file_path}")

def get_current_datetime():
    now = dt.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d_%H:%M:%S");
    return formatted_date

@app.errorhandler(404)
def not_found(error):
    return "sorry can't do that" 

@app.route('/sleep')
def sleep():
    if platform.system() == 'Darwin':
        os.system("pmset displaysleepnow")
        take_picture()
    else:
        print("not macos");
    return "sleeeeping"

if __name__ == "__main__":
    error_message = f"Usage: python {__file__} [1 | 2]"
    if len(argv) != 2:
        print(error_message)
        exit()
    try:
        if int(argv[1]) == 1:
            app.run(debug=True)
        else:
            if dont_move():
                sleep()
                exit()
    except:
        print(error_message)




