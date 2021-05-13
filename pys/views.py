from django.shortcuts import render

def base(request):
    return render(request,"base.html")

def child(request):
    return render(request,"child.html")

def home(request):
    return render(request,"phome.html")

def aboutus(request):
    return render(request,"paboutus.html")

def gallary(request):
    return render(request,"pgallary.html")