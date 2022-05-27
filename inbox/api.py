from django.urls import path, include

from rest_framework import viewsets
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import MessageSerializer
from .models import Message


class MyMessageViewSet(viewsets.ReadOnlyModelViewSet):
    """ Message api viewset """
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user)

    @action(detail=True, methods=['POST'])
    def read(self, request, pk=None):
        obj = self.get_object()
        obj.is_read = True
        obj.save()
        serializer = MessageSerializer(obj)
        return Response(serializer.data)


router = routers.DefaultRouter()
router.register('', MyMessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls))
]
