# coding=utf-8
from django.shortcuts import render, render_to_response

from .models import *

from .forms import CommentForm
from django.http import Http404


def get_blogs(request):
    blogs = Blog.objects.all().order_by('-pub')  # 获得所有的博客按时间排序
    return render_to_response('blog_list.html', {'blogs': blogs})  # 传递context:blog参数到固定页面。


def get_details(request, blog_id):
    # 检查异常
    try:
        blog = Blog.objects.get(id=blog_id)  # 获取固定的blog_id的对象；
    except Blog.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:  # 请求方法为Post
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-pub'),
        'form': form
    }  # 返回3个参数
    return render(request, 'blog_details.html', ctx)
