from django.conf.urls import url, include
from django.contrib import admin
from shortens import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'accounts/', include('accounts.urls')),
    url(r'shortens/', include('shortens.urls')),
    url('^$', views.home, name='home'),
    url(r'.{5}', views.shortened, name='shortened')
]
