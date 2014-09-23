from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .forms import CampeonatoForm
from .models import Campeonato
from complejos.forms import ComplejoPublicForm, ComplejoForm
from complejos.models import Complejo
from equipos.models import Equipo
from django import forms

# Create your views here.
@login_required
def agregar(request):
    logged_user = request.user.id
    if request.method == "POST":
        form = CampeonatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:perfil')
        else:
            print form.errors
    else:
        form = CampeonatoForm()
    return render_to_response("campeonato/agregar.html", {'form': form, 'user': logged_user}, context_instance=RequestContext(request))

@login_required
def editar(request, id=None):
    #Obtengo el objeto de acuerdo al id
    if id:
        campeonato_objeto =  get_object_or_404(Campeonato, id=id, complejo_id__user=request.user)
    else:
        campeonato_objeto = Campeonato(id=request.id)

    if request.method == "POST":
        campeonato_form = CampeonatoForm(request.POST, instance=campeonato_objeto)
        if campeonato_form.is_valid():
            campeonato_form.save()
            return redirect('usuarios:perfil')
    else:
        campeonato_form = CampeonatoForm(instance=campeonato_objeto)
    #Renderizo la vista y paso el objeto con los valores a editar
    return render_to_response("campeonato/editar.html", {'form': campeonato_form}, context_instance=RequestContext(request))

@login_required
def ver(request, id=None):
    #complejos = Complejo.objects.all().filter(id=id, user__id = request.user.id)
    campeonatos =  get_object_or_404(Campeonato, id=id, complejo_id__user=request.user)
    equipos = Equipo.objects.all().filter(complejo_id=campeonatos.id, complejo_id__user=request.user)
    logged_user = request.user.id
    return render_to_response("campeonato/ver.html", {'campeonatos': campeonatos, 'user': logged_user, 'equipos':equipos}, context_instance=RequestContext(request))

@login_required
def encurso(request):
    campeonatos = Campeonato.objects.all().filter(complejo_id__user = request.user.id, estado_torneo=1)
    form = CampeonatoForm()
    logged_user = request.user.id
    return render_to_response("campeonato/encurso.html", {'form': form, 'user': logged_user, 'campeonatos':campeonatos}, context_instance=RequestContext(request))

@login_required
def finalizados(request):
    campeonatos = Campeonato.objects.all().filter(complejo_id__user = request.user.id, estado_torneo=0)
    form = CampeonatoForm()
    logged_user = request.user.id
    return render_to_response("campeonato/encurso.html", {'form': form, 'user': logged_user, 'campeonatos':campeonatos}, context_instance=RequestContext(request))

