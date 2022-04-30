from io import StringIO
from urllib.request import urlopen, Request
# from StringIO import StringIO
import pyttsx3
from pathlib import Path
import PyPDF2
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import ( get_user_model,authenticate, login,logout )
from .models import BOOK , User , Cart
from threading import Thread
BASE_DIR = Path(__file__).resolve().parent.parent
is_paused = False
def pause_reading(req):
	global is_paused
	is_paused = True
	return HttpResponse('hello')
def speak(txt):
	global is_paused
	engine = pyttsx3.init('sapi5')
	voices = engine.getProperty('voices')
	engine.setProperty('voices', voices[0].id)
	for i in txt.split():
		if is_paused == False:
			engine.say(i)
		else:
			break;
	engine.runAndWait()
def read_this_pdf(name_of_pdf):
    Fileobj = open(name_of_pdf,'rb')
    reader = PyPDF2.PdfFileReader(Fileobj)
    number_of_pages = reader.numPages
    for i in range(number_of_pages):
    	speak(reader.getPage(i).extractText())
def read_ppl(req,id):
	global is_paused
	is_paused = False;
	book = get_object_or_404(BOOK,id = id)
	book_url = str(BASE_DIR) + str(book.get_url()).replace('/','\\')
	t = Thread(target = read_this_pdf,args=(book_url,))
	t.start()
	t.join()
	return HttpResponse("DONE")
