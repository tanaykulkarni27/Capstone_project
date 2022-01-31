from django.http import JsonResponse
from django.shortcuts import render
import speech_recognition as sr
from sys import stderr
def convert():
	root = sr.Recognizer()
	root.energy_threshold = 1000
	with sr.Microphone() as SRC:
		print('LISTENING...')
		audio_data = root.listen(SRC)
		try:
			print("RECOGNIZING...")
			text = root.recognize_google(audio_data)
			return text
		except Exception as e:
			return
def home(req):
	data = dict()
	text = convert()
	if text == None:
		data['status'] = 0
		data['text'] = False
	else:
		data['status'] = 1
		data['text'] = text
	return JsonResponse(data);