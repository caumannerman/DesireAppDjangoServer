from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.forms.fields import ImageField
from rest_framework import serializers
from design_fields.models import DesignField

from design_fields.serializers import DesignFieldSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    design_fields = DesignFieldSerializer(
        many=True, queryset=DesignField.objects.filter())
    profile_image = ImageField(allow_empty_file=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'nickname', 'design_fields',
                  'profile_image', 'profile_image', 'acc_type', )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        design_fields_data = []
        if validated_data.get('design_fields'):
            design_fields_data = validated_data.pop('design_fields')
        else:
            raise serializers.ValidationError(
                {'design_fields': ['This field is required.']}, code=400)

        user = User.objects.create(**validated_data)

        for design_field_data in design_fields_data:
            design_field_qs = DesignField.objects.filter(
                name__iexact=design_field_data)
            design_field = design_field_qs.first()
            user.design_fields.add(design_field)

        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        design_fields_data = []
        if validated_data.get('design_fields'):
            design_fields_data = validated_data.pop('design_fields')
        else:
            raise serializers.ValidationError(
                {'design_fields': ['This field is required.']}, code=400)

        # 비밀번호도 변경하는 경우
        if validated_data.get('password'):
            password_data = validated_data.pop('password')
            instance.set_password(password_data)

        # 사용자 정보 업데이트
        for key, value in validated_data.items():
            setattr(instance, key, value)

        for design_field_data in design_fields_data:
            design_field_qs = DesignField.objects.filter(
                name__iexact=design_field_data)
            design_field = design_field_qs.first()
            instance.design_fields.add(design_field)

        instance.save()
        return instance
