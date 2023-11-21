from django.urls import path
from . import views

urlpatterns = [
    path(
        "consumers", 
        views.index, 
        name="index",
    ),
    path(
        "consumers/min_previous_jobs_count=<int:min_previous_jobs_count>", 
        views.index, 
        name="index",
    ),
    path(
        "consumers/max_previous_jobs_count=<int:max_previous_jobs_count>", 
        views.index, 
        name="index",
    ),
    path(
        "consumers/status=<str:status>", 
        views.index, 
        name="index",
    ),
    path(
        "consumers/min_previous_jobs_count=<int:min_previous_jobs_count>&max_previous_jobs_count=<int:max_previous_jobs_count>", 
        views.index, 
        name="index",
    ),
    path(
        "consumers/min_previous_jobs_count=<int:min_previous_jobs_count>&status=<str:status>", 
        views.index, 
        name="index",
    ),
    path(
        "consumers/min_previous_jobs_count=<int:min_previous_jobs_count>&max_previous_jobs_count=<int:max_previous_jobs_count>&status=<str:status>", 
        views.index, 
        name="index",
    ),
    path(
        "consumers/max_previous_jobs_count=<int:max_previous_jobs_count>&status=<str:status>", 
        views.index, 
        name="index",
    ),
]
