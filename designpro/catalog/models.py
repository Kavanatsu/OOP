from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.crypto import get_random_string

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, verbose_name='Имя')
    surname = models.CharField(max_length=200, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=200, verbose_name='Отчество')
    username = models.CharField(max_length=200, verbose_name='Логин', unique=True)
    email = models.EmailField(max_length=200, verbose_name='Почта', unique=True)
    password = models.CharField(max_length=200, verbose_name='Пароль')
    role = models.CharField(max_length=200, verbose_name='Роль',
                            choices=(('admin', 'Администратор'), ('user', 'Пользователь')), default='user')

    def __str__(self):
        return self.name

def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


class Application(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', blank=False)
    username = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, verbose_name='Описание', help_text='Напишите описание ', blank=False)
    categories = models.ForeignKey('Categorise', verbose_name='Категория', on_delete=models.CASCADE)
    image = models.ImageField(max_length=254, verbose_name='Изображение', upload_to=get_name_file,
                              null=True, blank=False,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])])
    status = models.CharField(max_length=200, verbose_name='Статус',
                              choices=(('new', 'Новая'), ('in work', 'Принято в работу'), ('done', 'Выполнено')),
                              default='new')
    date = models.DateField(verbose_name='Дата добавления', auto_now_add=True)
    img = models.ImageField(max_length=254, verbose_name='Изображение', upload_to=get_name_file, null=True, blank=True,
                            validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])])
    comment = models.TextField(max_length=1000, verbose_name='Комментарий', help_text="Комментарий", blank=True)

    def __str__(self):
        return self.name


class Categorise(models.Model):
    name = models.CharField(max_length=200, help_text="Напишите категорию", blank=False)

    def __str__(self):
        return self.name