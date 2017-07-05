from django.db import models
from account.models import User

class Topic(models.Model):
    title = models.CharField('Titulo', max_length=150)
    body = models.TextField('Menssagem')
    author = models.ForeignKey(User, verbose_name='Autor', related_name='topics')
    views = models.IntegerField('Visualizações', blank=True, default=0)
    answers = models.IntegerField('Respostas', blank=True, default=0)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'
        ordering = ['-updated']

class Reply(models.Model):
    reply = models.TextField('Resposta')
    topic = models.ForeignKey(Topic, verbose_name='Tópico', related_name='replies')
    author = models.ForeignKey(User, verbose_name='Autor', related_name='replies')
    correct = models.BooleanField('Correta?',blank=True, default=False)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.reply[:100]

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
        ordering = ['-correct','created']
