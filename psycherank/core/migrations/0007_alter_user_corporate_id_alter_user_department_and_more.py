# Generated by Django 4.1.1 on 2022-09-24 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_questionnaire_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='corporate_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.corporateuser'),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='resume',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
