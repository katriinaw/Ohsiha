from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.conf.urls import include, url

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('menoappi/', include('menoappi.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
