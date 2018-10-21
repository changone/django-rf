# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class MaintenanceNotice(models.Model):

    # _database = 'testdb'


    id = models.IntegerField(primary_key=True,db_column='id')
    editer = models.CharField('修改人', max_length=50, db_column='editer', null=True)
    edit_dt = models.DateTimeField('编辑日期', db_column='edit_dt', null=True)
    content = models.TextField('维护内容', db_column='content')
    end_dt = models.DateTimeField('维护结束时间', db_column='end_dt')

    class Meta:
        db_table = 't_maintenance_notice'


    # def __init__(self, edit_end_dt, content, edit_dt, editer,id):
    #     self.editer = ''
    #     self.edit_dt = datetime.now()
    #     self.content = content
    #     self.edit_end_dt = edit_end_dt
