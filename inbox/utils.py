from django.db.models.query import QuerySet
from .models import Message

def send_message(users, title, content=None, link=None):
    if isinstance(users, list):
        for user in users:
            Message.objects.create(
                receiver = user,
                title = title,
                body = content,
                link = link
            )
    else:
        Message.objects.create(
            receiver = users,
            title = title,
            body = content,
            link = link
        )

