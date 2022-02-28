from django.urls import path
from . views import *


urlpatterns = [
    path('', TestingView.as_view()),
]
