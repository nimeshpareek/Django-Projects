# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc_button = request.POST.get('removepunc', 'off')
    capital_button = request.POST.get('capitalizefirst','off')
    newline_button = request.POST.get('newlineremover', 'off')
    space_button = request.POST.get('spaceremover', 'off')
    count_button = request.POST.get('charcounter', 'off')
    bool = False
    if removepunc_button == "on":
        bool = True
        x = 1
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
        params = {'analyzed_text': analyzed}
        djtext = analyzed

    if(capital_button == "on"):
        bool = True
        djtext = djtext.upper()
        params = {'analyzed_text': djtext}
        
    if newline_button == "on":
        bool = True
        newtext = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                newtext += char
        djtext = newtext  # Modify the djtext string directly
        params = {'analyzed_text': djtext}

    if(space_button == "on"):
        bool = True
        newtext = ""
        for index, x in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                newtext += x 
                
        djtext = newtext
        params = {'analyzed_text': djtext}

    if(count_button == "on" and bool == False):
        size = len(djtext)
        params = {'analyzed_text': size}
    if(count_button == "on" and bool == True):
        size = len(djtext)
        txt = f" \n Your char size is {size}" 
        djtext += txt
        params = {'analyzed_text': djtext}
        
    if(count_button == "off" and space_button == "off" and newline_button == "off" and capital_button == "off" and removepunc_button == "off"):
        return HttpResponse("Please select an checkpoint")
    print(djtext)
    return render(request, 'analyze.html', params)
    # else:
        