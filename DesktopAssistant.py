print(__name__)
from bs4 import BeautifulSoup
from matplotlib.pyplot import pause
# from bs4.element import whitespace_re
import requests
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import calendar
import pywhatkit

import time                                 # it is for 
import webbrowser as web
from typing import Optional                    # whatsapp
from urllib.parse import quote                    
import pyautogui as pg                              # message
from pywhatkit.core import core, exceptions, log          # and we have taken it from pywhatkit library

from selenium import webdriver
import smtplib

import os
# from translate import Translator
# from gtts import gTTS
# from pygame import mixer
import cv2
import random
from PIL import Image
import numpy as np



# engine=pyttsx3.init("sapi5")
engine=pyttsx3.init("espeak")
voices=engine.getProperty("voices")
# print(voices[0].id)
# print(voices[1].id)
try:
    engine.setProperty("voice",voices[33].id)
except Exception as e:
    engine.setProperty("voice",voices[11].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")
    else:
        speak("Good evening sir")
    
    speak("How can I help")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=2
        audio=r.listen(source)
    
    try:
        print("Recognising......")
        query=r.recognize_google(audio,language="en-in")
        print(f"You said: {query}")

    except Exception as e:
        print("Say that again please")
        speak("Say that again please")
        return "None"

    return query


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
def weather(city):
    city=city.replace(" ","+")
    res=requests.get(f"https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j04j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8",headers=headers)
    print("Searching.....\n")
    soup=BeautifulSoup(res.text,"html.parser")
    location=soup.select("#wob_loc")[0].getText().strip()
    time=soup.select("#wob_dts")[0].getText().strip()
    
    info=soup.select("#wob_dc")[0].getText().strip()
    weather=soup.select("#wob_tm")[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather+" degree C")
    location=location.replace(", "," ")
    speak(f"Weather at location {location} is {info}.")
    speak(f"And the temperature is {weather} degree celsius")

def tell_date_time(query):
    min=str(datetime.datetime.now().minute)
    hour=str(datetime.datetime.now().hour)
    sec=datetime.datetime.now().second
    year=datetime.datetime.now().year
    mon_num=datetime.datetime.now().month
    mon=str(calendar.month_name[mon_num])
    day=str(datetime.datetime.now().day)
    print("\nDate and Time: ",datetime.datetime.now())
    if "date" in query and "time" in query:
        speak(f"It is {day} of {mon} of year {year}")
        speak(f"And time is {hour} hours {min} minutes and {sec} seconds")
    elif "time" in query:
        speak(f"Time is {hour} hours {min} minutes and {sec} seconds")
    elif "date" in query:
        speak(f"It is {day} of {mon} of year {year}")

def whatsapp_mess(name,message):
    contacts={"rohit rawat":"+918295977760","subal bhat":"+916006832783","rishu rawat":"+918950413124","anubhav":"+919467951557","surendra":"+919728667385"}
    try:
        pg.FAILSAFE = False
        core.check_connection()
        sendwhatmsg_instantly(contacts[name],message,5,True,4
        )
        # pywhatkit.sendwhatmsg(contacts[name], message, hr, mi,7,True,4)
        speak(f"message has sent to {name}")
    except Exception as e:
        print("\nUnable to send message")
        speak("Task failed")
        speak("I am going to try once again")
        if True:
            whatsapp_mess(name,message)


# rahul
def sendwhatmsg_instantly(
    phone_no: str,
    message: str,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3,
) -> None:
    """Send WhatsApp Message Instantly"""

    if not core.check_number(number=phone_no):
        raise exceptions.CountryCodeException("Country Code Missing in Phone Number!")

    web.open(f"https://web.whatsapp.com/send?phone={phone_no}&text={quote(message)}")
    time.sleep(7)
    pg.click(core.WIDTH / 2, core.HEIGHT / 2)
    time.sleep(wait_time - 4)
    pg.press("enter")
    log.log_message(_time=time.localtime(), receiver=phone_no, message=message)
    if tab_close:
        core.close_tab(wait_time=close_time)

def email_fun(name,message):
    contacts={"rohit rawat":"mightyrawat75@gmail.com"}
    s=smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login("rrgrawat00@gmail.com","**** **** **** ****")
    email_id=contacts[name]
    s.sendmail('&&&&&&&&&&&',email_id,message)


  

# if __name__=="Friday":
if __name__=="__main__":
    speak("Hello Sir")
    wishMe()
    while True:
        query=takeCommand().lower()
        if ("shut down" in query or "shutdown" in query or "turn off" in query or "go offline" in query) and "friday" in query:
            speak("OK sir, i am going offline")
            speak("Take care")
            break
        
        elif "wait for" in query and ("minute" in query or "second" in query):
            ind=int(query.index("for")+4)
            last=ind
            while query[last]!=" ":
                last+=1
            if "minute" in query:
                tim=float(query[ind:last])*60
            elif "second" in query:
                tim=float(query[ind:last])
            speak("ok sir")
            time.sleep(tim-9)
            speak(" 10,, 9 ,, 8 ,, 7 ,, 6 ,, 5 ,, 4 ,, 3 ,, 2 ,, 1 ,, Now i am online")

        elif "close" in query and "tab" in query:
            core.close_tab(1)
        elif "close" in query and "window" in query:
            pg.click(core.WIDTH, core.HEIGHT/406)
        
        elif "your name" in query and ("tell" in query or "what" in query) or "who are you" in query:
            speak("My name is Friday and I am your desktop assistant")       

        elif "current time" in query or "time now" in query or "date today" in query or (("time" in query or "date" in query) and "tell" in query):
            tell_date_time(query)
            

        elif ("weather at" in query) or ("weather in" in query) or ("weather of" in query):
            ind=int(query.index("weather") + 11)
            last=ind
            while True:
                if last==len(query):
                    break
                # elif query[last]==" ":
                #     break
                last+=1
            city=query[ind:last]
            city = city+" weather"
            weather(city)
        
        elif ("search" in query and "wikipedia" in query) and  ("about" in query or "that" in query) :
            if "that" in query:
                ind=int(query.index("that")+5)
            elif "about" in query:
                ind=int(query.index("about")+6)  

            print("Searching wikipedia.....")
            try:
                results=wikipedia.summary(query[ind:],sentences=1)
                print("According to wikipedia")
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print("No match found related to",query)
                speak(f"No match found related to {query} ")

        elif "whatsapp" in query and ("message" in query or "text" in query):
            ind=int(query.index("to")+3)
            last=ind
            while last!=len(query):
                last+=1    
            name=query[ind:last]
            speak(f"ok sir. what is the message for {name}")
            message="none"
            while message=="none":
                message=takeCommand().lower()
            # hr=int(datetime.datetime.now().hour)
            # mi=int(datetime.datetime.now().minute +1)
            whatsapp_mess(name,message)

        elif "send" in query and "email" in query:
            ind=int(query.index("to")+3)
            last=ind
            while last!=len(query):
                last+=1    
            name=query[ind:last]
            speak(f"ok sir. what do you want to write in the email for {name}")
            message="none"
            while message=="none":
                message=takeCommand().lower()
            while True:
                try:
                    pg.FAILSAFE = False
                    core.check_connection()
                    email_fun(name,message)
                    speak(f"email has sent to {name}")
                    break
                except Exception as e:
                    print("\nUnable to send email")
                    speak("Task failed")
                    speak("I am going to try once again")

        elif "email" in query and "show" in query:
            if "sent" in query:
                web.open("https://mail.google.com/mail/u/4/#sent")
            elif "inbox" in query:
                web.open("https://mail.google.com/mail/u/4/#inbox")
            time.sleep(7)

        # elif ("search" in query and "google" in query) and  ("about" in query or "that" in query) :
        #     if "that" in query:
        #         ind=int(query.index("that")+5)
        #     else:
        #         ind=int(query.index("about")+6)

        elif "hello" in query and "friday" in query:
            speak("what do you want to search")
            # comm=takeCommand().lower()
            comm="none"
            while comm=="none":
                try:
                    comm=takeCommand().lower()
                except Exception as e:
                    speak("speak once again")
            try:
                print("serching.....")
                speak("I am serching")
                pywhatkit.search(comm)
                speak("Task done")
            except Exception as e:
                print("Task failed")
                speak("Task failed. I am going to try once again")
                pywhatkit.search(comm)

            time.sleep(5)
            speak("For how long do you want to use this window")

            tim="none"
            while tim=="none":
                try:
                    tim=takeCommand().lower()
                except Exception as e:
                    speak("speak once again")

            ind=0
            last=ind
            while tim[last]!=" ":
                last+=1
            if "minute" in tim:
                tim=float(tim[ind:last])*60
            elif "second" in tim:
                tim=float(tim[ind:last])
            speak("ok sir")
            time.sleep(tim-7)
            speak(" 10,, 9 ,, 8 ,, 7 ,, 6 ,, 5 ,, 4 ,, 3 ,, 2 ,, 1 ")
            core.close_tab(1)

                
        elif "play" in query and "on youtube" in query:
            try:
                query=query.replace("play","")
                ind=query.index("on youtube")
                if "second" in query:
                    last=query.index("second")
                    tim=query[ind+15:last-1]
                    tim=int(tim)
                if "minute" in query:
                    last=query.index("minute")
                    tim=query[ind+15:last-1]
                    tim=int(tim)*60
                tim=tim+10
                query=query[:ind-1]
                # query=query.replace("on youtube","")
                
                if "video" in query:
                    query=query.replace("video","")
                # elif "song" in query:
                #     query.replace("song","")
                print("playing....")
                pywhatkit.playonyt(query)
                time.sleep(tim)
                core.close_tab(1)

            except Exception as e:
                print("Task failed")
                speak("Task failed")
            
        elif "open chrome" in query:
            
            # driver=webdriver.Chrome(r"C:\Users\might\Downloads\chromedriver")
            d=os.getcwd()
            driver=webdriver.Chrome(rf"{d}\chromedriver")
            speak("what do you want to search")
            topic=takeCommand().lower()
            if "www" in topic:
                driver.get(f"https://{topic}")
            else:
                # topic=takeCommand().lower()
                driver.get(f"https://www.google.com/search?q={topic}")
            time.sleep(2)
            while True:
                try:
                    speak("where do you want to click now")
                    key=takeCommand().lower()
                    if "go back" in key:
                        core.close_tab(1)
                        break
                    while "capital" in key:
                        ind=int(key.index("capital")+8)
                        last=ind
                        while True:
                            if last==len(key):
                                break
                            elif key[last]==" ":
                                break
                            last+=1
                        r=key[ind:last]
                        key=key.replace(f"capital {r}",f"{r}".capitalize())
                    print(key)
                    button=driver.find_element_by_link_text(key)
                    button.click()
                    time.sleep(2)
                except Exception as e:
                    speak("Task failed. I am going to trying again")

        elif "open" in query and "code" in query:
            os.startfile(r"C:\Users\might\AppData\Local\Programs\Microsoft VS Code\Code.exe")


        elif "make" in query and "note" in query:
            speak("ok sir, tell me the note")
            note=takeCommand().lower()
            web.open(r"https://keep.google.com/u/0/")
            time.sleep(9)
            pg.write(note)
            core.close_tab(10)


        elif "translate" in query and "hindi" in query:
            speak("ok sir, i am listening")
            aud=takeCommand().lower()
            # driver=webdriver.Chrome(r"C:\Users\might\Downloads\chromedriver")
            d=os.getcwd()
            driver=webdriver.Chrome(rf"{d}\chromedriver")
            driver.get(f"https://translate.google.com/?hl=hi&sl=en&tl=hi&op=translate")
            pg.write(aud)
            time.sleep(5)
            pg.click(core.WIDTH/1.906, core.HEIGHT/1.624)
            core.close_tab(2)

        elif "open" in query and "calculator" in query:
            # os.startfile(r"C:\Users\might\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            from subprocess import call
            try:
                call(["calc.exe"])
            except Exception as e:
                os.popen("gnome-calculator")

        elif ("take" in query or "capture" in query) and "photo" in query and "friday" in query:
                camera = cv2.VideoCapture(0)
                # i=random.randint(1,10000)
                return_value, image = camera.read()
                # cv2.imwrite('opencv'+str(i)+'.png', image)
                cv2.imwrite("test.png",image)
                del(camera)               
                img=Image.open("test.png")
                img.show()
                time.sleep(3)
                img.close()

        # elif "call" in query and "friday" in query:
        elif "call" in query:
            if "to" not in query:
                ind=int(query.index("call")+5)
            else:
                ind=int(query.index("to")+3)
            last=ind
            while last!=len(query):
                last+=1    
            name=query[ind:last]
            contacts={"rohit rawat":"8295977760","subal bhat":"6006832783","rishu rawat":"8950413124","anubhav":"9467951557","surendra":"9728667385"}
            if name in contacts.keys():
                web.open(f"https://contacts.google.com/search/{contacts[name]}")
            if name not in contacts.keys():
                web.open(f"https://contacts.google.com/search/{name}")
                
            time.sleep(10)
            pg.click(core.WIDTH/2.652, core.HEIGHT/2.8)
            time.sleep(9)
            # pg.click(core.WIDTH/2.837, core.HEIGHT/1.6175)
            # time.sleep(9)
            # pg.click(core.WIDTH/1.596, core.HEIGHT/2.9)
            # time.sleep(5)
            # pg.click(core.WIDTH, core.HEIGHT/406)

        elif "join" in query and "class" in query:
            if ("digital" in query and "electronics" in query) or "de" in query:
                web.open("http://Meet.google.com/onn-betf-vnt?authuser=1&pli=1")
                time.sleep(10)
                pg.click(core.WIDTH/3.144, core.HEIGHT/1.429)
                time.sleep(1)
                pg.click(core.WIDTH/4.066, core.HEIGHT/1.429)
                time.sleep(3)
                pg.click(core.WIDTH/1.408, core.HEIGHT/1.749)
                time.sleep(5)
                break

            elif "maths" in query or "mathematics" in query:
                web.open("https://meet.google.com/pyt-gufp-nvc?authuser=1&pli=1")
                time.sleep(10)
                pg.click(core.WIDTH/3.144, core.HEIGHT/1.429)
                time.sleep(1)
                pg.click(core.WIDTH/4.066, core.HEIGHT/1.429)
                time.sleep(3)
                pg.click(core.WIDTH/1.408, core.HEIGHT/1.749)
                time.sleep(5)
                break
            
            elif "dsa" in query:
                web.open("https://meet.google.com/mnt-hbcm-zhd?authuser=1&pli=1")
                time.sleep(10)
                pg.click(core.WIDTH/3.144, core.HEIGHT/1.429)
                time.sleep(1)
                pg.click(core.WIDTH/4.066, core.HEIGHT/1.429)
                time.sleep(3)
                pg.click(core.WIDTH/1.408, core.HEIGHT/1.749)
                time.sleep(5)
                break

            elif "project" in query:
                web.open("https://meet.google.com/baa-xirc-iix?authuser=1&pli=1")
                time.sleep(10)
                pg.click(core.WIDTH/3.144, core.HEIGHT/1.429)
                time.sleep(1)
                pg.click(core.WIDTH/4.066, core.HEIGHT/1.429)
                time.sleep(3)
                pg.click(core.WIDTH/1.408, core.HEIGHT/1.749)
                time.sleep(5)
                break
            
            elif "aec" in query or ( "analog" in query and "electronics" in query ):
                web.open("https://classroom.google.com/u/1/h")
                time.sleep(10)
                pg.click(core.WIDTH/10.166, core.HEIGHT/1.257)
                time.sleep(5)
                pg.click(core.WIDTH/8.356, core.HEIGHT/1.434)
                time.sleep(10)
                pg.click(core.WIDTH/3.144, core.HEIGHT/1.429)
                time.sleep(1)
                pg.click(core.WIDTH/4.066, core.HEIGHT/1.429)
                time.sleep(3)
                pg.click(core.WIDTH/1.408, core.HEIGHT/1.749)
                time.sleep(5)
                break
        
        elif "take" in query and "screenshot" in query:
            time.sleep(3)
            speak("taking")
            # pg.keyDown("alt")
            # pg.press("z")
            # pg.keyUp("alt")
            image = pg.screenshot()
            image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
            cv2.imwrite("test.png", image)
            img=Image.open("test.png")
            img.show()
            time.sleep(3)
            img.close()
            speak("task done")

        elif "open" in query and "drive" in query:
            # web.open(r"D:\Drive")
            web.open(r"/home/rahulrawatr320/Desktop/Rahul_Drive")

        else:
            speak("Command does not exit. Try again.")
        


            

            

                
