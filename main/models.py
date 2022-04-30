import os
from pathlib import Path
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager ,PermissionsMixin
)
class UserManager(BaseUserManager):
    def create_user(self,email = "",password = "",username = "",firstname = "",lastname="",is_staff = True,is_active = True,is_admin = False):
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.firstname = firstname
        user_obj.lastname = lastname
        user_obj.username = username
        user_obj.active = is_active
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_admin
        user_obj.save(using = self._db)
        return user_obj
    def create_superuser(self,email = "",password = "",username = "",firstname="",lastname=""):
        user_obj = self.create_user(email,password,username,firstname,lastname,True,True,True)
        return user_obj
class User(AbstractBaseUser):
    firstname = models.TextField(max_length = 255,unique = False,default = "")
    lastname = models.TextField(max_length = 255,unique = False,default = "")
    username = models.TextField(max_length = 255,unique = True,default = "")
    email = models.EmailField(max_length = 255,unique = True,default = "tanay@gmail.com")
    is_staff = models.BooleanField(default = True)
    active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname','lastname','email']
    objects = UserManager()
    def has_perm(self,perm,obj = None):
        return True
    def has_module_perms(self,app_label):
        return True
    def __str__(self):
        return self.email
    def get_fname(self):
        return self.firstname
    def get_lname(self):
        return self.lastname
    def get_username(self):
        return self.username
    def is_admin(self):
        return self.is_superuser
    def is_active(self):
        return self.active
def get_new_dir():
    BASE_DIR = str(Path().parent.resolve()).replace('\\','/')
    pathss = 'MEDIA'
    tmp = -1
    with open(BASE_DIR + '/num.txt','r') as f:
        pathss += '/'+f.read()
        try:
            tmp = int(f.read())
        except:
            pass
    with open(BASE_DIR + '/num.txt','w') as f:
        f.write(str(tmp + 1))
    return pathss
class BOOK(models.Model):
    title = models.TextField();
    desc = models.TextField(default = "");
    category = models.TextField(default = "");
    language = models.TextField(default = "");
    DIRSS = get_new_dir()
    COVER = models.FileField(upload_to = DIRSS,unique = False);
    DOC = models.FileField(upload_to = DIRSS,unique = False);
    def create_book(self,TITLE,DESC,CATEGORY,LANGUAGE,DOC):
        book_obj = self.model()
        book_obj.title = TITLE
        book_obj.desc = DESC
        book_obj.category = CATEGORY
        book_obj.language = LANGUAGE
        book_obj.DOC = DOC
        book_obj.save()
    def get_url(self):
        return self.DOC.url
    def __str__(self):
        return self.title
    def get_pdf(self):
        return self.DOC
class Cart(models.Model):
    books = models.ForeignKey(BOOK , default = '' , on_delete = models.CASCADE)
    user_ids = models.ForeignKey(User , default = '' , on_delete = models.CASCADE)