import speech_recognition as sr
import pyttsx3
import webbrowser 
import openai
import os
from config import api_key
import time
import datetime
openai.api_key = api_key
import random

chatstr = ""

def chat(query):
    global chatstr
    chatstr += f"Qasim: {query}\nAria: "
def ai(prompt):
    global chatstr
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": chatstr}
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    ai_response = response['choices'][0]['message']['content']
    say(ai_response)
    chatstr += f"{ai_response}\n"

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(f"OpenAI response for prompt: {prompt}\n*****************\n\n{chatstr}")

    return ai_response

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        r.pause_threshold = 1 # Adjust pause threshold for quicker response
        try:
            print("Listening...")
            audio = r.listen(source)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-pk")
            print(f"User said: {query}\n")
            return query
        except sr.WaitTimeoutError:
            print("Listening timed out")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error occurred: {e}")
    
    return "None"

if __name__ == '__main__':
    say("Hello Qasim , how can I help you?")
    while True:
        query = takeCommand()
        sites = [["youtube" , "https://www.youtube.com"],["wikipedia" , "https://www.wikipedia.com"],["google" , "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir... ")
                webbrowser.open(site[1])
        if "open music".lower() in query.lower():
            musicPath = r"C:\Users\SBT\Desktop\softwares\SoundChecker.MP4"
            os.startfile(musicPath)
        
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir, the time is {strfTime}")

        if "Using artificial intelligence".lower() in query.lower():
            prompt = query
            response = ai(prompt)
            print(response)
        else :
            chat(query)
            response = ai(query)
            print("chatting....")
            print(response)