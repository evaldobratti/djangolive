from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forum.models import *
from django.core.urlresolvers import reverse

@login_required
def index(request):
	return render(request, 'forum/index.html', {
		    'categoria': None,
		    'categorias': Categoria.objects.filter(categoria_pai__isnull=True),
            'topicos': Topico.objects.filter(categoria__isnull=True)
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

def visualizar_categoria(request, categoria_id):
	c = get_object_or_404(Categoria, pk=categoria_id)
	return render(request, 'forum/categoria.html', {
			'categoria': c,
		    'categorias': Categoria.objects.filter(categoria_pai=c),
            'topicos': Topico.objects.filter(categoria=c)
        })

def novo_topico(request, categoria_id):
	c = get_object_or_404(Categoria, pk=categoria_id)
	return render(request, 'forum/novo_topico.html', {
			'categoria': c
		})

def novo_topico_criar(request, categoria_id):
	c = get_object_or_404(Categoria, pk=categoria_id)
	t = c.topico_set.create(titulo=request.POST['titulo'], 
		descricao=request.POST['descricao'], 
		conteudo=request.POST['conteudo'],
		autor=request.user)
	return HttpResponseRedirect(reverse('forum:topico', args=(t.id,)))