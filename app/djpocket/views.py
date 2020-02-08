from django.shortcuts import render

def HomeView(request):
    title = 'Home'
    context = {
        'title': title
    }
    return render(request, 'home.html', context)