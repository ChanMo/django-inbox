from django import forms
from django.contrib.auth import get_user_model
from accounts.widgets import UserTreeWidget
from .models import Message, Record
from .utils import send_message


class MessageForm(forms.ModelForm):
    users = forms.CharField(label='接收用户', widget=UserTreeWidget)
    
    class Meta:
        model = Message
        fields = ('users', 'title', 'body', 'link')

    def clean_users(self):
        data = self.cleaned_data['users'].split(',')
        ids = list(set(data))
        return list(get_user_model().objects.filter(id__in=ids))


    def send(self, handler=None):
        data = self.cleaned_data
        res = Record.objects.create(
            title = data['title'],
            body = data['body'],
            link = data['link'],
            handler = handler
        )
        res.users.set(data['users'])
        send_message(
            data['users'],
            data['title'],
            data['body'],
            data['link']
        )
