import speech_recognition as sr
from gtts import gTTS
import datetime
import requests
from bs4 import BeautifulSoup

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('response.mp3')
    print("Assistant:", text)
    # Add code to play the response.mp3 file using a media player of your choice

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

def get_date():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d")

def search_web(query):
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')
    if results:
        return results[0].get_text()
    else:
        return "No results found."

if __name__ == "__main__":
    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How can I help you today?")

        elif "time" in command:
            speak(f"The current time is {get_time()}.")

        elif "date" in command:
            speak(f"Today's date is {get_date()}.")

        elif "search" in command:
            query = command.replace("search", "").strip()
            result = search_web(query)
            speak(result)

        elif "exit" in command:
            speak("Goodbye!")
            break

        else:
            speak("I'm sorry, I didn't understand that command. Can you please repeat?")
