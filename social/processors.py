from .models import Link
#Diccionarios para generar Link de redes Sociales

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()

    for link in links:
        ctx[link.key] =link.url
    return ctx