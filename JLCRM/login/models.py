from django.db import models

#工资报表
class Salary(models.Model):
    amount = models.IntegerField('工资')
    bonus = models.IntegerField('奖金')
    reimburse = models.IntegerField('报销额')

#权限等级表
class Authority(models.Model):
    level = models.CharField('权限', max_length=10)
    description = models.TextField('权限说明')
    def __str__(self):
        return self.level
    class Meta:
        verbose_name = '权限等级'
        verbose_name_plural = '权限等级'

#员工表
class Staff(models.Model):
    username = models.CharField('用户名', max_length=20)
    password = models.CharField('密码', max_length=20)
    name = models.CharField('姓名', max_length=20)
    gendar = models.CharField('性别', max_length=5)
    age = models.IntegerField('年龄')
    education = models.CharField('学历', max_length=10)
    zone = models.CharField('区域', max_length=20)
    qualification = models.CharField('职称', max_length=20)
    email = models.EmailField('E-mail', max_length=32)
    dialNumber = models.IntegerField('电话号码')
    authority = models.ForeignKey(Authority, verbose_name='权限等级', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工'

#联系人表
class Contactor(models.Model):
    name = models.CharField('姓名', max_length=20)
    gendar = models.CharField('性别', max_length=5)
    dialNumber = models.IntegerField('电话号码')
    email = models.EmailField('E-mail')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '联系人'
        verbose_name_plural = '联系人'

#项目表
class Project(models.Model):
    project_name = models.CharField('项目名称', max_length=30)
    description = models.TextField('项目内容')
    beginTime = models.DateTimeField('开始时间')
    endTime = models.DateTimeField('结束时间')
    contactor = models.ForeignKey(Contactor, verbose_name='联系人', on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(Staff, verbose_name='员工', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.project_name
    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'

#公司表
class Company(models.Model):
    name = models.CharField('公司名称', max_length=30)
    visits = models.IntegerField('拜访次数')
    lastVisitTime = models.TimeField('上次拜访时间')
    intention = models.TextField('公司意向')
    score = models.IntegerField('公司评分')
    #project = models.ForeignKey(Project, on_delete =models.CASCADE)
