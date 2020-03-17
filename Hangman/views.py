from django.shortcuts import render, HttpResponse

def hangman(request):
    return render(request, 'Hangman/hangman.html')

def game(request):
    return render(request, 'Hangman/game.html')
