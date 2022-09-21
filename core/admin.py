from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'codigo_do_produto',
        'preco', 
        'estoque',
        'created_at',
        'updated_at',
    )


admin.site.register(Produto, ProdutoAdmin)
