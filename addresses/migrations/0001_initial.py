# Generated by Django 3.0.7 on 2020-07-08 01:39

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
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=140)),
                ('exterior_number', models.PositiveIntegerField()),
                ('internal_number', models.PositiveIntegerField(blank=True, null=True)),
                ('colony', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=140)),
                ('state', models.CharField(max_length=140)),
                ('coutry', models.CharField(max_length=140)),
                ('postal_code', models.CharField(max_length=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
