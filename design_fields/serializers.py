from rest_framework import serializers

from design_fields.models import DesignField


class DesignFieldSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

    def to_internal_value(self, data):
        try:
            return DesignField.objects.get(name=data)
        except:
            raise serializers.ValidationError(
                'Invalid design field name.', code=400)

    class Meta:
        model = DesignField
        fields = ('id', 'name', )
