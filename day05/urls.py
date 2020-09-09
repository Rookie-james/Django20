from django20.urls import path
from . import views

urlpatterns = [
    path('filter/',views.view_filter),
    path('include/tag/',views.include_tag_view),
    path('include/tag/new/',views.include_tag_new),
]