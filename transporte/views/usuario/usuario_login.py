from django.shortcuts import render
from django.http import HttpResponse

def login(request):

    usuario=""
    pwd=""
    if request.method == "POST":
        username= request.POST.get("username","").strip()
        usuario=username
        pwd=request.POST.get("password","")
        

    return render(request,'html/usuario_login.html',{'usuario':usuario,'pwd':pwd})