import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
from my_Secrets import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import requests
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import string
import random
from nltk.tokenize import word_tokenize

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def getvoices(voice):
    voices = engine.getProperty('voices')  
    if voice == 1:
        engine.setProperty('voice', voices[0].id)
        
    if voice == 2:
        engine.setProperty('voice', voices[1].id)

    speak("hello this is jarvis")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the currect time is:")
    speak(Time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak(f"Today's date is {day} {month} {year}")
    
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("good morning sir!")
    elif hour >= 12 and hour <18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour <24:
        speak("Good evening sir!")
    else: 
        speak("Good night sir!")

def wishme():
    # time()
    # date()
    # greeting()
    speak("Jarvis at you're service, tell me how can I help you?")

def takeCommandCMD():
    query = input("Please tell me how can i help you?\n")
    return query

def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing..")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Sorry can you say that again Please..")
        return "None"
    return query

def sendEmail(reciver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = reciver
    email['subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()
    
def sendwhatsmsg(phone_no, message):
    message = message
    wb.open('https://web/whatsapp.com/send?phone='+phone_no+'&text='+message)
    sleep(10)
    pyautogui.press('enter')
    
def searchgoogle():
    speak("what should i search for?")
    search = takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)
    
def news():
    newsapi = NewsApiClient(api_key='3649a692e2c9455299e623db4e5c0f77')
    speak("what would be the topic?")
    topic = takeCommandMic()
    try:
        data = newsapi.get_top_headlines(q=topic, language='en', page_size=5)
        articles = data.get('articles', [])
        if not articles:
            print("No news articles found.")
            speak("Sorry, I could not fetch any news at the moment.")
            return
        for idx, article in enumerate(articles, 1):
            description = article.get("description", "No description available")
            print(f'{idx}: {description}')
            speak(f'News {idx}: {description}')
        speak("that's it for now")
    except Exception as e:
        print(f"Error fetching news: {e}")
        speak("Sorry, I could not fetch any news due to an error.")

def text2speech():
    text = clipboard.paste()
    print(text)
    
def screenshot():
    name_img = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    name_img =  f"D:\\Python_programming_course\\python_projects\\screenshot\\{name_img}.png"
    img = pyautogui.screenshot(name_img)
    img.show()
    
def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    speak(newpass)

def flip():
    speak("Okay sir flipping a coin")
    coin = ["heads", "tails"]
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    speak("i flipped the coin and you got"+toss)

if __name__ == "__main__":
    # wishme()
    wakeword = "jarvis"
    while True:
        query = takeCommandMic().lower()
        query = word_tokenize(query)
        print(query)
        if wakeword in query:
            if 'time' in query:
                time()
            elif 'date'in query:
                date()
            elif 'email' in query:
                email_list = {
                    'test email':'shonkalangutkar1998@gmail.com'
                }
                try:
                    speak("To whom you want to send the mail?\n")
                    name = takeCommandMic()
                    receiver = email_list[name]
                    speak("what is the subject of the mail?\n")
                    subject = takeCommandMic()
                    speak("what should i say? \n")
                    content = takeCommandMic()
                    sendEmail(receiver, subject, content)
                    speak("email has been sent")
                except Exception as e:
                    print(e)
                    speak("unable to send the email")
            elif 'message' in query:
                user_name = {
                    'Jarvis':'+91 97110 00342'
                }
                try:
                    speak("To whom you want to send the whatsapp message?\n")
                    name = takeCommandMic()
                    phone_no = user_name[name]
                    speak("what is the message?\n")
                    message = takeCommandMic()
                    sendwhatsmsg(phone_no, message)
                    speak("mesage has been sent")
                except Exception as e:
                    print(e)
                    speak("unable to send the message")
            elif 'wikipedia' in query:
                speak("searching on wikipedia..")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences = 2)
                print(result)
                speak(result)
            elif 'search' in query:
                searchgoogle()
            elif 'youtube' in query:
                speak("what should I search on youtube?")
                topic = takeCommandMic()
                pywhatkit.playonyt(topic)
            elif 'weather' in query:
                city = 'faridabad'
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=b31324cafab29df35a39ea3197650b50"
                res = requests.get(url)
                data = res.json()
                weather = data['weather'][0]['main']
                temp = data['main']['temp']
                desp = data['weather'][0]['description']
                temp = round((temp-32)* 5/9)
                print(weather)
                print(temp)
                print(desp)
                speak(f"temperature: {temp} degree")
                speak(f"weather is {weather}")
                speak(f"description: {desp}")
            elif 'news' in query:
                news()
            elif 'read' in query:
                text2speech()
            elif 'open code' in query:
                codepath = "C:\\Users\\Shon\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
                os.startfile(codepath)
            elif 'open' in query:
                os.system('explorer C://{}'.format(query.replace('open','')))
            elif 'jokes' in query:
                speak(pyjokes.get_joke())
            elif 'screenshot' in query:
                screenshot()
            elif 'remember that' in query:
                speak("what should i remember?")
                data = takeCommandMic()
                speak("you siad me to remember that"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
                
            elif 'do you know anything' in query:
                remember = open('data.txt','r')
                speak("You told me to remember that"+remember.read)    
            elif 'password' in query:
                passwordgen()
            elif 'flip' in query:
                flip()
            elif 'offline' in query:
                quit()