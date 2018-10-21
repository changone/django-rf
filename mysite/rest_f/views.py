# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import MaintenanceNotice
from .serializer import MaintenanceSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.settings import api_settings



class MaintenanceViewset(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = MaintenanceNotice.objects.all()
    serializer_class = MaintenanceSerializers

    # def get_queryset(self):
    #     print '111'
    #     return self.queryset.all()

    # def get(self, request, *args, **kwargs):
    #     print '222'
    #     return self.queryset.all()


    # def create(self, request, *args, **kwargs):
    #     print 'create'
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     print 'perform_create'
    #     serializer.save()
    #
    # def get_success_headers(self, data):
    #     print 'get_success_headers'
    #     try:
    #         return {'Location': str(data[api_settings.URL_FIELD_NAME])}
    #     except (TypeError, KeyError):
    #         return {}
    #
    # def retrieve(self, request, *args, **kwargs):
    #     print 'retrieve'
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # def update(self, request, *args, **kwargs):
    #     print 'update'
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #
    #     return Response(serializer.data)
    #
    # def perform_update(self, serializer):
    #     print 'perform_update'
    #     serializer.save()