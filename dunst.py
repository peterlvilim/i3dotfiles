#! /usr/bin/env python3
import os
import sys
import json
import time
import re

path = os.environ["HOME"] + "/.cache/i3-dunst/notifications"
strlimit = 114  # Maximum notification length (without message amount).
notifications = []


def handle_mutt(notification):
    return "Email - " + notification["summary"]


def handle_profanity(notification):
    output = notification["body"]
    output = re.split("\(win .\)", output)
    output = "Chat - " + output[0] + " - " + output[1][1:]
    return output


def handle_default(notification):
    return notification["summary"]


# Returns the full notification text.
def full_text(notification):
    if "OfflineIMAP" in notification["app"]:
        return handle_mutt(notification)
    elif "Profanity" in notification["app"]:
        return handle_profanity(notification)
    else:
        return handle_default(notification)


# Load the notification buffer.
def load_notifications():
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    if not os.path.isfile(path):
        f = open(path, "w+")
    else:
        f = open(path, "r")
    global notifications
    try:
        notifications = json.load(f)
    except:
        notifications = list()
    f.close()


# Save the notification buffer.
def save_notifications():
    f = open(path, "w")
    json.dump(notifications, f)
    f.close()


# Check if called by i3blocks.
def calledby_i3blocks():
    for k in os.environ:
        if k.startswith("BLOCK_"):
            return True
    return False


# Get the top notification.
def gettop():
    if os.environ["BLOCK_INSTANCE"] == "OLDEST":
        return 0
    elif os.environ["BLOCK_INSTANCE"] == "URGENT_OLDEST":
        for k, v in enumerate(notifications):
            if v["urgency"] == "CRITICAL":
                return k
        for k, v in enumerate(notifications):
            if v["urgency"] == "NORMAL":
                return k
        for k, v in enumerate(notifications):
            if v["urgency"] == "LOW":
                return k
    elif os.environ["BLOCK_INSTANCE"] == "NEWEST":
        return len(notifications) - 1
    elif os.environ["BLOCK_INSTANCE"] == "URGENT_NEWEST":
        for k, v in reversed(list(enumerate(notifications))):
            if v["urgency"] == "CRITICAL":
                return k
        for k, v in reversed(list(enumerate(notifications))):
            if v["urgency"] == "NORMAL":
                return k
        for k, v in reversed(list(enumerate(notifications))):
            if v["urgency"] == "LOW":
                return k
    return 0


# Append notification from arguments.
def append_notification():
    notifications.append({
        "app": sys.argv[1],
        "summary": sys.argv[2],
        "body": sys.argv[3],
        "icon": sys.argv[4],
        "urgency": sys.argv[5],
        "time": time.time(),
        "displayed_time": 0
    })
    save_notifications()


# Delete topmost notification.
def delete_top():
    notifications.pop(gettop())
    save_notifications()


def cycle_top():
    notification = notifications.pop(gettop())
    notifications.insert(0, notification)
    save_notifications()


# Delete all notifications.
def delete_all():
    notifications = []
    save_notifications()


# Print topmost notification details.
def print_notification():
    top = gettop()
    amount = ""

    if len(notifications) > 1:
        amount = "({})".format(len(notifications))
    print(full_text(notifications[top]) + amount)
    time_diff = time.time() - notifications[top]["time"]
    if time_diff > 30:
        delete_top()
    else:
        cycle_top()

if __name__ == "__main__":
    load_notifications()
    if calledby_i3blocks():
        if len(notifications) > 0:
            print_notification()
    else:
        append_notification()
        os.system("pkill -RTMIN+12 i3blocks")
    sys.exit(0)
