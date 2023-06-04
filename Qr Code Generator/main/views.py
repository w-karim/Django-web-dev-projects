from django.shortcuts import render
from .forms import QR_generator
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.conf import settings

def index(request):
    qr_image_name = ''
    form = QR_generator()
    if request.method == 'POST':
        form = QR_generator(request.POST)
        if form.is_valid():
            sentence = form.cleaned_data['Text']
            qr_image = qrcode.make(sentence)
            qr_image_name = f'{sentence}_qr_code_image.png'
            qr_image.save(settings.MEDIA_ROOT + '/' + qr_image_name) 
    context = {'form':form, 'qr_image_name' : qr_image_name}
    return render(request,"main/Home.html", context)
