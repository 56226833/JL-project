from django.shortcuts import render
from login import models
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

#登陆
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = models.Staff.objects.filter(username=username, password=password)
        if user:
            name = models.Staff.objects.filter(username=username).first().name
            return render(request, 'main.html', {"name":name})
        else:
            return HttpResponseRedirect('/error/')

#注册用户
def regist(request):
    tags = ['username','password','name','gendar','age','education','zone','qualification','dialNumber','email']
    if request.method == 'POST':
        insertDB(request,tags,models.Staff)
        if selectDB('gendar','on',models.Staff)
            request.POST.get('gendar') = '男'
        else:
            request.POST.get('gendar') = '女'
        return render(request, 'regist_result.html')
    else:
        return render(request, 'regist_fail.html')

#增加项目
def addProject(request):
    if request.method == "POST":
        tags = ['name','description','beginTime','endTime']
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


#管理界面
# def main(request):







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
    return render(request,param+'.html')

# def index(request):
#     return render(request, 'index.html')
