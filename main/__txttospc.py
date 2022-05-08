import pyttsx3
from pathlib import Path
import PyPDF2
from django.shortcuts import HttpResponse, get_object_or_404
from .models import BOOK
from threading import Thread

BASE_DIR = Path(__file__).resolve().parent.parent
is_paused = False
cur_word = []


def pause_reading(req):
    global is_paused
    is_paused = True
    return HttpResponse('hello')


def __speakHelper(i):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.say(i)
    engine.runAndWait()


def __readPDF(__pp):
    Fileobj = open(__pp, 'rb')
    reader = PyPDF2.PdfFileReader(Fileobj)
    number_of_pages = reader.numPages
    j = 0
    while j < number_of_pages and is_paused == False:
        txt = reader.getPage(j).extractText().split()
        i = 0
        while i < len(txt) and is_paused == False:
            __speakHelper(txt[i])
            i += 1
        j += 1


def read_ppl(req, idx):
    global is_paused
    is_paused = False;
    book = get_object_or_404(BOOK, id=idx)
    book_url = str(BASE_DIR) + str(book.get_url()).replace('/', '\\')
    t = Thread(target=__readPDF, args=(book_url,))
    t.start()
    t.join()
    return HttpResponse("DONE")