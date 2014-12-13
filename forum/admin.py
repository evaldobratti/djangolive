from django.contrib import admin
from forum.models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(Topico)
admin.site.register(Label)
admin.site.register(UsuarioForum)
admin.site.register(Categoria)