from django.shortcuts import get_object_or_404
from django.urls import reverse
from election.models import ElectionDay, Race
from raceratings.conf import settings
from raceratings.models import (BadgeType, Category, RaceBadge,
                                RaceRating, RatingPageContent)
from raceratings.serializers import (RaceHomeSerializer,
                                     RaceRatingHomeSerializer,
                                     CategorySerializer,
                                     BadgeTypeSerializer,
                                     RaceBadgeHomeSerializer)

from .base import BaseView


class Home(BaseView):
    name = 'raceratings_home-page'
    path = ''

    js_dev_path = 'raceratings/js/main-home-app.js'
    css_dev_path = 'raceratings/css/main-home-app.css'

    model = ElectionDay
    context_object_name = 'election_day'
    template_name = "raceratings/home.html"

    def get_queryset(self):
        return self.model.objects.all()

    def get_object(self, **kwargs):
        return get_object_or_404(ElectionDay, slug='2018-11-06')

    def get_publish_path(self):
        return 'election-results/2018/ratings'

    def get_serialized_data(self):
        races = Race.objects.filter(cycle__slug='2018')
        race_data = RaceHomeSerializer(races, many=True).data

        ratings = RaceRating.objects.all()
        ratings_data = RaceRatingHomeSerializer(ratings, many=True).data

        categories = Category.objects.all()
        categories_data = CategorySerializer(categories, many=True).data

        badges = RaceBadge.objects.all()
        badges_data = RaceBadgeHomeSerializer(badges, many=True).data

        badge_types = BadgeType.objects.all()
        badge_types_data = BadgeTypeSerializer(badge_types, many=True).data

        content = RatingPageContent.objects.home_content()

        return {
            'races': race_data,
            'ratings': ratings_data,
            'categories': categories_data,
            'badges': badges_data,
            'badge_types': badge_types_data,
            'content': content
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['secret'] = settings.SECRET_KEY
        return {
            **context,
            **self.get_paths_context(production=context['production'])
        }

    def get_extra_static_paths(self, production):
        if production:
            return {
                'data': 'data.json'
            }
        return {
            'data': reverse('raceratings_api_home')
        }
