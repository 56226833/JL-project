# Generated by Django 2.0.1 on 2018-02-08 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180206_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='salary',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Salary', verbose_name='薪水'),
        ),
    ]
