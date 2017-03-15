from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .rest_api.view_set import *
from .views.SofthubIndex import SofthubIndex
from .views.OperatingSystemDetail import OperatingSystemDetail
from .views.ApplicationDetail import ApplicationDetail
from .views.ApplicationUpload import ApplicationUpload
from .views.ApplicationUpdate import ApplicationUpdate
from .views.VersionUpload import VersionUpload
from .views.ExecutableUpload import ExecutableUpload
from .views.UserCreation import UserCreation


app_name = 'softhub'

urlpatterns = [
    url(r'^$',
        SofthubIndex.as_view(),
        name='index'),

    url(r'^os/(?P<pk>[0-9]+)/$',
        OperatingSystemDetail.as_view(),
        name='os_detail'),

    url(r'^app/(?P<pk>[0-9]+)/$',
        ApplicationDetail.as_view(),
        name='app_detail'),

    url(r'^upload/app/',
        # login is required, and it's done via a
        # decorator inside ApplicationUpload class.
        ApplicationUpload.as_view(),
        name='app_upload'),

    url(r'^upload/app_version/',
        login_required(VersionUpload.as_view()),
        name='app_version_upload'),

    url(r'^upload/app_executable/',
        login_required(ExecutableUpload.as_view()),
        name='app_executable_upload'),

    url(r'^app/(?P<pk>[0-9]+)/update/',
        login_required(ApplicationUpdate.as_view()),
        name='app_update'),
]


# Authentication URLS
# https://docs.djangoproject.com/en/1.10/topics/auth/default/#module-django.contrib.auth.views
urlpatterns += [
    url(r'^', include('django.contrib.auth.urls')),

    url(r'^register/',
        UserCreation.as_view(),
        name='create_user'),
]


# REST router
router = DefaultRouter()
router.register(r'os', OperatingSystemViewSet)
router.register(r'app', ApplicationViewSet)
router.register(r'version', VersionViewSet)
router.register(r'executable', ExecutableViewSet)
router.register(r'developer', DeveloperViewSet)

urlpatterns += [
    url(r'^api/',
        include(router.urls)),
]
