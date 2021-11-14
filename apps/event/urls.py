from rest_framework.routers import DefaultRouter
from django.urls import path, include
from apps.event.views import *


router = DefaultRouter()
router.register('', EventListAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
