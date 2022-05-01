from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth import ( get_user_model,authenticate, login,logout )
from .models import BOOK , User , Cart
import speech_recognition as sr
from pathlib import Path
import json
import speech_recognition as sr
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#favourite page code
def __favourite(req):
    return render(req,'favourite.html')
#Restapi for Cart
class CC(serializers.ModelSerializer): # serializer class for cart
    class Meta:
        model = Cart
        fields = ('__all__') 
class __API(APIView): # api for cart 
    def get(self,req):
        __user = req.user.id
        als = Cart.objects.all().filter(user_ids = __user)
        return Response(CC(als,many = True).data)
def remove_book(req,book_id):
    user_id = req.user.id
    x = get_object_or_404(Cart,books = book_id,user_ids = user_id)
    x.delete();
    return HttpResponse('done')
def save_book(req,book_id):
    user_id = req.user.id
    try:
        x = get_object_or_404(Cart,books = book_id,user_ids = user_id)
    except:
        pp = Cart()
        pp.books = get_object_or_404(BOOK,id = book_id)
        pp.user_ids = req.user
        pp.save()
    return HttpResponse('done')
def __detailed(req,id):
    BASE_DIR = Path(__file__).resolve().parent.parent
    x = get_object_or_404(BOOK,id = id)
    assert x,"ROW NOT FOUND";
    context = dict()
    context['in_fav'] = -1
    if len(Cart.objects.all().filter(books = id,user_ids = req.user.id)) <= 0:
        context['in_fav'] = 1
    book_url = str(BASE_DIR).replace('\\','/') + str(x.get_url())
    context['PDF'] = book_url
    context['image_url'] = x.COVER;
    context['title'] = x.title;
    context['desc'] = x.desc;
    context['cate'] = x.category
    context['book_url'] = x.DOC
    context['id'] = id
    return render(req,'DETAILS.html',context)

def view_grid(req):
    if req.user.is_authenticated:
        return render(req,'urlel.html')
    return redirect('/')

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
    def get(self,req):
        als = BOOK.objects.all()
        category = req.GET.get('category')
        inner = req.GET.get('search')
        idss = req.GET.get('id')
        if inner == 'everything':
            inner = None
        if category == "ALL":
            category = None
        if category != None:
            als = als.filter(category = category)
        if inner != None:
            als = als.filter(title__contains = inner)
        if idss != None:
            als = als.filter(id = idss)
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
