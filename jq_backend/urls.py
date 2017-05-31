"""jq_backend URL Configuration

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
from rest_framework.routers import DefaultRouter

import student_stay_out_late.views as stayoutlateview

router = DefaultRouter()
router.register(r'passresults', stayoutlateview.PassresultsViewSet)
router.register(r'stuinfo', stayoutlateview.StuinfoViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^admin/', admin.site.urls),
    # url(r'^api/getabnormalinfo/(.*)/(.*)/', stayoutlateview.getabnormalinfo),
    # url(r'^api/getabnormalinfoall/(.*)/(.*)/', stayoutlateview.getabnormalinfoall),
    url(r'^login/(.*)/', stayoutlateview.pertendlogin),
    url(r'^getclass/', stayoutlateview.getclass),
]
