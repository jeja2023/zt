from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    class Meta:
        # 指定自定义用户模型的名称
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def clean(self):
        super().clean()
        password1 = self.password  # 修改为获取用户输入的密码
        password2 = self.password  # 这里你需要调整逻辑以获取第二次输入的密码

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("两次密码输入不一致，请重新输入。")