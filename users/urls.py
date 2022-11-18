from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path("users/", views.UsersViewSet.as_view({'get': 'list'})),
])
