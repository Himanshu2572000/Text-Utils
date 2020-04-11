# This Page Is For 'Text_Utils' Program

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Home")
    
    return render( request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    captialtext = request.POST.get('captialtext','off')
    newlineremove = request.POST.get("newlineremove",'off')
    spaceremove = request.POST.get('spaceremove','off')
    charcount = request.POST.get('charcount','off')
    # Program For Remove Punctuations
    if removepunc == "on":
        punctuations = '''!()-[]{};:'",<>./\\?@#$%+`~|^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed }
        #return render(request, 'analyze.html', params)
        djtext = analyzed
    # Program For Captialize Text
    if captialtext == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Captialize Text','analyzed_text':analyzed }
        #return render(request, 'analyze.html', params)
        djtext = analyzed
    # Program For Remove New Line
    if newlineremove == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'Remove New Line', 'analyzed_text':analyzed }
        #return render(request,'analyze.html',params)
        djtext = analyzed
    # Program For Remove Extra Space
    if spaceremove == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Remove Extra Space', 'analyzed_text':analyzed }
        #return render(request, 'analyze.html',params)
        djtext = analyzed
    # Program For Count Characters
    if charcount == 'on':
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'purpose':'Count Characters', 'analyzed_text':analyzed }
        

    if ( removepunc != "on" and captialtext != "on" and newlineremove != 'on' and spaceremove != 'on' and charcount != 'on'):
        return HttpResponse("<h3>Please,Check The Box!<h3>")
    return render(request, 'analyze.html',params)