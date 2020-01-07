from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import logout
from django.conf.urls import url
from image_service import views

urlpatterns = [
    url(r'^$', views.translate_image, name='translate_image'),
]
