from django.shortcuts import render

def dashboard(request):
    return render(request, 'blog/dashboard.html')