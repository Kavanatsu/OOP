from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, verbose_name='Имя', blank=False)
    surname = models.CharField(max_length=200, verbose_name='Фамилия', blank=False)
    patronymic = models.CharField(max_length=200, verbose_name='Отчество', blank=True)
    username = models.CharField(max_length=200, verbose_name='Логин', unique=True, blank=False)
    email = models.EmailField(max_length=200, verbose_name='Почта', unique=True, blank=False)
    password = models.CharField(max_length=200, verbose_name='Пароль', blank=False)
    role = models.CharField(max_length=200, verbose_name='Роль',
                            choices=(('admin', 'Администратор'), ('user', 'Пользователь')), default='user')

    def __str__(self):
        return self.name