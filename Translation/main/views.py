from django.shortcuts import render
from .forms import text
from textblob import TextBlob


def index(request):
    form = text()
    translated_sentence = ''
    if request.method == 'POST':
        form = text(request.POST)
        if form.is_valid():
            sentence = form.cleaned_data['Text']
            target_language = form.cleaned_data['Languages']
            blob = TextBlob(sentence)
            translated_sentence = blob.translate(from_lang = 'en', to = target_language)
    context = {'form' : form, 'translated_sentence' : translated_sentence}
    return render(request,"main/Home.html", context)
