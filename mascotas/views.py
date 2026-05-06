from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota, Dueno
from .forms import MascotaForm, DuenoForm

# Create your views here.

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/lista_mascotas.html', {'mascotas': mascotas})

def crear_mascota(request):
    form = MascotaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_mascotas')
    return render(request, 'mascotas/form_mascota.html', {'form': form})

def editar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    form = MascotaForm(request.POST or None, request.FILES or None, instance=mascota)
    if form.is_valid():
        form.save()
        return redirect('lista_mascotas')
    return render(request, 'mascotas/form_mascota.html', {'form': form})

def eliminar_mascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    mascota.delete()
    return redirect('lista_mascotas')


# Dueño 
def lista_duenos(request):
    duenos = Dueno.objects.all()
    return render(request, 'mascotas/lista_duenos.html', {'duenos': duenos})

def crear_dueno(request):
    form = DuenoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_duenos')
    return render(request, 'mascotas/form_dueno.html', {'form': form})

def editar_dueno(request, id):
    dueno = get_object_or_404(Dueno, id=id)
    form = DuenoForm(request.POST or None, instance=dueno)
    if form.is_valid():
        form.save()
        return redirect('lista_duenos')
    return render(request, 'mascotas/form_dueno.html', {'form': form})

def eliminar_dueno(request, id):
    dueno = get_object_or_404(Dueno, id=id)
    dueno.delete()
    return redirect('lista_duenos')
