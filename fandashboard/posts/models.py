from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import pgettext_lazy
from ckeditor.fields import RichTextField


CATEGORIES = [('Tanks','Tanks'), ('Heals', 'Heals'), ('Damage Dealers', 'Damage Dealers'),
              ('Traders','Traders'), ('Gild masters', 'Gild Masters'), ('Quest givers', 'Quest givers'),
              ('Blacksmiths', 'Blacksmiths'), ('Tanners', 'Tanners'), ('Potion masters', 'Potion masters'),
              ('Spell masters', 'Spell masters')
              ]


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
    category = models.CharField(max_length=28, choices=CATEGORIES, default='Tanks', verbose_name='category')
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128, verbose_name=pgettext_lazy('post title', 'title'))
    text = RichTextField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'{self.pk}'

    class Meta:
        ordering = ['id']


class Comment(models.Model):
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_dateCreation = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f'{self.pk}'

    class Meta:
        ordering = ['id']