# encoding=utf-8

from rest_framework.routers import SimpleRouter
import views

# api_router = SimpleRouter()
#
# api_router.register(r'test2', views.MaintenanceViewset,
#                     basename='test2')

from django.conf.urls import url

from .views import MaintenanceViewset

urlpatterns = [
    # url(r'test/$', MaintenanceViewset.as_view({'get': 'list'}), name='notice'),
    url(r'test/(?P<pk>\d*)$', MaintenanceViewset.as_view({'get': 'list', 'put': 'update'}), name='setnotice'),
]

