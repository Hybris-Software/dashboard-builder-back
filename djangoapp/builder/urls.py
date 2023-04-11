from django.urls import path

# Views
from builder.views import Layouts


urlpatterns = [
    path('layouts/', Layouts.as_view()),
]
