from django.urls import path
from fruit.api import views as api_views

urlpatterns = [
    path("fruits/", api_views.fruit_list_create_api_view, name="fruit-listesi")
]
