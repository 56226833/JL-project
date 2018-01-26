from django.db import models

# Create your models here.

#联系人表
class Contactor(models.Model):
    name = models.CharField('姓名', max_length=20)
    gendar = models.IntegerField('性别')
    dialNumber = models.IntegerField('电话号码')
    email = models.EmailField('E-mail')

#项目表
class Project(models.Model):
    name = models.CharField('项目名称', max_length=30)
    description = models.TextField('项目内容')
    beginTime = models.TimeField('开始时间')
    endTime = models.TimeField('结束时间')
    contactor = models.ForeignKey(Contactor, on_delete =models.CASCADE)

#权限等级表
class Authority(models.Model):
    level = models.IntegerField('权限')
    description = models.TextField('权限说明')
    class Meta:
        verbose_name = '权限等级'
        verbose_name_plural = '权限等级'

#工资报表
class Salary(models.Model):
    amount = models.IntegerField('数目')
    bonus = models.IntegerField('奖金')
    reimburse = models.IntegerField('报销额')

#员工表
class Staff(models.Model):
    username = models.CharField('用户名', max_length=20)
    password = models.CharField('密码', max_length=20) 
    name = models.CharField('姓名', max_length=20)
    gendar = models.IntegerField('性别')
    age = models.IntegerField('年龄')
    education = models.CharField('学历', max_length=10)
    zone = models.CharField('区域', max_length=20)
    #avatar = models.ImageField('照片', upload_to='./upload/')
    qualification = models.CharField('职称', max_length=20)
    email = models.EmailField('E-mail', max_length=32)
    dialNumber = models.IntegerField('电话号码')
    authority = models.OneToOneField(Authority, on_delete =models.CASCADE)
    project = models.ForeignKey(Project, on_delete =models.CASCADE)
    salary = models.OneToOneField(Salary, on_delete =models.CASCADE)
    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工'

#公司表
class Company(models.Model):
    name = models.CharField('公司名称', max_length=30)
    visits = models.IntegerField('拜访次数')
    lastVisitTime = models.TimeField('上次拜访时间')
    intention = models.TextField('公司意向')
    score = models.IntegerField('公司评分')
    project = models.ForeignKey(Project, on_delete =models.CASCADE)
