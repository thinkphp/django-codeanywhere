from django.shortcuts import render
from django.http import HttpResponse

def helloworldview(request):

    template = "index.html"

    context = {}  

    return render(request, template, context)


    #return HttpResponse(response)
