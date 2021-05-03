import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib
import random


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir . Please tell me how may i help you")    

def takeCommand():
    # It take microphone input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio=r.listen(source)
        

    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please....")
        return "None"
    return query    
                


def sendEmail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','yourpassword')
    server.sendmail('youremail@gmail.com',to, content)
    server.close()



if __name__=="__main__":
    Wishme()
    while True:
        query=takeCommand().lower()


        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('search wikipedia.....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        
        elif 'open google' in query:
            webbrowser.open("google.com")


        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir= 'E:\\Non Critical\\songs\\Favorite songs'
            songs=os.listdir(music_dir)
            print(songs)
            # os.startfile(os.path.join(music_dir, songs[1]))
            os.startfile(os.path.join(music_dir,random.choice(songs)))


        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")


        elif 'open code' in query:
            codepath="C:\\Users\\sharik ansari\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)


        elif 'open pycharm' in query:
            codepath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
            os.startfile(codepath)


        elif 'open video' in query:
            codepath="C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(codepath)

        elif 'open chrome' in query:
            codepath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath)

        elif 'open reader' in query:
            codepath="C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
            os.startfile(codepath)

        

        elif 'play movie' in query:
            movies_dir='F:\\Movies\\hollywood movies'
            movies=os.listdir(movies_dir)
            print(movies)
            os.startfile(os.path.join(movies_dir,random.choice(movies)))
            

        elif 'open images' in query:
            photos_dir='E:\\Photos\\mobile pic'
            photos=os.listdir(photos_dir)
            os.startfile(os.path.join(photos_dir,random.choice(photos)))


        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'random news' in query:
            codepath="C:\\Users\\sharik ansari\\exercise09.py"
            os.startfile(codepath)

        elif 'open powershell' in query:
            codepath= "C:\\Windows\\System32\\WindowsPowerShell\\v1.0"
            os.startfile(codepath)

        elif 'open notepad' in query:
            codepath="C:\\windows\\system32"
            os.startfile(codepath)

        elif ' open review' in query:
            codepath="C:\\Users\\sharik ansari\\Desktop\\code playground\\Drs Review System\\maini.py"
            os.startfile(codepath)

        elif 'open game' in query:
            codepath="C:\\Users\\sharik ansari\\Desktop\\code playground\\Flappy Bird\\main.py"
            os.startfile(codepath)

        




        


        










        elif 'email to sharik' in query:
            try:
                speak("what should i say ?")
                content=takeCommand()
                to="yourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my friend sharik bhai . i am not able to send this email")


        if 'stop' in query:
            exit()






















    


        
    



   




