from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse
from django.db.models import Count, F, Q
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.forms.models import model_to_dict
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully as {username}")
                return redirect('home')
            else:
                messages.info(request,"User dosn't exist")
        else:
            messages.info(request,"Invalid Syntaxe")
    form = AuthenticationForm()
    redirect('home')
    return render(request,"login.html", {"form":form})


def index(request):
    return render(request,"index.html")



