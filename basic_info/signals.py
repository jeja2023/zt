from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Ypbg  # 替换为你的模型
from django.conf import settings
from django.utils.timezone import now

@receiver(pre_save, sender=Ypbg)
def update_updated_by(sender, instance, **kwargs):
    # 检查实例是否已经保存过，即是否是更新操作
    if instance.pk:  # 如果有主键，表示这是一个更新操作
        if hasattr(instance, 'updated_by') and hasattr(instance, 'request_user'):
            instance.updated_by = instance.request_user  # 设置 `updated_by`