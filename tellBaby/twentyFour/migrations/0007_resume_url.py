# Generated by Django 2.0 on 2018-01-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twentyFour', '0006_resume_createdatetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='url',
            field=models.URLField(blank=True, verbose_name='简历地址'),
        ),
    ]
