from django.conf.urls import url
from . import views

app_name = 'shortens'
urlpatterns = [
    url(r'create/', views.create, name='create'),
    url(r'check/', views.check, name='check'),
]
