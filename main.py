import tkinter
import customtkinter
import translators as ts
import translators.server as tss
from random_word import RandomWords
from gtts import gTTS
from playsound import playsound
import random
import os

r = RandomWords()

# Return a single random word
word = r.get_random_word()

score = 0

correct = 0

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x600")
app.title("Vocab Training") 

#Text
title = customtkinter.CTkLabel(master=app, text="Vocab Training", font=("TH SarabunPSK",40))
title.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
title2 = customtkinter.CTkLabel(master=app, text="สร้างโดย จรณะ สุขโรจน์", font=("TH SarabunPSK",28))
title2.place(relx=0.5, rely=0.26, anchor=customtkinter.CENTER)
title3 = customtkinter.CTkLabel(master=app, text="วิธีการเล่นเพียงตอบคำแปลของคำด้านล่างนี้ให้ถูกต้อง", font=("TH SarabunPSK",18), text_color=("#ff2323"))
title3.place(relx=0.5, rely=0.33, anchor=customtkinter.CENTER)
scoretxt = customtkinter.CTkLabel(master=app, text="คะแนน : 0", font=("TH SarabunPSK",20), text_color=("#ff9900"))
scoretxt.place(relx=0.5, rely=0.41, anchor=customtkinter.CENTER)
transtext = customtkinter.CTkLabel(master=app, text="N/A", font=("TH SarabunPSK",30))
transtext.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
transtext.configure(text=word)

def btn_fun1():
    global correct
    global score
    global scoretxt
    if (correct == 1):
        correct = 0
        score = score + 1
        scoretxt.configure(text="คะแนน : "+str(score))
    renew()

def btn_fun2():
    global correct
    global score
    global scoretxt
    if (correct == 2):
        correct = 0
        score = score + 1
        scoretxt.configure(text="คะแนน : "+str(score))
    renew()

def sound_fun():
    audio = gTTS(text=word, lang="en", slow=True)
    audio.save("example.mp3")
    playsound("example.mp3")


# Use CTkButton instead of tkinter Button
button1 = customtkinter.CTkButton(master=app, text="Choice1", command=btn_fun1)
button1.place(relx=0.2, rely=0.7, anchor=tkinter.CENTER)
button2 = customtkinter.CTkButton(master=app, text="Choice2", command=btn_fun2)
button2.place(relx=0.8, rely=0.7, anchor=tkinter.CENTER)
soundplay = customtkinter.CTkButton(master=app, text="🔊", command=sound_fun)
soundplay.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

if (random.randint(1, 2) == "1"):
    button1.configure(text=tss.google(word, 'en', 'th'))
    button2.configure(text=tss.google(r.get_random_word(), 'en', 'th'))
    correct = 1
else:
    button2.configure(text=tss.google(word, 'en', 'th'))
    button1.configure(text=tss.google(r.get_random_word(), 'en', 'th'))
    correct = 2

def renew():
    global button1
    global button2
    global correct
    global word
    global transtext
    
    word = r.get_random_word()
    transtext.configure(text=word)
    if (random.randint(1, 2) == "1"):
        button1.configure(text=tss.google(word, 'en', 'th'))
        button2.configure(text=tss.google(r.get_random_word(), 'en', 'th'))
        correct = 1
    else:
        button2.configure(text=tss.google(word, 'en', 'th'))
        button1.configure(text=tss.google(r.get_random_word(), 'en', 'th'))
        correct = 2

app.mainloop()