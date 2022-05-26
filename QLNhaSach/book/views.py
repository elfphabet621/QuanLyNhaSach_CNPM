from django.shortcuts import render, redirect
from .forms import CreateUserForm
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import Group
import math, json
from .models import *
from django.http import JsonResponse

# Trang chủ
def home(request):
    if request.user.is_authenticated:
        kh = request.user.person

        if len(HoaDon.objects.filter(khach_hang = kh)) == 0:
            newid_hd = len(HoaDon.objects.all())+1
            if int(newid_hd) <= 9:
                newid_hd = '0'+ str(newid_hd)
            newid_hd = 'HD_0'+ str(newid_hd)
            hd = HoaDon.objects.create(khach_hang = kh, id_HD=newid_hd)
        else:
            hd = HoaDon.objects.get(khach_hang = kh)
        mat_hang = hd.chitiethoadon_set.all()
        cartItems = hd.get_cart_items
    else:
        mat_hang = []
        hd = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = hd['get_cart_items']

    sach = Sach.objects.all()
    context = {'sach': sach, 'cartItems': cartItems}
    return render(request, 'book/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        kh = request.user.person
        if len(HoaDon.objects.filter(khach_hang = kh)) == 0:
            newid_hd = len(HoaDon.objects.all())+1
            if int(newid_hd) <= 9:
                newid_hd = '0'+ str(newid_hd)
            newid_hd = 'HD_0'+ str(newid_hd)
            hd = HoaDon.objects.create(khach_hang = kh, id_HD=newid_hd)
        else:
            hd = HoaDon.objects.get(khach_hang = kh)
        mat_hang = hd.chitiethoadon_set.all()
        cartItems = hd.get_cart_items
    else:
        mat_hang = []
        hd = {'get_cart_total': 0, 'get_cart_item': 0}
        cartItems = hd['get_cart_items']
    context = {'mat_hang': mat_hang, 'hd':hd, 'cartItems': cartItems}
    return render(request, 'book/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        kh = request.user.person
        if len(HoaDon.objects.filter(khach_hang = kh)) == 0:
            newid_hd = len(HoaDon.objects.all())+1
            if int(newid_hd) <= 9:
                newid_hd = '0'+ str(newid_hd)
            newid_hd = 'HD_0'+ str(newid_hd)
            hd = HoaDon.objects.create(khach_hang = kh, id_HD=newid_hd)
        else:
            hd = HoaDon.objects.get(khach_hang = kh)
        mat_hang = hd.chitiethoadon_set.all()
        cartItems = hd.get_cart_items
    else:
        mat_hang = []
        hd = {'get_cart_total': 0, 'get_cart_item': 0}
        cartItems = hd.get_cart_items
    context = {'mat_hang': mat_hang, 'hd':hd, 'cartItems': cartItems}
    return render(request, 'book/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    bookId = data['bookId']
    action = data['action']

    kh = request.user.person
    sach = Sach.objects.get(id=bookId)
    hd, created = HoaDon.objects.get_or_create(khach_hang = kh)
    mat_hang, created = ChiTietHoaDon.objects.get_or_create(hoa_don=hd, sach=sach)

    if action == 'add':
        mat_hang.so_luong = (mat_hang.so_luong + 1)
    elif action == 'remove':
        mat_hang.so_luong = (mat_hang.so_luong - 1)
    mat_hang.save()

    if mat_hang.so_luong <= 0:
        mat_hang.delete()

    return JsonResponse('Item was added', safe=False)

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

def listInvoice(request):
    user = request.user.person
    
    invoices = HoaDon.objects.filter(khach_hang__id=user.id)
    print(invoices)

    context = {'invoices': invoices}
    return render(request, 'book/list_invoice.html', context)

def reviewInvoice(request, pk):
    invoice = HoaDon.objects.get(id_HD=pk)
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
            
            group = Group.objects.get(name='customer')
            
            messages.success(request, 'Account was created for '+ username)
            return redirect('login')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")

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

def book_details(request, pk):
    book = Sach.objects.get(id=pk) # truy vấn sách có mã pk từ csdl
    
    context = {'book': book}
    return render(request, 'book/book.html', context= context)