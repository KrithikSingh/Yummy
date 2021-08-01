# Generated by Django 3.2.4 on 2021-07-31 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0009_comment_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parents',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='social.comment'),
        ),
    ]
