import string 
import random
from django.shortcuts import render
from .forms import PassGenForm




def index(request):
    form = PassGenForm()
    password = ""
    if request.method == 'POST':
        form2 = PassGenForm(request.POST)
        if form2.is_valid():
            if form2.cleaned_data['length']:
                password_length = form2.cleaned_data['length']
                letters = string.ascii_letters
                numbers = string.digits
                punctuation = "!#$%+-*@&"
                list = [letters, numbers, punctuation]
                for i in range(password_length):
                    r = random.choice(list)
                    char = random.choice(r)
                    password  += char     
    context = {'form' : form, 'password' : password}
    return render(request, "main/MainPage.html", context)



