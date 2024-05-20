from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import Booklist

urlpatterns = [

    path('book/',Booklist.as_view(),name='Booklist')
]

urlpatterns = format_suffix_patterns(urlpatterns)