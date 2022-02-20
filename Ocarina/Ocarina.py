import time
import bluetooth
from playsound import playsound
import webbrowser
import subprocess
import screen_brightness_control as screen
import pyautogui

passkey = "1234"
sensor_address = '00:19:12:10:04:11'
socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
socket.connect((sensor_address, 1))

notes = ["Z","Z","Z","Z","Z","Z"]

while True:
    try:
        socket.connect((sensor_address, 1))
    except:
        placeholder = 0

    output = socket.recv(1)
    output = output.decode("utf-8")

    if output in "ALRUD" and output != notes[5]:
        notes.pop(0)
        notes.append(output)

    strnotes = ''.join(notes)
    if strnotes == "LURLUR":
        print("Zelda's Lullaby") # sleep
        playsound("Zelda\'s Lullaby.wav")
        screen.set_brightness(0)
        notes = ["Z","Z","Z","Z","Z","Z"]
    elif strnotes == "ULRULR":
        print("Epona's Song") # Google Classroom + Docs + Mail
        webbrowser.open("https://classroom.google.com", new=1)
        webbrowser.open("https://mail.google.com", new=2)
        webbrowser.open("https://docs.google.com", new=2)
        playsound("Epona\'s Song.wav")
        notes = ["Z", "Z", "Z", "Z", "Z", "Z"]
    elif strnotes == "RDURDU":
        print("Sun's Song") # get out of sleep
        playsound("Sun's Song.wav")
        screen.set_brightness(100)
        notes = ["Z", "Z", "Z", "Z", "Z", "Z"]
    elif strnotes == "DRLDRL":
        print("Saria's Song") # Google
        playsound("Saria's Song.wav")
        subprocess.Popen('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
        notes = ["Z", "Z", "Z", "Z", "Z", "Z"]
    elif strnotes == "RADRAD":
        print("Song of Time") # pause song
        playsound("Song of Time.wav")
        pyautogui.press("playpause")
        notes = ["Z", "Z", "Z", "Z", "Z", "Z"]
    elif strnotes == "ADUADU":
        print("Song of Storms") # Spotify
        playsound("Song of Storms.wav")
        subprocess.Popen('C:\\Users\\91959\\AppData\\Roaming\\Spotify\\Spotify.exe')
        notes = ["Z", "Z", "Z", "Z", "Z", "Z"]

    time.sleep(0.05)