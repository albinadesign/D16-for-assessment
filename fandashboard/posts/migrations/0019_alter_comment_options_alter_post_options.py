# Generated by Django 4.1.9 on 2023-05-10 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_alter_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id']},
        ),
    ]
