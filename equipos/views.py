from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from campeonatos.forms import CampeonatoForm
from campeonatos.models import Campeonato
from complejos.forms import ComplejoPublicForm, ComplejoForm
from complejos.models import Complejo
from equipos.models import Equipo
from equipos.forms import EquiposForm
from django import forms

# Create your views here.
@login_required
def agregar(request):
    logged_user = request.user.id
    if request.method == "POST":
        form = EquiposForm(request.POST)
        if form.is_valid():
            form.save()
            return lista(request)
        else:
            print form.errors
    else:
        form = EquiposForm()
    return render_to_response("equipos/agregar.html", {'form': form, 'user': logged_user}, context_instance=RequestContext(request))

@login_required
def editar(request, id=None):
    #Obtengo el objeto de acuerdo al id
    if id:
        equipo_objeto =  get_object_or_404(Equipo, id=id, complejo_id__user=request.user)
    else:
        equipo_objeto = Equipo(id=request.id)

    if request.method == "POST":
        form = EquiposForm(request.POST, instance=equipo_objeto)
        if form.is_valid():
            form.save()
            return lista(request)
        else:
            print form.errors
    else:
        form = EquiposForm(instance=equipo_objeto)
    #Renderizo la vista y paso el objeto con los valores a editar
    return render_to_response("equipos/editar.html", {'form': form}, context_instance=RequestContext(request))

@login_required
def ver(request, id=None):
    #complejos = Complejo.objects.all().filter(id=id, user__id = request.user.id)
    campeonatos =  get_object_or_404(Campeonato, id=id, complejo_id__user=request.user)
    equipos = Equipo.objects.all().filter(complejo_id=campeonatos.id, complejo_id__user=request.user)
    logged_user = request.user.id
    return render_to_response("equipos/ver.html", {'campeonatos': campeonatos, 'user': logged_user, 'equipos':equipos}, context_instance=RequestContext(request))

@login_required
def lista(request):
    equipos = Equipo.objects.all().filter(complejo_id__user=request.user)
    form = CampeonatoForm()
    logged_user = request.user.id
    return render_to_response("equipos/lista.html", {'form': form, 'user': logged_user, 'equipos':equipos}, context_instance=RequestContext(request))