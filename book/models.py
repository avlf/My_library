from django.db import models


class Genre(models.Model):
    name = models.CharField('Название жанра ', max_length=100)
    description = models.CharField('описание жанра ', max_length=2000, blank=True)

    def __str__(self):
        return self.name


class Reward(models.Model):
    name = models.CharField('Название премии ', max_length=100)
    date = models.DateField('Дата получения ', blank=True, null=True)
    description = models.CharField('Описание премии ', max_length=2000, blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    second_name = models.CharField('Отчество', max_length=100, blank=True)
    surname = models.CharField('Фамилия', max_length=100)
    birthday = models.DateField('Дата рождения ', blank=True, null=True)
    deathday = models.DateField('Дата смерти ', blank=True, null=True)
    description = models.CharField('Биография ', max_length=2000, blank=True)
    rewards = models.ManyToManyField(
        Reward,
        verbose_name='Награды',
        related_name='authors',
        blank=True,
        # on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('Название книги ', max_length=100)
    description = models.CharField('Биография ', max_length=2000, blank=True)
    genres = models.ManyToManyField(
        Genre,
        verbose_name='Жанры книги ',
        related_name='books',
        blank=True,
        # on_delete=models.CASCADE,
    )
    author = models.ManyToManyField(
        Author,
        verbose_name=' Автор книги',
        related_name='book',
        blank=True,
        # on_delete=models.CASCADE,
    )
    publish_date = models.DateField('Дата публикации ')

    def __str__(self):
        return self.title
