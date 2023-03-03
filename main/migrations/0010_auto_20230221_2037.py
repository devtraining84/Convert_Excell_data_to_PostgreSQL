# Generated by Django 3.2.12 on 2023-02-21 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_subgroupmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubGroupNameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=32)),
            ],
        ),
        migrations.RemoveField(
            model_name='subgroupmodel',
            name='group',
        ),
    ]
