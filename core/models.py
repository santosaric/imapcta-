from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    codigo_do_produto = models.IntegerField('Codigo de produto')
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField("Quantidade em Estoque")
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
