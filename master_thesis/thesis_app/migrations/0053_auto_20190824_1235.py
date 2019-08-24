# Generated by Django 2.2.2 on 2019-08-24 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thesis_app', '0052_auto_20190824_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_rate',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
