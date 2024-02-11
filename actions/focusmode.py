import time
import datetime
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
if is_admin:
    currentTime = datetime.datetime.now().strftime("%H:%M")
    stopTime = input("Enter Time as [HH:MM] :-")
    a = currentTime.replace(":", ".")
    a = float(a)
    b = stopTime.replace(":", ".")
    b = float(b)
    focusTime = b - a
    focusTime = round(focusTime, 3)

    hostPath = "C:\Windows\System32\drivers\etc\hosts"
    redirect = "127.0.0.1"

    print(currentTime)

    websites = [
        "www.facebook.com",
        "facebook.com",
        "www.instagram.com",
        "instagram.com",
        "www.youtube.com",
        "youtube.com"
    ]

    if (currentTime < stopTime):
        with open(hostPath, "r+") as file: # r+ = writing and reading
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(f"{redirect} {website}")
                    print(f" {website} Done")
            print("Website are blocked!, Entering Focus mode")
            file.close()
    while True:
        currentTime = datetime.datetime.now().strftime("%H:%M")
        websites = [
        "www.facebook.com",
        "facebook.com",
        "www.instagram.com",
        "instagram.com",
        "www.youtube.com",
        "youtube.com"
    ]
        if (currentTime >= stopTime):
            with open(hostPath, "r+") as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in websites):
                        file.write(line)
                file.truncate()
                print("Websites unblocked")
                file = open("focus.txt", "a")
                file.write(f",{focusTime}")
                file.close()
                break

else:
    # This will try to run as administrator and ask for the passsword
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, -1)