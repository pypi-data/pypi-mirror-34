from django.core.exceptions import ObjectDoesNotExist
from election.models import Race
from geography.models import DivisionLevel
from rest_framework import serializers
from rest_framework.reverse import reverse

from raceratings.models import RatingPageContent
from .race_rating import RaceRatingSerializer, RaceRatingAdminSerializer
from .race_badge import RaceBadgeSerializer


class RaceListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return reverse(
            'raceratings_api_race-detail',
            request=self.context['request'],
            kwargs={
                'pk': obj.pk
            })

    class Meta:
        model = Race
        fields = (
            'url',
            'uid',
            'label'
        )


class RaceSerializer(serializers.ModelSerializer):
    ratings = serializers.SerializerMethodField()
    badges = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    office = serializers.SerializerMethodField()

    def get_ratings(self, obj):
        return RaceRatingSerializer(obj.ratings, many=True).data

    def get_badges(self, obj):
        return RaceBadgeSerializer(obj.badges, many=True).data

    def get_content(self, obj):
        return RatingPageContent.objects.race_content(obj)

    def get_office(self, obj):
        if not obj.office.body:
            label = obj.office.label
        else:
            if obj.office.body.slug == 'senate':
                label = '{} Senate'.format(obj.office.division.label)
            elif obj.office.body.slug == 'house':
                label = '{}, District {}'.format(
                    obj.office.division.parent.label, obj.office.division.code
                )

        if obj.special:
            label = '{}, Special Election'.format(label)

        return label

    class Meta:
        model = Race
        fields = (
            'uid',
            'ratings',
            'badges',
            'content',
            'office',
        )


class RaceHomeSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    office = serializers.SerializerMethodField()
    abbrev = serializers.SerializerMethodField()
    division = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    body = serializers.SerializerMethodField()
    latest_rating = serializers.SerializerMethodField()
    incumbent_rating = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.uid

    def get_office(self, obj):
        if not obj.office.body:
            label = obj.office.label
        else:
            if obj.office.body.slug == 'senate':
                label = '{} Senate'.format(obj.office.division.label)
            elif obj.office.body.slug == 'house':
                label = '{}, District {}'.format(
                    obj.office.division.parent.label, obj.office.division.code
                )

        if obj.special:
            label = '{}, Special Election'.format(label)

        return label

    def get_abbrev(self, obj):
        # for easier search
        if obj.office.division.level.slug == DivisionLevel.DISTRICT:
            postal = obj.office.division.parent.code_components['postal']
            code = int(obj.office.division.code)
            return '{}-{}'.format(postal, code)
        else:
            return obj.office.division.code_components['postal']

    def get_division(self, obj):
        return obj.office.division.label

    def get_state(self, obj):
        if obj.office.division.level.name == DivisionLevel.DISTRICT:
            return obj.office.division.parent.label
        else:
            return obj.office.division.label

    def get_body(self, obj):
        if obj.office.body:
            return obj.office.body.slug
        else:
            return 'governor'

    def get_latest_rating(self, obj):
        try:
            latest = obj.ratings.filter(incumbent=False).latest('created_date')
            return latest.category.pk
        except ObjectDoesNotExist:
            return None

    def get_incumbent_rating(self, obj):
        try:
            incumbent = obj.ratings.get(incumbent=True)
            return incumbent.category.pk
        except ObjectDoesNotExist:
            return None

    class Meta:
        model = Race
        fields = (
            'id',
            'office',
            'abbrev',
            'division',
            'state',
            'body',
            'latest_rating',
            'incumbent_rating'
        )


class RaceAdminSerializer(serializers.ModelSerializer):
    ratings = serializers.SerializerMethodField()
    badges = serializers.SerializerMethodField()
    office = serializers.SerializerMethodField()

    # a bunch of search fields
    abbrev = serializers.SerializerMethodField()
    code = serializers.SerializerMethodField()

    def get_ratings(self, obj):
        return RaceRatingAdminSerializer(
            obj.ratings.order_by('created_date', 'pk'), many=True
        ).data

    def get_badges(self, obj):
        return RaceBadgeSerializer(obj.badges, many=True).data

    def get_office(self, obj):
        if obj.office.body and obj.office.body.slug == 'senate':
            label = '{} {}'.format(obj.office.division.label, 'Senate')
        else:
            label = obj.office.label

        if obj.special:
            return '{} Special'.format(label)
        else:
            return label

    def get_abbrev(self, obj):
        # for easier search
        if obj.office.division.level.slug == DivisionLevel.DISTRICT:
            postal = obj.office.division.parent.code_components['postal']
            code = int(obj.office.division.code)
            return '{}-{}'.format(postal, code)
        else:
            postal = obj.office.division.code_components['postal']

            if obj.office.body:
                return '{}-{}'.format(postal, 'sen')
            else:
                return '{}-{}'.format(postal, 'gov')

    def get_code(self, obj):
        if obj.office.division.level.slug == DivisionLevel.DISTRICT:
            return int(obj.office.division.code)
        else:
            return 0

    class Meta:
        model = Race
        fields = (
            'uid',
            'ratings',
            'badges',
            'office',
            'abbrev',
            'code',
            'special'
        )
