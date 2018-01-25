from django.db import models

# Create your models here.
#用户表
class User(models.Model):
    userId = modesl.CharField('用户名', max_length=20)
    password = models.IntegerField('密码', max_length=20)
    name = models.CharField('姓名', max_length=20, default=self.userId)
    email = models.EmailField('E-mail', max_length=32)
    authorityLevel = models.ForeignKey('level')


#员工表
class Staff(models.Model):
    name = models.CharField('姓名', max_length=20)
    gendar = models.IntegerField('性别', max_length=1)
    age = models.IntegerField('年龄', max_length=3)
    education = models.CharField('学历', max_length=10)
    zone = models.CharField('区域')
    avatar = models.FileField('照片', upload_to='/upload/')
    qualification = models.CharField('职称')


#权限等级表
class Authority(models.Model):
    level = models.IntegerField('权限', max_length=5, Blank=True)
    description = models.TextField('权限说明', Blank=True)


#项目表
class Project(modesl.Model):
    name = models.CharField('项目名称', max_length=30)
    description = models.TextField('项目内容', Blank=True)
    beginTime = models.TimeField('开始时间', Blank=True, null=True)
    endTime = models.TimeField('结束时间', Blank=True, null=True)


#客户表
class Customer(models.Model):
    company = models.CharField('客户单位')
    contactor = models.CharField('联系人', max_length=20)
    dialNumber = models.IntegerField('电话号码', max_length=20)
