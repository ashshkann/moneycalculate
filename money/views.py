from django.shortcuts import render

def homePage(request):
    context = {

    }
    
    return render(request, 'home.html', context)