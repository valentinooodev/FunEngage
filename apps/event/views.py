from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination

from apps.event.models import *
from apps.event.serializers.event_serializers import *


class EventListSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'perpage'
    max_page_size = 1000


class EventListAPIView(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    pagination_class = EventListSetPagination
