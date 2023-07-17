import time
import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init()

opts = {"alias": ('роблокс'),
        "commands": {"time": ('который час', 'сколько времени', 'время'),
                     "weather": ("какая погода", "погода")}}

r = sr.Recognizer()
m = sr.Microphone(device_index=2)

with m as source:
    r.adjust_for_ambient_noise(source)

def speak(message):
    engine.say(message)
    engine.runAndWait()



def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language='ru-RU')
        print(voice)
        if voice.startswith("roblox"):
            cmd = voice[7:]
            print(cmd)


    except sr.UnknownValueError:
        print("Не пооооон")
    except sr.RequestError as e:
        print("Вообще не пон")


def commands(cmd):
    if 

#Начало
speak("Можете говорить")


stop_listening = r.listen_in_background(m, callback)
while True:
    time.sleep(0.1)

