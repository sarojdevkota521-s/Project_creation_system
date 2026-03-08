from django.urls import path
from .views import EmailTOkenView, RegisterView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', EmailTOkenView.as_view(), name='token_obtain_pair'),
]