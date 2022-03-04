#I have created this webiste - Suriya
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('mytext','default')
    analysed = ''
    purpose=''
    if 'removepunc' in request.POST:
        purpose='Remove Punctuation ,'
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analysed=analysed+char
    if 'fullcaps' in request.POST:
        purpose = purpose+'capitalize ,'
        if analysed!='':
            analysed=analysed.upper()
        else:
            analysed = djtext.upper()

    if 'spaceremover' in request.POST:
        purpose = purpose+'Space Remover '
        if analysed!='':
            analysed = analysed.replace(" ", "")
        else:
            analysed = djtext.replace(" ", "")
    params={'purpose':purpose,'analysed_text':analysed}
    return render(request,'analyse.html',params)
