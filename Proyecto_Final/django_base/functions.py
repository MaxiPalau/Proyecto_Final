from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def usuario_logueado(request):
    if request.user.is_authenticated:
        username  = request.user.username
        id_usuario = User.objects.filter(username__icontains = username).values('id')
        lista_grupo = list(Group.objects.filter(user__in = id_usuario).values_list('name', flat=True))

        for grupo in lista_grupo:
            if grupo == 'Ferreteria':
                return True
            else:
                return False
    else:
        return False

def paginator(request, object, item):
    # object = queryset, lista de objetos que se quieren paginar
    # item = int, cantidad de items por pagina
    grupo = usuario_logueado(request)
    pag = request.GET.get('page', 1)
    paginator = Paginator(object, item)
    try:
        resultados = paginator.page(pag)
    except PageNotAnInteger:
        resultados = paginator.page(1)
    except EmptyPage:
        resultados = paginator.page(paginator.num_pages)
    context = {'object_list':resultados, 'grupo':grupo}
    return context