# Generated by Django 3.2.12 on 2023-02-21 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20230221_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subgroupmodel',
            name='rider',
        ),
        migrations.DeleteModel(
            name='SubGroupNameModel',
        ),
        migrations.DeleteModel(
            name='SubGroupModel',
        ),
    ]
