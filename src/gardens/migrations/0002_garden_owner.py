# Generated by Django 3.1 on 2020-09-01 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gardens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='garden',
            name='owner',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gardens', to=settings.AUTH_USER_MODEL),
        ),
    ]
