import json
import time
import random
from datetime import datetime
import os

# Ensure the logs directory exists
current_script_dir = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(current_script_dir, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Output log files in the current folder
SYSLOG_FILE = os.path.join(LOG_DIR, "syslog_fake.log")
SWITCHLOG_FILE = os.path.join(LOG_DIR, "switchlog_fake.log")
CONTROLLERLOG_FILE = os.path.join(LOG_DIR, "controllerlog_fake.log")



with open(  os.path.join(current_script_dir,"./data/syslog.json")) as fh:
    syslogs =  json.load(fh)
    
with open(os.path.join(current_script_dir,"./data/switchlog.json")) as fh:
    switchlogs =  json.load(fh)
    
with open(os.path.join(current_script_dir,"./data/controllerlog.json")) as fh:
    controllerlogs =  json.load(fh)
    

def main():
    index = 0
    while True:
        with open(SYSLOG_FILE, "a") as f1:
            json.dump(syslogs[index%len(syslogs)], f1)
            f1.write("\n")
        with open(SWITCHLOG_FILE, "a") as f2:
            json.dump(switchlogs[index%len(syslogs)], f2)
            f2.write("\n")
        with open(CONTROLLERLOG_FILE, "a") as f3:
            json.dump(controllerlogs[index%len(syslogs)], f3)
            f3.write("\n")
        index+=1
        time.sleep(1)

if __name__ == "__main__":
    main()
