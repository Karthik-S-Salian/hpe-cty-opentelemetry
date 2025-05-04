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

SEVERITY_LEVELS = ["debug", "info", "notice", "warning", "error", "critical", "alert", "emergency"]
USERNAMES = ["root", "admin", "user1", "karthik", "monitor", "sysadmin"]
HOSTNAMES = ["antero-turin-1011", "antero-turin-2022", "loghost01", "debugbox", "log-analyzer"]
SERVICES = {
    "syslog": ["sshd", "systemd", "systemd-logind", "rsyslogd", "cron"],
    "switchlog": ["pimd", "lldpd", "snmpd", "stpd"],
    "controllerlog": ["hmfused", "ctlmgr", "eventproc", "nodewatch"]
}

def generate_syslog():
    severity = random.choice(SEVERITY_LEVELS)
    body_options = [
        f"Accepted publickey for {random.choice(USERNAMES)} from 172.23.0.{random.randint(1, 254)} port {random.randint(30000, 60000)} ssh2: RSA SHA256:FAKEKEY",
        f"pam_unix(sshd:session): session opened for user {random.choice(USERNAMES)} by (uid=0)",
        f"Started Session {random.randint(10000, 13000)} of User {random.choice(USERNAMES)}.",
        f"New session {random.randint(10000, 13000)} of user {random.choice(USERNAMES)}.",
        f"session closed for user {random.choice(USERNAMES)}",
        f"User {random.choice(USERNAMES)} disconnected from 172.23.0.{random.randint(1, 254)} port {random.randint(20000, 60000)}"
    ]
    return {
        "Severity": severity,
        "Body": random.choice(body_options),
        "Timestamp": datetime.now().strftime("%b %d %H:%M:%S"),
        "Attributes": {
            "facility": str(random.randint(0, 23)),
            "type": "log_syslog",
            "priority": str(random.randint(10, 90))
        },
        "Resource": {
            "process_id": str(random.randint(10000, 999999)),
            "host.name": random.choice(HOSTNAMES + [f"antero-turin-{random.randint(1000, 9999)}"]),
            "service.name": random.choice(SERVICES["syslog"])
        }
    }

def generate_switchlog():
    severity = random.choice(SEVERITY_LEVELS)
    reasons = [
        "invalid IPv4 header", "TTL exceeded", "unexpected packet format",
        "packet dropped by ACL", "checksum error", "source MAC unknown"
    ]
    body = (
        f"Event|{random.randint(5000, 5200)}|LOG_WARN|{random.choice(['AMM', 'CDTR', 'BMC', 'NOC'])}|"
        f"{random.randint(1,4)}/{random.randint(1,4)}|Assert packet is discarded on interface vlan{random.randint(1, 100)}. "
        f"Reason: Dropping due to {random.choice(reasons)}"
    )
    return {
        "Severity": severity,
        "Body": body,
        "Timestamp": datetime.utcnow().isoformat() + "+00:00",
        "Attributes": {
            "priority": str(random.randint(100, 200)),
            "type": "log_switchlog",
            "facility": str(random.randint(20, 30))
        },
        "Resource": {
            "process_id": str(random.randint(1000, 5000)),
            "host.name": random.choice(["cdusw01", "sw25g1", "sw25g2", "sw-smn01", "sw-edge01"]),
            "service.name": random.choice(SERVICES["switchlog"])
        }
    }

def generate_controllerlog():
    severity = random.choice(SEVERITY_LEVELS)
    body_options = [
        f"T3: hmsfuse_read: rd_func returned 0, val: [{random.randint(1, 10**6)}]",
        f"T3: hmsfuse_read: Calling rd_func for Reading of size {random.choice([2048, 4096, 8192, 16384])}",
        f"T3: hmsfuse_read: rd_func failed with error code {random.randint(1, 5)}",
        f"T3: hmsfuse_read: timeout occurred at offset {random.randint(1000, 100000)}",
        f"T3: hmsfuse_read: read success after {random.randint(1, 10)} retries"
    ]
    return {
        "Timestamp": datetime.now().strftime("%b %d %H:%M:%S"),
        "Resource": {
            "host.name": f"x1000c4s2b{random.randint(0, 9)}",
            "service.name": random.choice(SERVICES["controllerlog"]),
            "process_id": str(random.randint(3000, 4000))
        },
        "Attributes": {
            "type": "log_controllerlog",
            "priority": str(random.randint(10, 20)),
            "facility": str(random.randint(0, 3))
        },
        "Severity": severity,
        "Body": random.choice(body_options)
    }

def main():
    while True:
        with open(SYSLOG_FILE, "a") as f1:
            json.dump(generate_syslog(), f1)
            f1.write("\n")
        with open(SWITCHLOG_FILE, "a") as f2:
            json.dump(generate_switchlog(), f2)
            f2.write("\n")
        with open(CONTROLLERLOG_FILE, "a") as f3:
            json.dump(generate_controllerlog(), f3)
            f3.write("\n")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
