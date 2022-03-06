# Generated by Django 4.0.3 on 2022-03-06 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('member_since', models.CharField(max_length=30)),
                ('email_id', models.CharField(default=None, max_length=50)),
                ('about_me', models.CharField(max_length=800)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('breeds', models.CharField(default=None, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]