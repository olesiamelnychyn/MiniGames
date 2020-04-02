from django.shortcuts import render


def bones(request):
    return render(request, 'Bones/bones.html')