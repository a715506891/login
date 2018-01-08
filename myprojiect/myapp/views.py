from django.shortcuts import render
from django.contrib.auth.decorators import login_required  # 登陆权限
from django.contrib.auth.decorators import permission_required  # 登陆访问权限

# Create your views here.


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/admin/login/')
def numone(request):
    return render(request, 'numone.html')


@login_required(login_url='/admin/login/')
@permission_required('myapp.add', login_url='/num1/')
def numtwo(request):
    return render(request, 'numtwo.html')
