from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, 'index.html')


def RegistroUsuarioView(request):
    form = forms.RegistroUsuarioForm()
    data = {'forms': form}
    return render(request, 'registro.html', data)