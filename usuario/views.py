from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from complejos.forms import ComplejoPublicForm
from complejos.models import Complejo
from campeonatos.forms import CampeonatoForm
from campeonatos.models import Campeonato

# Create your views here.
class PerfilView(TemplateView):
    template_name = "perfil/index.html"

@login_required
def perfil(request):
    campeonatos = Campeonato.objects.all().filter(complejo_id__user = request.user.id)
    form = CampeonatoForm()
    logged_user = request.user.id
    return render_to_response("perfil/index.html", {'form': form, 'user': logged_user, 'campeonatos':campeonatos}, context_instance=RequestContext(request))
