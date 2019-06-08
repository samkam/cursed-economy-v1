from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Curse, VoteRecord
from django.utils import timezone
import random
def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            #log user in
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})


def index(request):
    if request.method == "POST":
        prev_curse1 = request.session["toVisit"].pop(0)
        prev_curse2 = request.session["toVisit"].pop(0)
        #retrieve vote record, create if it doesn't exist

    if 'toVisit' not in request.session:
        request.session["toVisit"] = []
    if len(request.session["toVisit"]) < 2:
        curse_id_list =  list(Curse.objects.values_list('id', flat=True))
        request.session["toVisit"] += random.shuffle(curse_id_list)
    selected = False
    #check for existing objects
    curse1 = get_object_or_404(pk=request.session["toVisit"][0])
    curse2 = get_object_or_404(pk=request.session["toVisit"][1])
    #check against
    return render(request, 'curses/curse_index.html', {"curse1":curse1,"curse2":curse2})
@login_required()
def submit_curse(request):
    c = Curse(author=request.user, pub_date=timezone.now(),
              title_text=request.POST["title"],curse_text=request.POST["curse"])
    c.save()
    return HttpResponse("submitted successfully!")

def get_curse(request, curse_id):
    curse = get_object_or_404(Curse, pk=curse_id)
    return render(request, 'curses/curses.html', {"curse":curse})
    #data = serializers.serialize("json", curse)
    #return JsonResponse(data)
@login_required
def user_curses(request):
    x = Curse.objects.filter(author=request.user)
    return render(request,'curses/my_curses.html', {"curses":x})
    #return HttpResponse(x)
    pass
def get_all_curses(request):

    output = Curse.objects.values_list('id', flat=True)
    data = {"total_curses": list(output)}
    return JsonResponse(data)
# Create your views here.
