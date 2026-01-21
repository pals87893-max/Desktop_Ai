
import win32com.client as win32
import speech_recognition as sr
import os
import AppOpener as app
from groq import Groq
import datetime
import webbrowser

r=sr.Recognizer()
m=sr.Microphone()

#Block of code for Voice output
def speak(text):
    speaker = win32.Dispatch("SAPI.SpVoice")
    voices = speaker.GetVoices()
    speaker.Voice=voices.Item(1)
    speaker.Speak(f"{text}")

#Block of code for getting responce
def chat(prompt):

    client = Groq(api_key="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")
    completion = client.chat.completions.create(
    model="groq/compound",
    messages=[
        {
            "role": "user",
            "content": f"{prompt}"
        }
    ]
)
    return(completion.choices[0].message.content)

#Block of codes for command prompts
def command(prompts):
    result=""
    client = Groq(api_key="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")
    completion = client.chat.completions.create(
    model="groq/compound",
    messages=[
        {
            "role": "user",
            "content": f"{prompts}"
        }
    ]
)
    # print(completion.choices[0].message.content)
    result+=completion.choices[0].message.content
    if not os.path.exists("response"):
        os.mkdir("response")
    with open(f'response/{text.split('hey')}.txt','w',encoding='utf-8') as f:
        f.write(result)


#Block of code for oppenning Applications
def Open_App(application):
    speak(f"openning {application[5:]}")
    app.open(application, match_closest=True)

#Block of code for Time
def GetTime():
    now=datetime.datetime.now()
    timestamp= now.strftime("%H:%M:%S")
    return timestamp

#Block of code for web app opening
def websearch(i):
    url=[["youtube","https://www.youtube.com/"],
    ["instagram","https://www.instagram.com/"],
    ["discord","https://discord.com/channels/@me"],
    ["hianime","https://hianime.do/home"]]
    for url in url:
        if f"search {url[0]}" in i:
            speak(f"Openning {url[0]}",)
            webbrowser.open(f"{url[1]}")

#Start
speak("Hello I am Lisaara")

#loop
while True:
    #Block of code for voice input
    try:
        with m as mic:
            print("Listenning....")
            r.energy_threshold=300
            audio= r.listen(mic, timeout=3)
            print("Done!")
            text=r.recognize_google(audio, language='en-in')
            text=text.lower()
    except sr.UnknownValueError:
        print("Sorry, i did not understand that")
        continue
    except sr.WaitTimeoutError:
        text=""

    #Block of code for taking inputs
    if "open" in text:
        print(Open_App(text))
    
    elif "time" in text:
        res=GetTime()
        speak(res)

    elif "search" in text:
        websearch(text)

    elif text=="stop" or  text=="":
        break

    elif "hey" in text:
        command(text)
    else:
        response=chat(text)
        speak(response)
