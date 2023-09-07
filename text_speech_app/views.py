# text_speech_app/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'text_speech_app/index.html')
"text_speech_app\index.html"