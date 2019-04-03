from django.db import models
from transliterate import translit


class Filter(models.Model):
    VerboseTitle = models.CharField(max_length=50, verbose_name='Название фильтра') 
    Title = models.CharField(max_length=50, unique=True)
    Attribute = models.OneToOneField('Catalog.Attribute', on_delete=models.CASCADE,
                                     verbose_name='Характеристика товара', 
                                     help_text='Характеристика для которой создается фильтр',
                                     related_name='filter',
                                     null=True)
    Type = models.CharField(max_length=50,null=True)
    def save(self, *args, **kwargs):
        self.Type = kwargs['update_fields']['Type']
        
        if self.Title is None:
            self.Title = translit(VerboseTitle.encode(), 'ru', reversed=True)
        super().save(*args, **kwargs)


    def __str__(self):
        self.Title

    class Meta:
        managed = True
        verbose_name = 'Filter'
        verbose_name_plural = 'Filters'
