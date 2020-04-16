from time import strftime, localtime
import time
import subprocess

#military time
lightTime = 600
darkTime = 1730
lightThemeGTK = "Mojave-light"
lightWallpaper = "/home/avery/Pictures/Wallpapers/10-13.jpg"
darkThemeGTK = "Mojave-dark"
darkWallpaper = "/home/avery/Pictures/Wallpapers/10-15-7-Dusk.jpg"
monitor = "DVI-D-0"

#settings
applyGTK = 1
applyWall = 0
applyBrghnss = 1
darkBrghnss = 0.75

def log(input): #function for writing to log file (write append)
    log = open('/home/avery-pc/Dropbox/PROGRAMMING/PYTHON/log.txt', 'a')
    log.write(strftime("%d %b %Y %H:%M:%S - ", time.localtime()) + input + '\n')
    log.close()

log("initializing")

def checkGTK(): #checks which theme is applied
    cur_GTK = str(subprocess.check_output(["gsettings", "get", "org.gnome.desktop.interface", "gtk-theme"]))
    if (darkThemeGTK in cur_GTK):
        return 0
    elif (lightThemeGTK in cur_GTK):
        return 1
    else: return None

def lightThemeSwitch():
    if (applyGTK): subprocess.call(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", lightThemeGTK]) #acts as if the command was typed in a terminal and only executed if the setting for it is true
    if (applyWall): subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", lightWallpaper]) 
    if (applyBrghnss): subprocess.call(["xrandr","--output",monitor,"--brightness", "1"])
    log("light theme applied")


def darkThemeSwitch(): #used to 
    if (applyGTK): subprocess.call(["gsettings", "set", "org.gnome.desktop.interface", "gtk-theme", darkThemeGTK])
    if (applyWall): subprocess.call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", darkWallpaper])
    if (applyBrghnss): subprocess.call(["xrandr","--output",monitor,"--brightness", str(darkBrghnss)])
    log("dark theme applied")

#Loop used to constantly check if a proper time has been met with the if statements.
#Wait commands are used so the script isn't checking every possible tick.
while True:
    if (int(strftime("%H%M", time.localtime())) < darkTime and int(strftime("%H%M", time.localtime())) > lightTime): #switches between dark and light theme depending on the time and only if it's inbetween the bounds
        if (checkGTK() == 0): #checks if another theme is applied. if yes, then execute the function. if no, don't apply the same theme again.
            lightThemeSwitch()
    else:
        if (checkGTK() == 1):
            darkThemeSwitch()

    if (lightTime % 100 == 0 and darkTime % 100 == 0): #this only makes sense if there are only hours in the times
        if (int(strftime("%H%M", time.localtime())) % 100 != 0): #wait until time is in the next hour to check so it can check every hour
            log("waiting " + str(60 - (int(strftime("%H%M", time.localtime())) % 100)) + " minutes")
            time.sleep((60 - int(strftime("%H%M", time.localtime())) % 100)*60)
            continue
        else:
            log("waiting an hour")
            time.sleep(3600)

    if (lightTime % 100 != 0 or darkTime % 100 != 0):
        log("waiting 5 minutes")
        time.sleep(300)

