from django.contrib.auth.models import AbstractUser
from django.db import models

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