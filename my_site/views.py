# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    print(djtext)
    removepunc = request.GET.get('removepunc', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for x in djtext:
            bool = False
            for y in punctuations:
                if(x == y):
                    bool = True
            if(bool == True):
                continue
            else:
                analyzed += x
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Please select an checkpoint")
