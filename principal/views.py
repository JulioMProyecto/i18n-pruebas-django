from django.shortcuts import render, HttpResponse
from .models import Proyecto
# Create your views here.


def inicio(request):

    #from django.utils import translation
    # user_language = 'es'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #    del request.session[translation.LANGUAGE_SESSION_KEY]
    from django.utils.translation import gettext as _

    title = _('Homepage')

    proyectos = Proyecto.objects.all()
    context = {"proyectos": proyectos, 'title': title, }
    return render(request, "principal/index.html", context)


def trabajos(request):
    proyectos = Proyecto.objects.all()
    context = {"proyectos": proyectos}
    return render(request, "principal/trabajos.html", context)


def detalles(request, slug_text):
    proyecto = Proyecto.objects.filter(slug=slug_text)
    if proyecto.exists():
        proyecto = proyecto.first()
    else:
        return HttpResponse("<h1>Pagina no encontrada</h1>")

    context = {'proyecto': proyecto}

    return render(request, "principal/detalles.html", context)
