from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Phone(models.Model):
    name = models.CharField(verbose_name="Имя абонента", max_length=64, db_index=True)
    mobile_phone = models.IntegerField(verbose_name="Мобильный телефон", null=True)
    second_mobile_phone = models.IntegerField(verbose_name="Доп. моб. телефон", null=True)
    home_phone = models.IntegerField(verbose_name="Домашний телефон", null=True)
    work_phone = models.IntegerField(verbose_name="Рабочий телефон", null=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)