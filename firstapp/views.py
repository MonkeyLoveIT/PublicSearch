from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

from .utils.database import create_record, get_record, update_record, delete_record
from .models import Book


# def index(request):
#     # 处理视图函数的逻辑
#     return render(request, 'index.html')
def index(request):
    records = Book.objects.all()  # 假设使用 Record 模型
    return render(request, 'index.html', {'records': records})


@csrf_protect
def create(request):
    if request.method == 'POST':
        data = request.POST.dict()
        record = create_record(data)
        return redirect('index')  # 重定向视图函数

    return render(request, 'index.html')


def read(request, record_id):
    record = get_object_or_404(Book, id=record_id)
    return render(request, 'read.html', {'record': record})


def update(request, record_id):
    record = get_object_or_404(Book, id=record_id)

    if request.method == 'POST':
        data = request.POST.dict()
        # 更新记录对象
        record.title = data['title']
        record.author = data['author']
        record.publication_date = data['publication_date']
        record.price = data['price']
        # 更新其他字段
        record.save()
        return redirect('index')

    return render(request, 'update.html', {'record': record})


def delete(request, record_id):
    delete_record(record_id)
    return redirect('index')


