from django.dispatch import receiver
from django.db.models.signals import post_save
# from allauth.account.signals import user_signed_up
from .utils import send_message


# @receiver(user_signed_up)
# def send_welcome_msg(sender, request, user, **kwargs):
#     send_message(
#         user,
#         '欢迎注册',
#         '',
#         '/'
#     )
