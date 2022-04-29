import pyttsx3
import PyPDF2
def speak(txt):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.say(txt)
    engine.runAndWait()
def read_pdf(name):
	pass
speak("hello world")