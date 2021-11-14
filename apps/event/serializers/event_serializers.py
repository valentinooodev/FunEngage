from rest_framework import serializers
from apps.event.models import *


class ImagePathSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image_Paths
        field = ['image_url', 'display_order']
        #depth = 1


class EventSerializer(serializers.ModelSerializer):
    # image = ImagePathSerializer(many=True)

    class Meta:
        model = Events
        fields = ['event_id', 'type', 'title', 'is_private']

