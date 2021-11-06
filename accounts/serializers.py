from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db.models import fields
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        # 비밀번호도 변경하는 경우
        if 'password' in validated_data:
            validated_data['password'] = make_password(
                validated_data['password'])

        # 사용자 정보 업데이트
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance
