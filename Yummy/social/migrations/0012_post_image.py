# Generated by Django 3.2.4 on 2021-08-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/post_photos'),
        ),
    ]
