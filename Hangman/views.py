from django.shortcuts import render, HttpResponse

def hangman(request):
    return render(request, 'Hangman/hangman.html')
