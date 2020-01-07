from django.shortcuts import render
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import json
from django.http import JsonResponse


test = {'requestId':'/storage/2/12apap.png', 'title': 'haha', 'amount': 0}

# Create your views here.
def translate_image(request):
    return JsonResponse(test)