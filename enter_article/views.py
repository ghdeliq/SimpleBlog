from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
from django.http import HttpResponseRedirect

# Create your views here.

# 测试方法
def cs(request):
    return render(request, 'cs2.html')

def shouye(request):
    return render(request, 'shouye.html')

# 文章 图片 全部乱序展示  待删除
def index(request):
    article = {}
    articleList = []
    photo = {}
    photoList = []
    qbList = []
    for art in Article.objects.all():  # 1此处封装文章列表  以字典存储每一篇文章 然后放入列表中
        # 文章封装
        article = art.toZD()
        #print(article)  # 测试用
        articleList.append(article)

    for pho in Photo.objects.all():  # 此处封装图片列表
        # 图片封装
        photo = pho.toZD()
        #print(photo)  # 测试用
        photoList.append(photo)
    qbList.extend(articleList)
    qbList.extend(photoList)
    from random import shuffle
    shuffle(qbList)
    print(qbList)
    for qb in qbList:
        print(qb)



    return render(request, 'shouye.html', context={'qbList': qbList})
    #return  HttpResponse('测试点')

# 进入该目录下后的默认显示页面  -- 展示所有文章
def show(request):
    article = {}
    articleList = []
    for art in Article.objects.order_by('-article_post_time'):  # 此处封装文章列表  以字典存储每一篇文章 然后放入列表中
        # 文章按时间顺序排序
        #article.clear()
        article = art.toZD()
        for user in User.objects.filter(user_id = art.user_id):  # 获取文章的作者名字
            article['article_username'] = user.get_name()
        articleList.append(article)

    print('遍历列表：')
    for art in articleList:   # 测试点
        print(art)
        #print(len(articleList))
    return render(request, 'passage.html', context={'articleList':articleList, 'listSize':len(articleList)})

# 个人的全部文章展示 默认时间排序
def show_person(request):
    ''' 获取传过来的user_id ，有问题'''
    # if request.method == "GET":
    #     user_id = request.Get['userId',1000] # 1000 在数据库中并不存在
    # elif request.method == "POST":
    #     user_id = request.POST.get('userId', 1000)  # 1000 在数据库中并不存在
    # else:
    #     user_id = 1000
    article = {}
    alist = []
    articleList = []
    perArticleList = []
    articleList = Article.objects.filter(user_id=1002).order_by('-article_post_time')  # 获取当前所要查询的用户的全部文章, 默认以时间顺序排序

    for art in articleList:  # 此处封装文章列表  以字典存储每一篇文章 然后放入列表中
        # 文章按时间顺序排序
        article = art.toZD()
        for user in User.objects.filter(user_id = art.user_id):  # 获取文章的作者名字
            article['article_username'] = user.get_name()

        perArticleList.append(article)

    for art in perArticleList:  # 输出测试 成功
        print (art)


    return render(request, 'enter_article/person_show.html', context={'perArticleList':perArticleList})

# 文章详情 要求展示跟帖情况   初始版本完成
'''
 
'''
def show_wzxq(request, art_id):
    # 模拟有文章id
    article_id = art_id

    article = {}
    for a in Article.objects.filter(article_id = article_id): # 获取文章信息
        article = a.toZD()
    print(article)

    # for type in ArticleType.objects.filter(article_type_id=article['article_type_id']): # 获取文章 类别名 需求变更，不需要了
    #     article_type = type.getname()
    #     print(article_type) # 输出成功
    #     article['article_type_name'] = article_type
    for aaa in User.objects.filter(user_id=article['user_id']): # 获取作者名字
        name = aaa.get_name()
        print(name)
        article['user_name'] = name
    print(article)


    # 获取跟帖列表
    # gtlist = []
    # for gt in ArticleGt.objects.filter(article_id=article['article_id']):
    #     gt_z = gt.toZD()
    #     gtlist.append(gt_z)

    # for gt in gtlist:      # 测试成功 列表封装完好
    #     print(gt)

    #return HttpResponse('测试假成功')
    return render(request, 'wzxq.html', context={'article':article})

# 发布跟帖的处理函数
# def post_gt(request):
    # request.session['user_id'] = 1002 # 模拟测试
    # user_id = request.session['user_id']


# post_article_qbj
def post_article_qbj(request):
    return render(request, 'wzfb.html') # 跳转到文章发布的页面



# 发布文章 包含所有流程
def post_article(request):
    # 测试信息
    #request.session['user_name'] = 'user2'

    # 获取用户信息
    userName = request.session.get('username', False)
    userId = request.session.get('user_id', 0)
    # for user in User.objects.filter(user_name=userName): # 获取
    #     userId = user.getId()
    #     print(userId) # 输出 成功


    # 获取编辑的文章信息
    title = request.POST.get('articleName')
    context = request.POST.get('articleContext')

    print(title)
    print(context)
    # 将数据存入数据库中
    article = Article(
                        user_id = userId,
                        article_title = title,
                        article_context = context,
                        article_post_time = datetime.datetime.now()
    )
    article.save()
    # 修改用户发表文章数
    user = User.objects.get(user_id=userId)
    user.user_wzs += 1
    user.save()
    return HttpResponseRedirect('../show/all/') # 跳转到 passage.html



