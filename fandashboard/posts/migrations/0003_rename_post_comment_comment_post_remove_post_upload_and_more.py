# Generated by Django 4.2 on 2023-05-02 05:56

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_rename_comment_accepted_comment_accepted_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_comment',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upload',
        ),
        migrations.AddField(
            model_name='comment',
            name='dateCreation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
