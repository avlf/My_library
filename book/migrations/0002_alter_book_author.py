# Generated by Django 4.0.6 on 2022-12-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='book', to='book.author', verbose_name=' Автор книги'),
        ),
    ]
