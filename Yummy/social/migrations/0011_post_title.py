# Generated by Django 3.2.4 on 2021-08-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Title',
            field=models.CharField(default='Title', max_length=50),
        ),
    ]
