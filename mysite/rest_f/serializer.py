# encoding=utf-8

from rest_framework import serializers
from .models import MaintenanceNotice
import datetime

class MaintenanceSerializers(serializers.Serializer):

    end_dt = serializers.DateTimeField()
    content = serializers.CharField()

    class Meta:
        model = MaintenanceNotice
        fields = ( 'content', 'end_dt')

    # def create(self, validated_data):
    #     print 'serializers create'
    #     print validated_data
    #     return MaintenanceNotice(**validated_data)
    #
    def update(self, instance, validated_data):
        print 'serializers update'
        instance.id = 1
        instance.editer = ''
        instance.edit_dt = datetime.datetime.utcnow()
        instance.content = validated_data.get('content', instance.content)
        instance.end_dt = validated_data.get('end_dt', instance.edit_dt)
        instance.save()
        return instance