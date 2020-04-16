from time import strftime, localtime
import time
import subprocess
import os

#settings
#military time
lightTime = 600
darkTime = 1900
lightTheme = "Breeze-Light"
darkTheme = "Breeze-Dark"
currTheme = 2 #0 = light; 1 = dark;

def log(input): #function for writing to log file (write append)
    log = open(os.getcwd() + '/log.txt', 'a')
    log.write(strftime("%d %b %Y %H:%M:%S - ", time.localtime()) + input + '\n')
    log.close()

log("initializing")

#Loop used to constantly check if a proper time has been met with the if statements.
#Wait commands are used so the script isn't checking every possible tick.
while True:
    if (int(strftime("%H%M", time.localtime())) < darkTime and int(strftime("%H%M", time.localtime())) > lightTime): #switches between dark and light theme depending on the time and only if it's inbetween the bounds
        if (currTheme != 0):
            subprocess.call(["lookandfeeltool", "-a", lightTheme])
            log("light theme applied")
            currTheme = 0
    else:
        if (currTheme != 1):
            subprocess.call(["lookandfeeltool", "-a", darkTheme])
            log("dark theme applied")
            currTheme = 1

    if (lightTime % 100 == 0 and darkTime % 100 == 0): #this only makes sense if there are only hours in the times
        if (int(strftime("%H%M", time.localtime())) % 100 != 0): #wait until time is in the next hour to check so it can check every hour
            log("waiting " + str(60 - (int(strftime("%H%M", time.localtime())) % 100)) + " minutes")
            time.sleep((60 - int(strftime("%H%M", time.localtime())) % 100)*60)
            continue
        else:
            log("waiting an hour")
            time.sleep(3600)

    if (lightTime % 100 != 0 or darkTime % 100 != 0): #executed if the time shifts aren't devisible by an hour
        log("waiting 5 minutes")
        time.sleep(300)

