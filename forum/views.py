from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forum.models import *
from django.core.urlresolvers import reverse

@login_required
def index(request):
	return render(request, 'forum/index.html', {
            'topicos': Topico.objects.all()
        })

def visualizar_topico(request, topico_id):
	t = get_object_or_404(Topico, pk=topico_id)
	return render(request, 'forum/topico.html', {
			'topico': t
		})

def comentar(request, topico_id):
	t = get_object_or_404(Topico, pk=topico_id)
	t.post_set.create(conteudo=request.POST['conteudo'], autor=request.user)

	return HttpResponseRedirect(reverse('forum:topico', args=(t.id,)))