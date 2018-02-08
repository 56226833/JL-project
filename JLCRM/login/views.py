from django.shortcuts import render
from login import models
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from itertools import chain
from django.http import HttpResponse

#登陆
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = models.Staff.objects.filter(username=username, password=password)
        if user:
            staff_name = models.Staff.objects.filter(username=username).first().staff_name
            return render(reqeust,'main_.html',locals())
        else:
            return HttpResponseRedirect('/login_fail/')

#注册用户
def regist(request):
    tags = ['username','password','staff_name','staff_gendar','age','education','staff_zone','qualification','staff_dialNumber','staff_email']
    if request.method == 'POST':
        param = request.POST.get('username')
        if models.Staff.objects.filter(username=param):
            return HttpResponseRedirect('/regist_result/')
        else:
            insertDB(request,tags,models.Staff)
            return HttpResponseRedirect('/regist_fail/')

#增加项目
def addProject(request):
    if request.method == "POST":
        tags = ['project_name','project_description','beginTime','endTime']
        insertDB(request,tags,models.Project)
        return render(request, 'index.html')

#增加联系人
def addContactor(request):
    if(request.method == 'POST'):
        tags=['name','gendar','dialNumber','email']
        insertDB(request,tags,models.Contactor)
        return render(request,'index.html')

#增加权限
def addAuthority(request):
    if(request.method == 'POST'):
        tags=['level','description']
        insertDB(request,tags,models.Authority)
        return render(request,'index.html')

#增加联系人
def addCompany(request):
    if(request.method == 'POST'):
        tags=['name','visits','lastVisitTime','intention','score']
        insertDB(request,tags,models.Company)
        return render(request,'index.html')


def main(request):
    staffs = models.Staff.objects.all()
    projects = models.Project.objects.all()
    companies = models.Company.objects.all()
    return render(request,'main_.html',locals())






#数据库-删
def deleteDB(key,value,model):
    selectDB(key,value,model).delete()

#数据库-查
def selectDB(key,value,model):
    obj = model.objects.filter(key=value)
    return obj;

#表单数据-增
def insertDB(request,tags,model):
    value = {}
    for tag in tags:
        increment = {tag:request.POST.get(tag)}
        value.update(increment)
    model.objects.create(**value)

#页面处理
def redirect(request,param):
    projects = models.Project.objects.all()
    staffs = models.Staff.objects.all()
    companies = models.Company.objects.all()
    contactors = models.Contactor.objects.all()
    return render(request,param+'.html',locals())
