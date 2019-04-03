from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from .media_paths import generate_path
from transliterate import translit
from hashlib import md5

class Category(models.Model):
	Group = models.ForeignKey('Catalog.CategoryGroup', on_delete=models.CASCADE, related_name='categories')
	Title = models.CharField(max_length=50,verbose_name='Название категории',null=True)
	Keywords = ArrayField(models.CharField(max_length=50), 
						verbose_name='Ключевые слова',
						help_text='слова и словосочетания, описывающие категорию')    
	
	def __str__(self):
		self.Title

	def getUrl(self):
		return translit(self.Title, 'ru', reversed=True)
		
	class Meta:
		db_table = ''
		managed = True
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class CategoryGroup(models.Model):
	Title = models.CharField(max_length=50, verbose_name='Название', null=True, unique=True)
	TranslitTitle = models.CharField(max_length=50,null=True)

	def __str__(self):
		self.Title

	def getUrl(self):
		return translit(self.Title, 'ru', reversed=True)
	
	class Meta:
		db_table = ''
		managed = True
		verbose_name = 'Группа'
		verbose_name_plural = 'Группы категорий'


class Good(models.Model):
	Title = models.CharField(verbose_name=u'Название', unique=True,
							 max_length=100, default=u'Без навзания')
	UrlHash = models.CharField(null=True, max_length=70, unique=True,)
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
	Units = models.CharField(max_length=50, verbose_name='Ед. изм. товара')
	#SEO fields block
	Page_keywords = ArrayField(models.CharField(max_length=50), null=True,
							   help_text=u'Cлова и словосочетания описывающие содержимое страницы(Необходимо для SEO оптимизации)')
	Page_description = models.CharField(verbose_name=u'Описание страницы', max_length=200, null=True,
										help_text=u'Текст для <meta description>(Необходимо для SEO оптимизации)')
	
	States = (
		('Stock','Есть в наличии'),
		('Sold','Продано'),
	)
	State = models.CharField(max_length=50, choices=States, verbose_name='Наличиe:', null=True)
	PublishedDate = models.DateField(auto_now_add=True)
	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товары"
	
	def get_absolute_url(self):
		return 'goods/%s/' % self.UrlHash

	def __str__(self):
		return self.Title

	def save(self, *args, **kwargs):
		if self.UrlHash is None:
			hash_for_good = md5(self.Title.encode())
			hash_for_good.update(self.Category.Title.encode())
			self.UrlHash = hash_for_good.hexdigest()
		super().save(*args, **kwargs)

class Attribute(models.Model):
	Title = models.CharField(verbose_name=u'Название', unique=True, max_length=50)
	TYPE_TEXT = 'str'
	TYPE_FLOAT = 'float'
	TYPE_INT = 'int'
	TYPE_BOOLEAN = 'bool'
	characteristic_types = (
		(TYPE_TEXT, (u'Текстовая')),
		(TYPE_FLOAT, (u'Число с запятой')),
		(TYPE_INT, (u'Целое число')),
		(TYPE_BOOLEAN, (u'Да / Нет')),
	)
	Type = models.CharField(verbose_name=u'Тип характеристики товара',
										   choices=characteristic_types, null=True, max_length=50)
	Category = models.ForeignKey('Catalog.category', verbose_name=u'Категория', on_delete=models.CASCADE, default=1,
								 related_name='characteristics')
	PossibleValues = ArrayField(base_field=models.CharField(max_length=250, blank=True),
								verbose_name=u'Возможные значения характеристики', null=True, blank=True)
	Units = models.CharField(max_length=40, null=True, verbose_name='Единицы измерения', blank=True)
	class Meta:
		verbose_name = "Характеристика"
		verbose_name_plural = "Характеристики"

	def __str__(self):
		return self.Title