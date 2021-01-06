from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-Overview"),
    path('show-list/', views.showList, name="show-List"),
    path('add-list/', views.addList, name="add-List"),
]
