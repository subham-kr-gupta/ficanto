# Generated by Django 4.1.1 on 2022-09-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_corporate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
