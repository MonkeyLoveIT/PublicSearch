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
        return redirect('index')

    return render(request, 'index.html')


def read(request, record_id):
    record = get_object_or_404(Book, id=record_id)
    return render(request, 'read.html', {'record': record})


def update(request, record_id):
    if request.method == 'POST':
        data = request.POST.dict()
        record = update_record(record_id, data)
        return redirect('index')

    record = get_record(record_id)
    return render(request, 'index.html', {'record': record})


def delete(request, record_id):
    delete_record(record_id)
    return redirect('index')


