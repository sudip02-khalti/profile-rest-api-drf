from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import *


router = DefaultRouter()
router.register('hello-viewset', viewsetclass, base_name='view-sets')
router.register('profile', UserProfileViewsets)
urlpatterns = [
    # path('', TestingView.as_view()),
    path('', include(router.urls)),
]
