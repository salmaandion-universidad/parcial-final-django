from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProgramaForm

def crear_programa(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Programa registrado exitosamente!')
            return redirect('crear_programa')
    else:
        form = ProgramaForm()

    return render(request, 'myapp/crear_programa.html', {'form': form})