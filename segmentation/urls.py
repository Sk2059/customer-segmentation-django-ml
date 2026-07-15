from django.urls import path

from . import views

app_name = "segmentation"

urlpatterns = [
    path("", views.predict_segment_view, name="predict"),
]
