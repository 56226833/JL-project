# Generated by Django 2.0.1 on 2018-02-08 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20180208_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='amount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='工资'),
        ),
    ]
