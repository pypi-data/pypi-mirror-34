from rest_framework import serializers

from raceratings.models import RaceRating
from .category import CategorySerializer


class RaceRatingSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        return CategorySerializer(obj.category).data

    class Meta:
        model = RaceRating
        fields = (
            'pk',
            'created_date',
            'category',
            'explanation',
            'incumbent'
        )


class RaceRatingHomeSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.pk

    class Meta:
        model = RaceRating
        fields = (
            'id',
            'created_date',
            'category',
            'explanation',
            'incumbent',
            'race'
        )


class RaceRatingAdminSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()

    def get_rating(self, obj):
        return obj.category.short_label

    class Meta:
        model = RaceRating
        fields = (
            'pk',
            'created_date',
            'rating',
            'explanation',
            'incumbent'
        )
