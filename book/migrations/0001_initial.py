# Generated by Django 4.0.6 on 2022-12-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения ')),
                ('deathday', models.DateField(blank=True, null=True, verbose_name='Дата смерти ')),
                ('description', models.CharField(blank=True, max_length=2000, verbose_name='Биография ')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название жанра ')),
                ('description', models.CharField(blank=True, max_length=2000, verbose_name='описание жанра ')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название премии ')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата получения ')),
                ('description', models.CharField(blank=True, max_length=2000, verbose_name='Описание премии ')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название книги ')),
                ('description', models.CharField(blank=True, max_length=2000, verbose_name='Биография ')),
                ('publish_date', models.DateField(verbose_name='Дата публикации ')),
                ('author', models.ManyToManyField(blank=True, related_name='book', to='book.author', verbose_name=' Автор книги')),
                ('genres', models.ManyToManyField(blank=True, related_name='books', to='book.genre', verbose_name='Жанры книги ')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='rewards',
            field=models.ManyToManyField(blank=True, related_name='authors', to='book.reward', verbose_name='Награды'),
        ),
    ]
