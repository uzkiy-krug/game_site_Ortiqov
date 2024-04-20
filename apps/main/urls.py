from django.urls import path, include
from .views import HomeView, ContactView, CommunityView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('community/', CommunityView.as_view(), name='community'),
]