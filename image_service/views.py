from django.shortcuts import render
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from io import StringIO


test = {'requestId':'/storage/2/12apap.png', 'title': 'haha', 'amount': 0}

request = {'requestId':'/storage/2/12apap.png', 'image': 'haha'}

@csrf_exempt
def index(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        ocr_result = do_ocr(body['image'])
        print("OCR RESULT")
        print(ocr_result)
        map_result = map_to_transaction(ocr_result)
    return JsonResponse(test)

def map_to_transaction(ocrResult):
    return None

def do_ocr(image):
    imgstring = image.split('base64,')[-1].strip()
    image_string = StringIO(base64.b64decode(imgstring))
    image = Image.open(image_string)
    
    # Overlay on white background, see http://stackoverflow.com/a/7911663/1703216
    bg = Image.new("RGB", image.size, (255,255,255))
    bg.paste(image,image)

    return pytesseract.image_to_string(bg)