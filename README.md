# AutoThemeSwitcher 0.1
Built with Python 3.8.

# Usage
To be able to tune the settings to your desires you have to edit the file that is needed for your desktop enviroment.
Set the time (military time) and theme folder location with the variables at the top of the script.
A log file will be added to the directory of the script with timestamps, when changes happen and wait times.
Initialize the file at system startup with python3 and the directory of that file.

# Differences
Gnome has more features than the Cinnamon or KDE version like:
* X-org brightness control(disable/enable) - requires to change string "monitor" to your specific monitor. 
* Wallpaper control(disable/enable) - requires to change path to desired wallpaper for light and dark theme.
