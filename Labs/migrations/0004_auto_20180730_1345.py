# Generated by Django 2.0.7 on 2018-07-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Labs', '0003_auto_20180730_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labtasks',
            name='task_number',
            field=models.IntegerField(null=True),
        ),
    ]
