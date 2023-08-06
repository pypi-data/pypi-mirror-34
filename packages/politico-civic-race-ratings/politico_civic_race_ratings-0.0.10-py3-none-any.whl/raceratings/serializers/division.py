
import us
from geography.models import Division, DivisionLevel
from rest_framework import serializers


class ChildDivisionSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField
    level = serializers.SerializerMethodField()
    postal_code = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.uid

    def get_postal_code(self, obj):
        if obj.level.name == 'state':
            return us.states.lookup(obj.code).abbr
        return None

    def get_level(self, obj):
        return obj.level.slug

    class Meta:
        model = Division
        fields = (
            'id',
            'label',
            'short_label',
            'code',
            'postal_code',
            'level',
        )


class DivisionSerializer(ChildDivisionSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        districts = obj.children.filter(
            level__name=DivisionLevel.DISTRICT
        )

        return ChildDivisionSerializer(districts, many=True).data

    class Meta:
        model = Division
        fields = (
            'id',
            'label',
            'short_label',
            'code',
            'level',
            'postal_code',
            'children',
        )
