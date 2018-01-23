from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.utils.html import format_html


class Resume(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(default=0)
    educationBackgroudChoices = ((0, '大专以下'), (1, "大专"), (2, "本科"))
    educationBackgroud = models.IntegerField("学历", choices=educationBackgroudChoices, default=0)
    sexChoices = ((0, "男"), (1, "女"))
    sex = models.IntegerField("性别", choices=sexChoices, default=0)
    states = models.BooleanField('能否拨打',default=True)
    createDateTime = models.DateTimeField('创建日期', auto_now_add=True)
    url=models.URLField("简历地址",blank=True)
    def __str__(self):
        return self.name

    def callPhone(self):
        return format_html('<a class="call" data-id="{}" href="tel:{}?call">拨打电话</a>',self.id,self.phone)

    callPhone.short_description = '拨打电话'
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.url="http://jianli.58.com/resumedetail/batch/"+self.url
        return  super(Resume,self).save(force_insert=force_insert,force_update=force_update,using=using,update_fields=update_fields)


class CallHistory(models.Model):
    resume = models.ForeignKey(Resume, on_delete=CASCADE)
    createDateTime = models.DateTimeField(u'创建日期', auto_now_add=True)
    stateChoices = ((0, '同意'),(1, "待定"),(2, '不同意'))
    state = models.IntegerField("意愿", choices=stateChoices, default=2)
    remark = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.resume.name
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.state==2 or self.state==0:
            self.resume.states=False

        elif self.state==1:
            self.resume.states=True
        self.resume.save()
        return super(CallHistory,self).save(force_insert=force_insert,force_update=force_update,using=using,update_fields=update_fields)
