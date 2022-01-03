# This a simple python program gave Linux user the ability to run ExpressVPN easier than ever
# It will gave you a nice systemTray icon on your system bar and will let you control your
# expressVPN connection instead of the usual traditional way on the terminal
import expressvpn
import pystray
import subprocess
from tkinter import *
from tkinter import simpledialog
import tkinter.messagebox
from PIL import Image, ImageDraw
from pystray import MenuItem as item

def run_command(command):
    return subprocess.Popen(f'expressvpn {command}',
                   shell=True,
                   stdin=subprocess.PIPE ).communicate('y\n')
def action():
    pass
# Connect to ExpressVPN
def connect():
    return run_command('connect')
# Disconnect from ExpressVPN
def disconnect():
    return run_command('disconnect')
# Quick Switch IP to avoid bands
def quickSwitch():
    pass
# Activate your account
def activate():
    # Show popup window to take the activation code from the user 
    root=Tk()
    root.withdraw()
    activationCode = simpledialog.askstring(title="Activation",
                                  prompt="Please enter your activation Code:")
    # Activate your account   
    # EYFNAUJTCEQERIRTR3SX5AF
    print(activationCode)
    return run_command(f'activate {activationCode}') 
    # subprocess.Popen(f'expressvpn activate {activationCode}',
    #                shell=True,
    #                stdin=subprocess.PIPE ).communicate('y\n')
    # expressvpn.run_command(f'expressvpn activate {activationCode}')
    # return __name__
# About me 
def about():
    tkinter.messagebox.showinfo("About US", "Created by Fowzy.")
# Exit the program
def quit():
    exit()

# Enable the app on the startup
def startup():
    pass

def systemIcon():
    image = Image.open('cwhite.png')
    menu = (item('Activate', activate), item('Connect', connect), item('Quick Switch',quickSwitch), item('Enable at Startup', startup),item('About', about), item('Quit',quit)) 
    icon = pystray.Icon("name", image, "title", menu)
    icon.run()

if __name__ == "__main__":
    # print("Hello", USER_INP)
    activationCode = str()
    print(activationCode)
    systemIcon()