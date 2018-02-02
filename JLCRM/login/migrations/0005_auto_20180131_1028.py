# Generated by Django 2.0.1 on 2018-01-31 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20180130_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': '单位', 'verbose_name_plural': '单位'},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='salary',
            name='amount',
            field=models.IntegerField(verbose_name='工资'),
        ),
    ]
