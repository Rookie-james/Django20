from django20.urls import path
from day04 import views

urlpatterns = [
    path('if/<str:name>/',views.if_view),
    path('for/',views.for_view),
    path('link/<version>/',views.url_view),
    path('base/',views.base_view),
    path('include/',views.include_view),
]