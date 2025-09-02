from django.urls import path
from .views import UserProfileView, UserLogin, LogoutAllView

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout-all/', LogoutAllView.as_view(), name='logout-all'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]