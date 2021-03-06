# Generated by Django 2.1.5 on 2022-03-19 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatProfile',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('breed', models.CharField(max_length=50)),
                ('price_range', models.CharField(max_length=30)),
                ('friendliness', models.FloatField(default=3.0)),
                ('tidiness', models.FloatField(default=3.0)),
                ('fussiness', models.FloatField(default=3.0)),
                ('description', models.CharField(default='', max_length=800)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=800)),
                ('likes', models.IntegerField(default=0)),
                ('postdate', models.DateField(auto_now_add=True, null=True)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.CatProfile')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile')),
            ],
        ),
    ]
