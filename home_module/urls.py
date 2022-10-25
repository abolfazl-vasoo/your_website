from django.urls import path
from home_module.views import ContactPage
from . import views

urlpatterns = [
    path('', views.index),
    # path('', IndexPage.as_view()),
    path('contact', ContactPage.as_view()),

]

# IndexPage,