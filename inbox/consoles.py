from django.shortcuts import render, redirect
from django.urls import path
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from utils.utils import admins_only
from utils.mixins import SearchMixin
from .models import Record
from .forms import MessageForm


class RecordListView(LoginRequiredMixin, SearchMixin, ListView):
    model = Record
    search_fields = ('title', 'body')
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()
        return self.search_queryset(self.request, qs)

    def get_context_data(self):
        context = super().get_context_data()
        title = '发送记录'
        context['title'] = title
        context['breadcrumbs'] = [
            ('首页', '/console/index/'),
            ('发送消息', '/console/inbox/send/'),
            (title,)
        ]
        return context


@login_required
@user_passes_test(admins_only)
def send_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.send(request.user)
            messages.success(request, '发送成功')
            return redirect(request.path)

    else:
        form = MessageForm()

    context = {
        'title': '发送消息',
        'form': form,
    }
    return render(request, 'inbox/message_form.html', context)



urlpatterns = [
    path('send/', send_message_view),
    path('send/record/', RecordListView.as_view()),
]
