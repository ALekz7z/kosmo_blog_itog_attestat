from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class articles(models.Model):
    title = models.CharField('Название', max_length=150)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикации')

    def __str__ (self):
        return self.title

    def get_absolute_url(self):
        return f'/lenta/{self.id}'


    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Comments(models.Model):
    article = models.ForeignKey(articles, on_delete = models.CASCADE, verbose_name='Статья', blank = True, null = True,related_name='comments_articles' )
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Автор комментария', blank = True, null = True )
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name='Видимость статьи', default=False)




