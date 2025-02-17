# Generated by Django 2.2.2 on 2019-09-06 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thesis_app', '0004_user_result_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step_1',
            name='age',
            field=models.CharField(choices=[('under_18', 'Under 18'), ('b18_24', '18_24'), ('b25_35', '25_35'), ('b35_45', '35_45'), ('b45_55', '45_55'), ('bover_55', 'Over 55')], default=None, max_length=40, verbose_name='age'),
        ),
        migrations.CreateModel(
            name='evaluate_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='evaluate_result', editable=False, max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('appealed_list', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='appealed_list')),
                ('bad_suggestions', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='bad_suggestions')),
                ('similar_result', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='similar_result')),
                ('varied_selection', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='varied_selection')),
                ('wider_preference', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='wider_preference')),
                ('better_reflection', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='wider_preference')),
                ('more_personalized', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='more_personalized')),
                ('more_mainstream', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='more_mainstream')),
                ('better_help', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='better_help')),
                ('recommended_list', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='recomend_to_Friend')),
                ('not_expect', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='not_expect')),
                ('familiar_list', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='familiar_list')),
                ('surprising_list', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='surprising_list')),
                ('fewer_suggestions', models.CharField(choices=[('List 1', 'List 1'), ('List 2', 'List 2'), ('List 3', 'List 3')], default=None, max_length=20, verbose_name='fewer_suggestions')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Evaluate_result',
                'db_table': 'Evaluate_result',
                'ordering': ['user_id'],
            },
        ),
    ]
