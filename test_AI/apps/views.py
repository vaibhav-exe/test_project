from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def to_do_create(request):
    return render(request,"to_do_create.html")

def to_do_list(request):
    return render(request,"to_do_list.html")

def to_do_update(request):
    return render(request,"to_do_update.html")

def to_do_view(request):
    return render(request,"to_do_view.html")
