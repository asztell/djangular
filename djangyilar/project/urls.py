"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from core.views import SampleView, AngularApp, NgTemplateView, ComingSoonView, contact
# from .views import 


ngurls = [
    url(r'^$', SampleView.as_view(), name='sample'),
    url(r'^ng/$', NgTemplateView.as_view(), name='ngTemplate'),
    url(r'^comingsoon/$', ComingSoonView.as_view()),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sample/', include(ngurls)),
    url(r'^contact', contact, name='contact'),
    url(r'^(?!ng/).*$', AngularApp.as_view(), name="angular_app"),
] + static(settings.ANGULAR_URL, document_root=settings.ANGULAR_ROOT)
