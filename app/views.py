from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *

# Create your views here.
def Fbv(request):
    return HttpResponse('this is fbv')

class Cbv(View):
    def get(self,request):
        return HttpResponse('this is class BASED RETURNING A STRING')
    

def fbv_htmlpage(request):
    return render(request,'fbv_htmlpage.html')

class cbv_htmlpage(View):
    def get(self,request):
        return render(request,'cbv_htmlpage.html')
    
def fbv_htmlpagedata(request):
    d={'name':'ashu','age':23}
    return render(request,'fbv_htmlpagedata.html',d)

class cbv_htmlpagedata(View):
    def get(self,request):
        d={'name':'suresh','age':12}
        return render(request,'cbv_htmlpagedata.html',d)
    
def fbv_form(request):
    SF=student()
    d={'form':SF}
    if request.method=='POST':
        sfo=student(request.POST)
        if sfo.is_valid():
            return HttpResponse(str(sfo.cleaned_data))
    return render(request,'fbv_form.html',d)

class cbv_form(View):
    def get(self,request):
        efo=emp()
        d={'emp':efo}
        return render(request,'cbv_form.html',d)
    def post(self,request):
        sfo=emp(request.POST)
        if sfo.is_valid():
            return HttpResponse(str(sfo.cleaned_data))


