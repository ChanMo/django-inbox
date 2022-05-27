from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Message


class MessageListView(LoginRequiredMixin, ListView):
    paginate_by = 12
    model = Message

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user)


@login_required
def mark_read(request, pk):
    """标记为已读"""
    obj = get_object_or_404(
        Message, pk=pk, receiver=request.user, is_read=False)
    obj.is_read = True
    obj.save()

    return redirect('/inbox/')


@login_required
def mark_read_all(request):
    """全部标记为已读"""
    Message.objects.filter(receiver=request.user,
                           is_read=False).update(is_read=True)

    return redirect('/inbox/')
