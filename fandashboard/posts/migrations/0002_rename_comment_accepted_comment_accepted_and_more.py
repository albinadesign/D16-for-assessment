# Generated by Django 4.2 on 2023-05-02 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_accepted',
            new_name='accepted',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author_comment',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='text_comment',
            new_name='text',
        ),
    ]
