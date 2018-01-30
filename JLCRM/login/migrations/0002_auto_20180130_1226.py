# Generated by Django 2.0.1 on 2018-01-30 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactor',
            options={'verbose_name': '联系人', 'verbose_name_plural': '联系人'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '项目', 'verbose_name_plural': '项目'},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='project_name',
        ),
        migrations.AddField(
            model_name='project',
            name='contactor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Contactor', verbose_name='联系人'),
        ),
        migrations.AddField(
            model_name='staff',
            name='authority',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Authority', verbose_name='权限等级'),
        ),
        migrations.AlterField(
            model_name='authority',
            name='level',
            field=models.CharField(max_length=10, verbose_name='权限'),
        ),
        migrations.AlterField(
            model_name='contactor',
            name='gendar',
            field=models.CharField(max_length=5, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='project',
            name='beginTime',
            field=models.DateTimeField(verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='project',
            name='endTime',
            field=models.DateTimeField(verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='gendar',
            field=models.CharField(max_length=5, verbose_name='性别'),
        ),
    ]
