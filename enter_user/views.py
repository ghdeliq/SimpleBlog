from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.contrib import auth
from django.http import HttpResponseRedirect
from .models import *
from django import forms
# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField()

def index(request):
    username = request.session.get('username', 'anybody')
    return render(request, 'enter_user/index.html',{'username': username})

def cs(request):
    return render(request, 'cs2.html')

# 注册模块
def regist(request):

  # if request.method == 'GET':
  #   return render(request, 'index.html')
 if request.method == 'POST':
    # 注册
    name = 'default'
    name = request.POST.get('username')
    newUserName = name
    oldUserName = 'oldUserNamehh'
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    print(name)
    # 判断用户名密码是否输入正确
    flag = 1
    if len(name)==0:
        return render(request,'index.html',{'name': '用户名不能为空'})
    elif len(password)<6:
        return render(request, 'index.html', {'name': '密码不能小于6位'})
    elif password != password2:
        return HttpResponse('<script>alert("两次密码输入不一致");location.href="../../" </script>')
    else:
        # 判断数据库中是否有相同的用户名
        for u in User.objects.filter(user_name=name):
            oldUserName = u.getName()
            print('newUserName', end=' ')
            print(newUserName)
        if oldUserName == newUserName:
            flag = 0
            print(flag)
            #return render(request, 'index.html', {'flag':flag ,'error': '该用户名已被占用'})
            return HttpResponse('<script>alert("该用户名已被占用");location.href="../../" </script>')
        else:
            # 将数据提交到数据库
            print(flag)
            newUser = User(
                            user_name=name,
                            user_password=password,
                            user_wzs=0
            )
            newUser.save()
            #return render(request, 'index.html', {'flag': flag, 'message': '注册成功，请登录'})
            return HttpResponse('<script>alert("注册成功，请登录");location.href="../../" </script>')

# 登录模块 全部流程
def login(request):
    # if request.method == 'GET':
    #     return render(request, 'index.html')

    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            #把获取表单的用户名传递给session对象
            request.session['start'] = 'start'


        name = request.POST.get('username')
        password = request.POST.get('password')
        print('username', end=' ')
        print(name)
        print('password', end=' ')
        print(password)
        # 查询用户是否在数据库中
        userId = 0
        for user in User.objects.filter(user_name=name,user_password=password):
            userId = user.getId()
            userStatus = user.getStatus()
            print(userId)
        if userId > 1000: # 判断用户是否存在于数据库中
            request.session['username'] = name
            request.session['user_id'] = userId
            if userStatus != '正常':
                return HttpResponse('<script>alert("账户状态异常");location.href="/"</script>')
            else :
                return render(request,'pp.html')
            #return HttpResponse('测试点')
        else:
            #用户不存在
            #flag = 0;
            #return render(request, 'enter_user/login.html', { 'name': '用户不存在'})
            #uf = UserForm()
            return  HttpResponse('<script>alert("请注册后在登陆");location.href="../../"</script>')

def logout(request):
    # 删除session
    del request.session['username']
    return HttpResponse('logout ok!')

def detail_info(request):
        for user in User.objects.filter(user_name=request.session['username']):
            userInfo = {}
            userInfo['user_id'] = user.user_id
            userInfo['user_name'] = user.user_name
            userInfo['user_password'] = user.user_password
            #userInfo['user_zps'] = user.user_zps
            userInfo['user_wzs'] = user.user_wzs
            userInfo['user_status'] = user.user_status
            print(userInfo)
        return render(request, 'pi.html', context={'userInfo':userInfo})
        #return HttpResponse('测试点')

def detail_info_jr(request):
    return HttpResponseRedirect('../')

# 修改信息函数
# def modify(request):
#     if request.method == 'GET':
#         return render(request, 'enter_user/modify.html')
#     if request.method == 'POST':
#        username=request.POST.get('username')
#        password=request.POST.get('password1')
#        newpassword=request.POST.get('password2')
#        print(username,password,newpassword)
#        s=User.objects.filter(user_name=username,user_password=password)
#        if s.count()!=0:
#            s.update(user_password=newpassword)
#            #return HttpResponse('<script>alert("修改成功");location.href="/enter_user/detail_info.html"</script>')
#            return HttpResponse('成功')
#        else:
#            #return HttpResponse('<script>alert("修改失败");location.href="/enter_user/modify.html"</script>')
#            return HttpResponse('shib')

# 个人信息修改处理
def xgxx_go(request):
    return render(request, 'xgxx.html')
class Modify1(View):
    # def get(self,request):
    #     return render(request, 'enter_user/modify.html')
    def post(self,request):
        new_username = request.POST.get('newUsername')
        password = request.POST.get('password')
        newpassword = request.POST.get('passwordb')
        # print(new_username, password, newpassword)
        s = User.objects.filter(user_password=password)
        print(s)
        if s.count() != 0:
            s.update(user_password=newpassword,user_name=new_username)
            return HttpResponse('<script>alert("修改成功，请重新登录");location.href="/"</script>')
        else:
            return HttpResponse('<script>alert("修改失败,可能是旧密码输入错误");location.href="/enter_user/xgxx/go/"</script>')





# 个人主页的展示
def pp(request):
    photos = []
    perArticleList = []
    articleList = Article.objects.filter(user_id=request.session['user_id']).order_by('article_post_time')  # 获取当前所要查询的用户的全部文章, 默认以时间顺序排序

    for art in articleList:  # 此处封装文章列表  以字典存储每一篇文章 然后放入列表中
        # 文章按时间顺序排序
        article = art.toZD()

        article['article_username'] = request.session['username']

        perArticleList.append(article)

    for art in perArticleList:  # 输出测试 成功
        print(art)
    return render(request, 'pp.html', context={'photos':photos, 'perArticleList':perArticleList})