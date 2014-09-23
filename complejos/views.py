from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from complejos.forms import ComplejoPublicForm, ComplejoForm
from complejos.models import Complejo
from equipos.models import Equipo
from django import forms

# Create your views here.
@login_required
def agregar(request):
    form = ComplejoPublicForm()
    logged_user = request.user.id
    return render_to_response("torneos/agregar.html", {'form': form, 'user': logged_user}, context_instance=RequestContext(request))

@login_required
def editar(request, id=None):
    #Obtengo el objeto de acuerdo al id
    if id:
        complejo_objeto =  get_object_or_404(Complejo, id=id, user=request.user)
    else:
        complejo_objeto = Complejo(id=request.id)

    if request.method == "POST":
        complejo_form = ComplejoPublicForm(request.POST, instance=complejo_objeto)
        if complejo_form.is_valid():
            complejo_form.save()
            return redirect('usuarios:perfil')
    else:
        complejo_form = ComplejoPublicForm(instance=complejo_objeto)
    #Renderizo la vista y paso el objeto con los valores a editar
    return render_to_response("torneos/editar.html", {'form': complejo_form}, context_instance=RequestContext(request))

@login_required
def ver(request, id=None):
    #complejos = Complejo.objects.all().filter(id=id, user__id = request.user.id)
    complejos =  get_object_or_404(Complejo, id=id, user=request.user)
    equipos = Equipo.objects.all().filter(complejo_id=complejos.id, complejo_id__user=request.user)
    logged_user = request.user.id
    return render_to_response("torneos/ver.html", {'complejos': complejos, 'user': logged_user, 'equipos':equipos}, context_instance=RequestContext(request))
