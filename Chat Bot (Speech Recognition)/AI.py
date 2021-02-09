import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from random import randint
import smtplib
import mycontact as mc


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendEmail(email, password, to, content,):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    server.sendmail('', to_addrs=to, msg=content)
    server.close()


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")


def takecommand():
    #It takes the input from user through microphone and returns as a string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening. . .")
        r.pause_threshold = 1
        r.energy_threshold = 550
        audio = r.listen(source)

    try:
        print("Recognizing. . .")
        query = r.recognize_google(audio_data=audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please!")
        return "None"
    return query


if __name__ == '__main__':
    greet()
    while True:
        query = takecommand().lower()
        if "who are you" in query:
            speak("I am your AI. How's it going Homie? I will try to help you!")

        elif "hello" in query or "hi" in query:
            speak("Hello, NIce to meet you!")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia,")
            print(results)
            speak(results)
            break

        elif "speak" in query:
            query = query.replace("speak", "")
            speak(query)

        elif "open youtube" in query:
            speak("opening youtube..")
            webbrowser.open("https://www.youtube.com/")
            break

        elif "open google" in query:
            speak("opening google..")
            webbrowser.open("https://www.google.com/")
            break

        elif "open coursera" in query:
            speak("opening coursera..")
            webbrowser.open("https://www.coursera.org/")
            break

        elif "play music" in query:
            speak("Playing music")
            music_dir = "D:\\Music\\Bass_Culture_2_-_Tracks_1-15"
            songs = os.listdir(music_dir)
            print(songs)
            random_intger = randint(0, len(songs) - 1)
            os.startfile(os.path.join(music_dir, songs[random_intger]))
            break

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open visual studio" in query:
            vs_path = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(vs_path)

        elif "send mail" in query or "send email" in query:
            speak("to whom you want to send email")
            to = takecommand().lower()
            if to in mc.Contacts.keys():
                to = mc.Contacts[to].email
            else:
                speak("did not caught that, enter name manually")
                to = input("contact: ").lower()
                if to in mc.Contacts:
                    to = mc.Contacts[to].email
                else:
                    speak("The contact does not exists. Enter the email")
                    email_id = input("To: ")
            speak("What you want to say")
            content = takecommand()
            try:
                speak("Please Enter the email Id and password to proceed.")
                email_id = input("Email ID: ")
                password = input("password: ")
                sendEmail(email_id, password, to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Error: I am unable to sent email")


        elif query in ["quit", "exit", "shut down", "close"]:
            speak("Shutting down. . Take care sir!")
            break


        elif query == "code 7":
            speak("Code seven activated. AI version: 0.1, speech version Beta. Entering Master Control.")
            speak("Hello my maker. Lord Tejas, How is it going? It's Nice to meet you again.")
            speak("Got any new upgrade for me Master?")
            if "yes" in takecommand().lower():
                speak("I am happy. can't wait to get updated!")
                speak("Shutting down AI for new upgrade.")
                break
            else:
                speak("Maybe Next time, how may i help you master?")