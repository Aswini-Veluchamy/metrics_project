from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_metrics, name="create_metrics"),
    path('correlation_table/', views.correlation_table, name="correlation_table"),
]
