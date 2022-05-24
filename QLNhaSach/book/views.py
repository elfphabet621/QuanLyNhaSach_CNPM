from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *

# Trang chủ
def home(request):

    # context = {}
    return render(request, 'book/home.html')

def cart(request):
    context = {}
    return render(request, 'book/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'book/checkout.html', context)

def customer_info(request):
    form = CustomerInfo()
    context = {'form': form}
    if request.method == "POST":
        form = CustomerInfo(request.POST)

        context['form'] = form
    return render(request, 'book/customer_info.html', context)

# Trang đăng ký tài khoản
# @unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
<<<<<<< HEAD
=======
            
>>>>>>> origin/main
            messages.success(request, 'Account was created for '+ username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'book/register.html', context)

# Trang đăng nhập
# @unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username Or Password is incorrect')
    return render(request, 'book/login.html')

# Đăng xuất
def logoutUser(request):
    logout(request)
    return redirect('home')

# Tạo một cuốn sách mới
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def createBook(request, ):
    # if request.method == "POST":
        # if formset.is_valid():
        #     formset.save()
        #     return redirect('/')

    context = {}

    return render(request, 'book/book_form.html', context)

# Cập nhật một cuốn sách
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def updateBook(request):
    # if request.method == "POST":
        # if form.is_valid() :
        #     form.save()
        #     return redirect('/')

    context = {}
    return render(request, 'book/book_form.html', context)

# Xóa một cuốn sách
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def deleteBook(request):

    # if request.method == "POST":
    #     book.delete()
    #     return redirect('/')

    context = {}
    return render(request, 'book/delete_book.html', context)