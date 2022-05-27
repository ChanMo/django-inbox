from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Record(models.Model):
    """
    管理员手动发送记录
    """
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, verbose_name='用户')
    title = models.CharField(_('title'), max_length=255)
    body = models.TextField(_('body'), blank=True, null=True)
    link = models.CharField(
        '链接', max_length=200, blank=True, null=True,
        help_text='用户点击消息跳转的链接地址')
    handler = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name='my_send'
    )
    created_at = models.DateTimeField('发送时间', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_users(self):
        return ','.join([str(i) for i in self.users.all()])

    class Meta:
        ordering = ['-created_at']
        verbose_name = '发送记录'
        verbose_name_plural = '发送记录'
    


class Message(models.Model):
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name=_('receiver user'))
    title = models.CharField(_('title'), max_length=255)
    body = models.TextField(_('body'), blank=True, null=True)
    link = models.CharField(
        '链接', max_length=200, blank=True, null=True,
        help_text='用户点击消息跳转的链接地址')
    is_read = models.BooleanField(_('is read'), default=False)
    created = models.DateTimeField(_('created at'), auto_now_add=True)
    updated = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = _('inbox')
        verbose_name_plural = _('inbox')
