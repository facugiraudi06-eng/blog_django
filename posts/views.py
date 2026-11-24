from django.shortcuts import render


def inicio(request):
    # Muestra la página de inicio
    return render(request, 'posts/inicio.html')


def acerca(request):
    # Muestra la página acerca del autor
    return render(request, 'posts/acerca.html')