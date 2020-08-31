from django.urls import path, re_path
from day01.views import view_func,view_re_func
from day01.views import view_func_v1,view_template,\
    view_template_2,view_template_3,view_template_4,\
    view_template_5,view_json

urlpatterns = [
    path("view/name/", view_func, name='v0'),
    path("view/v1/", view_func_v1, name='v1'),
    re_path("^9\d{4}/$",view_re_func),
    path("temp/",view_template),
    path("temp_v1/",view_template_2),
    path("day01/",view_template_3),
    path("user/<username>",view_template_4),
    path("img/",view_template_5),
    path("json/",view_json),
]