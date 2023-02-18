from django import forms
from app.models import *

class student(forms.Form):
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()
    email=forms.EmailField()


class emp(forms.Form):
    empno=forms.IntegerField()
    ename=forms.CharField(max_length=20)
    job=forms.CharField(max_length=30)



