from django.urls import re_path
from . import views

urlpatterns = [
    re_path(
        r'^api/(?P<pk>[0-9]+)$',
        views.get_delete_update_experiment,
        name='get_delete_update_experiment'
    ),
    re_path(
        r'^api/$',
        views.get_post_experiments,
        name='get_post_experiments'
    )
]
