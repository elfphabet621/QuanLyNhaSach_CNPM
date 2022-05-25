from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *


# Trang chủ
def home(request):
    sach = Sach.objects.all()
    context = {'sach': sach}
    return render(request, 'book/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        kh = request.user.person
        hd, created = HoaDon.objects.get_or_create(khach_hang = kh)
        mat_hang = hd.chitiethoadon_set.all()
    else:
        mat_hang = []
        hd = {'get_cart_total': 0, 'get_cart_item': 0}
    context = {'mat_hang': mat_hang, 'hd':hd}
    return render(request, 'book/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        kh = request.user.person
        hd, created = HoaDon.objects.get_or_create(khach_hang = kh)
        mat_hang = hd.chitiethoadon_set.all()
    else:
        mat_hang = []
        hd = {'get_cart_total': 0, 'get_cart_item': 0}
    context = {'mat_hang': mat_hang, 'hd':hd}
    return render(request, 'book/checkout.html', context)

def customer_info(request):
    customer = request.user.person
    form = CustomerInfo(instance=customer)
    
    if request.method == "POST":
        form = CustomerInfo(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            print(form.cleaned_data['profile_pic'])
            form.save()
    
    context = {'form': form}
    return render(request, 'book/customer_info.html', context)


def reviewInvoice(request):
    invoice = HoaDon.objects.all()[0]
    details = ChiTietHoaDon.objects.filter(hoa_don=invoice)
    remain = invoice.tong_tien - invoice.da_tra
    context = {'invoice': invoice, 'remain': remain, 'details': details}
    return render(request, 'book/invoice.html', context)

# Trang đăng ký tài khoản
# @unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
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