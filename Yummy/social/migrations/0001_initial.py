# Generated by Django 3.2.4 on 2021-07-08 19:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ingredients', models.TextField()),
                ('Recipe', models.TextField()),
                ('created_on', models.DateTimeField(default=datetime.datetime(2021, 7, 8, 19, 6, 43, 457291, tzinfo=utc))),
                ('auhtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
