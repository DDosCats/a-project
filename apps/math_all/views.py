from django.shortcuts import render

def index(request):
    return render(request, 'math_all/index.html')
