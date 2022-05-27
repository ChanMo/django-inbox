from django.contrib.auth import get_user_model
from celery import shared_task
from .models import *

@shared_task
def send_msg(uid, text):
    """发送信息"""
    return Message.objects.create(
        receiver = get_user_model().objects.get(pk=uid),
        title = '系统通知',
        body = text
    )
