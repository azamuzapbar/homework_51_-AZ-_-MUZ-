from django.urls import path
from webapp import views

urlpatterns = [
    path('',views.index_view),
    path('view/add/',views.add_view),
]