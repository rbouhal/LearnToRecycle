from django.http import HttpResponse
from django.shortcuts import render
from subprocess import run

import sys

def run_pythonScript(request):

    run([sys.executable, 'Game.py'])



def home_page(request):
    return render(request, "gamepage.html")