from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth.serializers import MyTokenObtainPairSerializer, MyTokenRefreshSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer
