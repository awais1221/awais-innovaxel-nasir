
from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ('short_code', 'url', 'created_at', 'updated_at', 'access_count')


