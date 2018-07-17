"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from .views import home_page, about_page, services_page, portfolio_page, pricing_page, contact_page
from blog.views import PostListView, PostDetailSlugView, comment

urlpatterns = [
    url(r'^$', home_page, name='Home'),
    url(r'^about/$', about_page, name='About'),
    url(r'^services/$', services_page, name='Services'),
    url(r'^portfolio/$', portfolio_page, name='Portfolio'),
    url(r'^pricing/$', pricing_page, name='Pricing'),
    url(r'^blog/$', PostListView.as_view(), name='Blog'),
    url(r'^Comment/$', comment, name='Comment'),
    url(r'^blog/(?P<slug>[\w-]+)/$', PostDetailSlugView.as_view(), name='post-detail'),
    url(r'^contact/$', contact_page, name='Contact'),
    url(r'^admin/', admin.site.urls),
]

contact_page
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)