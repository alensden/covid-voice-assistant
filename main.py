import urllib.request, urllib.parse, urllib.error
import json
import pyttsx3
import speech_recognition as sr
import re


# this function is for text to speech
# here 1st initialisation
# then engine says the text
# it runs and wait

#audio to string function
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            r.recognize_google(audio)
        except Exception as e:
            print("Exception:", str(e))
    return said.upper()
print(get_audio())
# TEMP CODE 

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


main_api = 'https://api.covid19api.com'
s1 = "WELCOME TO COVID STATS ! I'M KEVIN YOUR VOICE ASSISTANT\n\n"
speak(s1)
print(s1)
a = 'i will help find you the total cases,deaths,recovered cases and the active cases globally or of a specific country!'
speak(a)
print(a.upper())

req = main_api + '/summary'
t = urllib.request.urlopen(req).read()
parsed_data = json.loads(t)



def new_cases():
    s9 = "NEW CONFIRMED CASES :" + str(parsed_data['Global']['NewConfirmed'])
    print(s9)
    speak(s9)


def total_confirmed_cases():
    s10 = "TOTAL CONFIRMED CASES :" + str(parsed_data['Global']['TotalConfirmed'])
    print(s10)
    speak(s10)


def new_death():
    st1 = "NEW DEATHS :" + str(parsed_data['Global']['NewDeaths'])
    print(st1)
    speak(st1)

    speak("PLEASE RERUN FOR A SPECIFIC CONTRY ANALYSIS")


def new_recoverd_cases():
    st2 = "NEW RECOVERD CASES " + str(parsed_data['Global']['NewRecovered'])
    print(st2)
    speak(st2)


def total_recoverd_cases():
    st3 = "TOTAL RECOVERED CASES " + str(parsed_data['Global']['TotalRecovered'])
    print(st3)
    speak(st3)


print("looking through " + req + " API")
print("Recieved " + str(len(parsed_data)) + " Characters\n\n")

for x in parsed_data:
    if (x == 'Countries'):
        a = dict()
        a = parsed_data[x]
country = list()

for m1 in a:
    y1 = m1['Country'].upper()
    country.append(y1)
print("COUNTRY AVAILABLE -")
print(country,"\n")


flag = 0


total_cases = []
total_deaths = []
total_recover = []


def user_country():
    for content in a:



        #country.append(content['Country'])
        total_cases.append(content['TotalConfirmed'])
        total_deaths.append(content['TotalDeaths'])
        total_recover.append(content['TotalRecovered'])

s2 = "ENTER '1' TO REVIEW GLOBAL COVID STATS \n"+" ENTER '2' TO REVIEW SPECIFIC COUNTRY STATS\n"
speak(s2)
choice = input(s2)





if choice == '1':
    s3 = "YOU CHOOSE GLOBAL STATS!"
    speak(s3)
    new_cases()
    total_confirmed_cases()
    total_recoverd_cases()
    new_death()

else:

    user = input("ENTER THE COUNTRY eg -'India ' (CaSeSeNsItIvE)")
    user = user.upper()
    s3 = "SELECTED COUNTRY " + user
    speak(s3)
    user_country()

    for x in country:

        if x == user:
            print("FOUND! fetching details \n")
            key = country.index(x)
            s4 = 'TOTAL CASES IN ' + user.upper() + ' : ' + str(total_cases[key])
            print(s4)
            speak(s4)
            s5 = "TOTAL DEATHS IN " + user.upper() + " : " + str(total_deaths[key])
            print(s5)
            speak(s5)
            s6 = "TOTAL RECOVERED IN " + user.upper() + " : " + str(total_recover[key])
            print(s6)
            speak(s6)
            active = total_cases[key] - total_recover[key]
            s7 = "TOTAL ACTIVE CASES " + user.upper() + " : " + str(active)
            print(s7)
            speak(s7)
            print("\n")
            s8 = 'Please rerun for global analysis, byee!'
            speak(s8)
            print("CODE EXIT")


