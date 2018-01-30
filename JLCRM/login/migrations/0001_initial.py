# Generated by Django 2.0.1 on 2018-01-28 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(verbose_name='权限')),
                ('description', models.TextField(verbose_name='权限说明')),
            ],
            options={
                'verbose_name': '权限等级',
                'verbose_name_plural': '权限等级',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='公司名称')),
                ('visits', models.IntegerField(verbose_name='拜访次数')),
                ('lastVisitTime', models.TimeField(verbose_name='上次拜访时间')),
                ('intention', models.TextField(verbose_name='公司意向')),
                ('score', models.IntegerField(verbose_name='公司评分')),
            ],
        ),
        migrations.CreateModel(
            name='Contactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('gendar', models.IntegerField(verbose_name='性别')),
                ('dialNumber', models.IntegerField(verbose_name='电话号码')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='项目名称')),
                ('description', models.TextField(verbose_name='项目内容')),
                ('beginTime', models.TimeField(verbose_name='开始时间')),
                ('endTime', models.TimeField(verbose_name='结束时间')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='数目')),
                ('bonus', models.IntegerField(verbose_name='奖金')),
                ('reimburse', models.IntegerField(verbose_name='报销额')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('gendar', models.IntegerField(verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('education', models.CharField(max_length=10, verbose_name='学历')),
                ('zone', models.CharField(max_length=20, verbose_name='区域')),
                ('qualification', models.CharField(max_length=20, verbose_name='职称')),
                ('email', models.EmailField(max_length=32, verbose_name='E-mail')),
                ('dialNumber', models.IntegerField(verbose_name='电话号码')),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
            },
        ),
    ]