from django.urls import path
from .views import home_page_view
from . import views

urlpatterns = [
    path("", home_page_view),
    path("", views.home_page_view, name="playground-home"),
]


"""[
    path('hello', views.say_hello),
]"""

#  path('hello/', views.say_hello, name='hello'),
