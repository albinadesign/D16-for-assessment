from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с новостями
    list_display = ['title','author', 'category', 'dateCreation', 'text']
    list_filter = ('category', 'author', 'dateCreation')
    search_fields = ('title',)



# Register your models here.


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)


