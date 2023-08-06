from raceratings.models import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.pk

    class Meta:
        model = Category
        fields = (
            'id',
            'label',
            'short_label',
        )
