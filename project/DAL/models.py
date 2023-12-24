from django.contrib.auth.models import AbstractUser
from django.db import models


# from .bot import send_telegram_message


class Region(models.Model):
    objects = None
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return self.name


class Role(models.Model):
    objects = None
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(unique=True)  # Сделайте поле email уникальным
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.username


class Task(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_created')
    executor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_executed')
    status = models.CharField(max_length=255)
    information = models.TextField()
    release_date = models.DateField()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title

    """
    def save(self, *args, **kwargs):
        # Определение, новая ли это задача или обновление существующей
        is_new = self._state.adding
        super().save(*args, **kwargs)

        # Сообщение зависит от того, новая задача или обновление
        if is_new:
            message = f"Новая задача создана: {self.title}"
        else:
            message = f"Задача обновлена: {self.title}"
        send_telegram_message(message)

    def delete(self, *args, **kwargs):
        message = f"Задача удалена: {self.title}"
        super().delete(*args, **kwargs)
        send_telegram_message(message)
    """


class Article(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    information = models.TextField()
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)
    release_date = models.DateField()

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class Company(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.title
