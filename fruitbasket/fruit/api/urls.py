from django.urls import path
from fruit.api import views as api_views


#### CLASS BASED VIEWS
urlpatterns = [
    path("fruits/", api_views.FruitListCreateAPIVıew.as_view(), name="fruit-listesi"),
    path("fruits/<int:pk>", api_views.FruitDetailAPIView.as_view(), name="fruit-detay"),
]

#### FUNCTIONAL BASED VIEWS
# urlpatterns = [
#     path("fruits/", api_views.fruit_list_create_api_view, name="fruit-listesi"),
#     path("fruits/<int:pk>", api_views.fruit_detail_api, name="fruit-detay"),
# ]
