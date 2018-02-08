from django.db import models

#权限等级表
class Authority(models.Model):
    authority_level = models.CharField('权限', max_length=10, null=True)
    authority_description = models.TextField('权限说明')
    def __str__(self):
        return self.authority_level
    class Meta:
        verbose_name = '权限等级'
        verbose_name_plural = '权限等级'

#员工表
class Staff(models.Model):
    username = models.CharField('用户名', max_length=20, unique=True)
    password = models.CharField('密码', max_length=20)
    staff_name = models.CharField('姓名', max_length=20)
    staff_gendar = models.CharField('性别', max_length=5)
    age = models.IntegerField('年龄', null=True, blank=True)
    education = models.CharField('学历', max_length=10, null=True, blank=True)
    staff_zone = models.CharField('区域', max_length=20, null=True, blank=True)
    qualification = models.CharField('职称', max_length=20, null=True, blank=True)
    staff_email = models.EmailField('E-mail', max_length=32, null=True, blank=True)
    staff_dialNumber = models.IntegerField('电话号码', null=True, blank=True)
    amount = models.IntegerField('工资', blank=True, default=0)
    bonus = models.IntegerField('奖金', blank=True, default=0)
    reimburse = models.IntegerField('报销额', blank=True, default=0)
    authority = models.ForeignKey(Authority, verbose_name='权限等级', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.staff_name
    class Meta:
        verbose_name = '员工'
        verbose_name_plural = '员工'

#联系人表
class Contactor(models.Model):
    contactor_name = models.CharField('姓名', max_length=20)
    contactor_gendar = models.CharField('性别', max_length=5, null=True)
    contactor_dialNumber = models.IntegerField('电话号码')
    contactor_email = models.EmailField('E-mail')
    def __str__(self):
        return self.contactor_name
    class Meta:
        verbose_name = '联系人'
        verbose_name_plural = '联系人'

#项目表
class Project(models.Model):
    project_name = models.CharField('项目名称', max_length=30)
    project_description = models.TextField('项目内容')
    beginTime = models.DateField('开始时间')
    endTime = models.DateField('结束时间', null = True, blank=True)
    status = models.CharField('项目状态', max_length=5, null=True, blank=True)
    contactor = models.ForeignKey(Contactor, verbose_name='联系人', on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(Staff, verbose_name='员工', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.project_name
    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'

#公司表
class Company(models.Model):
    company_name = models.CharField('公司名称', max_length=30)
    visits = models.IntegerField('拜访次数')
    lastVisitTime = models.DateField('上次拜访时间')
    intention = models.TextField('公司意向')
    score = models.IntegerField('公司评分')
    def __str__(self):
        return self.company_name
    class Meta:
        verbose_name = '单位'
        verbose_name_plural = '单位'
