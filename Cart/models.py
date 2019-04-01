import os
from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from hashlib import md5
from django.conf import settings

class Category(models.Model):
    Group = models.ForeignKey('Cart.Group', on_delete=models.CASCADE, related_name='categories')
    Title = models.CharField(max_length=50,verbose_name='Название категории',null=True)
    Keywords = ArrayField(models.CharField(max_length=50), 
                        verbose_name='Ключевые слова',
                        help_text='слова и словосочетания, описывающие категорию')
    
    TranslitTitle = models.CharField(max_length=50, null=True)
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CategoryGroup(models.Model):
    Title = models.CharField(max_length=50, verbose_name='Название',null=True)
    TranslitTitle = models.CharField(max_length=50,null=True)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы категорий'


class Good(models.Model):
    Title = models.CharField(verbose_name=u'Название', unique=True,
                             max_length=100, default=u'Без навзания')
    UrlHash = models.CharField(null=True, blank=True, max_length=70, unique=True)        
    Category = models.ForeignKey('Catalog.category', verbose_name=u'Категория', on_delete=models.CASCADE, null=True,
                                 related_name='goods')
    Characteristics = JSONField(verbose_name=u'Характеристики товара', null=True,
                                blank=True, default=dict)
    Price = models.IntegerField(verbose_name=u'Цена', null=True, blank=True)
    Description = models.TextField(verbose_name=u'Описание', null=True)
    Main_image = models.ImageField(verbose_name=u'Главная фотография товара',
                                   help_text=u'Эта фотография будет отображаться в карточке товара',
                                   upload_to=generate_path, null=True)
    Images = ArrayField(models.ImageField(upload_to=generate_path, blank=True, null=True),
                        verbose_name='Галерея')
    
    #SEO fields block
    Page_keywords = ArrayField(models.CharField(max_length=50), null=True,
                               help_text=u'Cлова и словосочетания описывающие содержимое страницы(Необходимо для SEO оптимизации)')

    Page_description = models.CharField(verbose_name=u'Описание страницы', max_length=200, null=True,
                                        help_text=u'Текст необходимый для <meta description>(Необходимо для SEO оптимизации)')

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    @staticmethod
    def generate_path(instance, filename):
        ext = filename.rsplit('.', 1)[-1]
        h = md5(str(filename).encode()).hexdigest()
        result = 'Catalog/%s/%s/%s.%s' % (h[:2], h[2:4], h[4:], ext)
        path = os.path.join(settings.MEDIA_ROOT, result)
        
        if os.path.exists(path):
            os.remove(path)
        return result
    
    

    def __str__(self):
        return self.Title