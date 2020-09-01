from django20.urls import path
from day04.views import if_view

urlpatterns = [
    path('if/<str:name>/',if_view)
]