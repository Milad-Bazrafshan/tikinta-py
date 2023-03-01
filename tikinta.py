from email.mime import audio
import os
from pdb import Restart
from pydoc import text
from re import M
import time
from tkinter.messagebox import YES
from turtle import reset
import playsound
import speech_recognition as sr
from gtts import gTTS
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice1.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said
def write_slogan():
    text = get_audio()
    dir = "C:/Program Files/Mozilla Firefox/firefox.exe"
    photoshop = "C:/Program Files/Adobe/Adobe Photoshop 2021/photoshop.exe"
    chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    vscode = "C:/Users/Milad/AppData/Local/Programs/Microsoft VS Code/Code.exe"
    word = "C:/Program Files/Microsoft Office/root/Office16/winword.exe"
    exel = "C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE"
    access = "C:/Program Files/Microsoft Office/root/Office16/MSACCESS.EXE"
    powerpoint = "C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE"


    # for hey in text:
    #     speak("Yes, I am in service")
    #     break
    if "hello" in text:
        speak("hello Iam tkinter, how are you ?")
        write_slogan()
    elif "how are you" in text:
        speak("Thanks, i am great")
        write_slogan()
    elif "thanks" in text :
        speak("it is Good")
    elif "iam find, Whats up ?" in text:
        speak("Thanks everything is great")
    elif "what's your name" in text:
        speak("My name is bam")
    elif "please open the Firefox" in text:
        speak("ok, please wait")
        os.startfile(dir)
    elif "please open the Photo Shop" in text:
        speak("ok, please wait")
        os.startfile(photoshop)
    elif "please open the Chrome" in text:
        speak("ok, please wait")
        os.startfile(chrome)
    elif "please open the vs code" in text:
        speak("ok, please wait")
        os.startfile(vscode)
    elif "please open the word" in text:
        speak("ok, please wait")
        os.startfile(word)
    elif "please open the Excel" in text:
        speak("ok, please wait")
        os.startfile(exel)
    elif "please open the access" in text:
        speak("ok, please wait")
        os.startfile(access)
    elif "please open the PowerPoint" in text:
        speak("ok, please wait")
        os.startfile(powerpoint)
    else:
        speak("Invalid input")
        print("Invalid input")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.geometry("200x300")
style = Style()

style.configure('TButton', font =
			('calibri', 20, 'bold'),
					borderwidth = '4')
style.map('TButton', foreground = [('active', '!disabled', 'green')],
					background = [('active', 'black')])
btn1 = Button(frame,
                   text="Send Voice",
                   command=write_slogan)
btn1.grid(row = 0, column = 3, padx = 0)
root.mainloop()  
