from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import ( get_user_model,authenticate, login,logout )
from .models import BOOK ,User
import speech_recognition as sr
import json
import speech_recognition as sr
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening...')
            r.enerygy_threshold = 1000
            audio_data = r.listen(source)
            try:
                text = r.recognize_google(audio_data,language='en-in')
                return text
            except: 
                return
class SERIAL(serializers.ModelSerializer):
    class Meta:
        model = BOOK
        fields = ('__all__')
def UPLOAD(req):
    NAME = req.POST.get('bookname')
    DESCRIPTION = req.POST.get('bookdesc')
    CATEGORY = req.POST.get('category')
    LANGUAGE = req.POST.get('booklang')
    COVER_VALUE = req.FILES.get('bookimg')
    FILE_VALUE = req.FILES.get('bookfile')
    BOOK(title = NAME,desc = DESCRIPTION,category = CATEGORY,language = LANGUAGE,COVER = COVER_VALUE,DOC = FILE_VALUE).save()
    return redirect("/")
class ACT(APIView):
    # def post(self,req):
        
    def get(self,req):
        als = BOOK.objects.all()
        category = req.GET.get('category')
        inner = req.GET.get('search')
        if inner == 'everything':
            inner = None
        if category == "ALL":
            category = None
        if category != None:
            als = als.filter(category = category)
        if inner != None:
            als = als.filter(title__contains = inner)
        return Response(SERIAL(als,many = True).data)
def getout(req):    
    logout(req)
    return redirect("/")	
def LOG_IN(req):
    if req.method == "POST":
        name = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req,username = name,password = password)
        if user != None:
            login(req,user);
            return HttpResponse("done")
        else:
            return HttpResponse("username or password incorrect")
        
    assert False,"GET METHOD WILL NOT WORK"
def GET_IN(req):
    if req.method == "POST": 
        typ = req.POST.get('typ');
        USER = get_user_model()
        first_name = req.POST.get("FNAME")
        last_name = req.POST.get("LNAME")
        email = req.POST.get("EMAIL")
        username = req.POST.get("USNAME")
        password = req.POST.get("PWD")
        user = USER.objects.create_superuser(email,password,username ,phone_number,first_name,last_name,dob,gender)
        user.save()
        return redirect("/",)
 
    return render(req,'form.html');        
def FILE_UPLOAD(req):
    if req.method == "POST":
        return render(req,'upload.html');            
    return render(req,'upload.html');        

def home(req):
    all_books = BOOK.objects.all()
    context = dict()
    context['books'] = all_books
    category = req.GET.get('CAT');
    types = req.GET.get('type');
    print("DEBUG : GOT A REQUEST")
    if types:
        print("DEBUG : "+types)
    REQUEST_URL = f'/RESTAPI?format=json'
    if(category != None):
        REQUEST_URL += f'&category={category}'
    if types == 'VOICE':
        txt = listen()
        REQUEST_URL += f'&search={txt}'
    elif types == "TXT":
        txt =  req.GET.get('search')
        REQUEST_URL += f'&search={txt}'
    context['URL'] = REQUEST_URL
    context['SLC']  = category;
    return render(req,'index.html',context)