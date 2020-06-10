from django.shortcuts import render
from django.views.generic.base import View
import datetime
from django.http import HttpResponse
from .models import *


# Create your views here.
# def show(request):
#     photos = Photos.objects.all()
#     return render(request, 'index.html', {'photos': photots})

def index(request):
    pass

# 展示全部照片 完成
def photo_show(request):
    ''' 由于需求变动，此功能可以删除 '''
    # # 测试信息
    # request.session['user_name'] = 'user2'
    #
    # # 获取用户信息
    #
    # userName = request.session.get('user_name', False)
    # for user in User.objects.filter(user_name=userName):  # 获取文章 类别名
    #     userId = user.getId()
    #     print(userId)  # 输出 成功
    photos = []
    for ph in Photo.objects.all().order_by('-photo_id'): # 封装照片列表
        # print(ph.photo_p) 测试成功
        photo = ph.toZD()

        # for type in PhotoType.objects.filter(photo_type_id = ph.get_type_id()):  # 获取分类名
        #     photo_type=type.get_name()
        #     photo['photo_type_name'] = photo_type
        photos.append(photo)

    # for type in PhotoType.objects.filter(user_id=userId): # 获取分类名列表
    #     photo_type = type.toZD()
    #     photo_type_list.append(photo_type)


    for p in photos:  # 测试
        print(p)

    #return  HttpResponse('测试点')
    return render(request, 'zpq.html', context={'photos':photos})


def cs(request):
    return render(request, 'enter_photo/show_detail.html')

#上传模块
# def uploadImg(request): # 图片上传函数
#     if request.method == 'POST':
#         img = Img(img_url=request.FILES.get('img'))
#         img.save()
#     return render(request, 'imgupload.html')


# 展示照片详情
def show_detail(request,ph_id):
    photoId = ph_id

    for ph in Photo.objects.filter(photo_id=photoId): # 封装照片列表
        # print(ph.photo_p) 测试成功
        photo = ph.toZD()

    return render(request, 'zpxq.html', context={'photo':photo})





