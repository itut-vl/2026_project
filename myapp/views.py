from django.shortcuts import render

def base_open(request):
    return render(request, 'base.html')

def test_open(request):
    return render(request, 'test.html')