import os 

from PIL import Image

from django.conf import settings
from django.db import models
from app.common import choices
from app import utils
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Produto')   
    descripition = models.TextField(verbose_name='Descrição')
    short_descripition = models.TextField(verbose_name='Descrição Curta', null=True, blank=True)
    image = models.ImageField(upload_to='product_images/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    amount = models.DecimalField(verbose_name='Valor do produto', decimal_places=2, max_digits=8)
    promotional_amount = models.DecimalField(verbose_name='Valor do produto promocional', decimal_places=2, max_digits=8, default=0)
    type = models.CharField(choices=choices.PRODUCT_TYPE, max_length=50, verbose_name='Tipo do produto', default='simple')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def resize_image(self, img, new_width: int):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_heigth = img_pil.size 

        if original_width  >= new_width:
            new_heigth = (new_width * original_heigth) / original_width
            new_img = img_pil.resize((new_width, new_heigth), Image.LANCZOS)
            new_img.save(
                 img_full_path,
                optimize=True
            )

            print('A imagem foi redimencionada')
        img_pil.close()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

        if self.image:
            self.resize_image(self.image, 800)

    def get_formated_amount(self):
        return utils.format_money(self.amount)
    
    get_formated_amount.short_description = 'Valor'

class Variation(models.Model):
    name = models.CharField(max_length=190, verbose_name='Variação do produto')
    product = models.ForeignKey(Product, verbose_name='ID do Produto', on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name='Valor do produto', decimal_places=2, max_digits=8)
    promotional_amount = models.DecimalField(verbose_name='Valor do produto promocional', decimal_places=2, max_digits=8, default=0)
    stock = models.IntegerField(verbose_name='Quantidade em estoque', default=1)

    class Meta:
        verbose_name = 'Variação do Produto'
        verbose_name_plural = 'Variações dos produtos'

    def __str__(self) -> str:
        return self.name or self.product.name