# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc_button = request.GET.get('removepunc', 'off')
    capital_button = request.GET.get('capitalizefirst','off')
    newline_button = request.GET.get('newlineremover', 'off')
    space_button = request.GET.get('spaceremover', 'off')
    count_button = request.GET.get('charcounter', 'off')
    if removepunc_button == "on":
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

    elif(capital_button == "on"):
        djtext = djtext.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': djtext}
        return render(request, 'analyze.html', params)

    elif(newline_button == "on"):
        newtext = ""
        for x in djtext:
            if x!="\n":
                newtext += x
        params = {'purpose': 'New Line Remove', 'analyzed_text': newtext}
        return render(request, 'analyze.html', params)

    elif(space_button == "on"):
        newtext = ""
        for index, x in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                newtext += x 
                
        params = {'purpose': 'Space remover', 'analyzed_text': newtext}
        return render(request, 'analyze.html', params)

    elif(count_button == "on"):
        size = len(djtext)
        params = {'purpose': 'char count', 'analyzed_text': size}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Please select an checkpoint")
