import jwt

from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = {
            'id': self.user.id,
            'acc_type': self.user.acc_type,
        }
        return data


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user_id = jwt.decode(data.get('refresh'), settings.SECRET_KEY, algorithms=[
                             "HS256"])['user_id']
        self.user = User.objects.get(id=user_id)

        # Add custom claims
        data['user'] = {
            'id': self.user.id,
            'acc_type': self.user.acc_type,
        }

        return data
