from django.contrib import admin

# Register your models here.
from django.contrib.admin import register
from import_export import fields
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.formats import base_formats
from import_export.widgets import ForeignKeyWidget
from import_export import resources
from twentyFour.models import *

class ResumeAdminResource(resources.ModelResource):
    pass
    class Meta:
        model = Resume
        fields = "__all__"

@register(Resume)
class ResumeAdmin(ImportExportModelAdmin):
    change_list_template='change_list_call.html'
    resource_class = ResumeAdminResource
    list_display = ('phone','name','sex','educationBackgroud','createDateTime','states','callNum','lastDateTime','callPhone')
    list_filter=('educationBackgroud','states')
    def callNum(self,obj):
        return obj.callhistory_set.count()
    def lastDateTime(self,obj):
        if(obj.callhistory_set.all()):
            return obj.callhistory_set.latest('createDateTime').createDateTime
    callNum.short_description = '拨打次数'
    lastDateTime.short_description="最后拨打时间"






@register(CallHistory)
class CallHistoryAdmin(admin.ModelAdmin):
    list_display = ('createDateTime','state','remark')

    list_filter = ('state',)

