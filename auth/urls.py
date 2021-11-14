from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

from auth.views import MyTokenObtainPairView, MyTokenRefreshView

app_name = 'auth'

urlpatterns = [
    # rest_framework_simplejwt
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
