# Generated by Django 4.1.9 on 2023-05-04 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_comment_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='comment_post',
        ),
    ]
