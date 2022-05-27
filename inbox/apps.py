from django.apps import AppConfig


class InboxConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inbox'
    verbose_name = '收件箱管理'

    # def ready(self):
    #     import inbox.receivers
