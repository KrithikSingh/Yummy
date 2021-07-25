# Generated by Django 3.2.4 on 2021-07-10 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('social', '0005_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user', verbose_name='user')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('picture', models.ImageField(default='uploads/profile_pictures/default.png', upload_to='uploads/profile_pictures')),
            ],
        ),
    ]
