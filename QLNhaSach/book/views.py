from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *
from .utils import get_cart_info
from django.http import JsonResponse
from .decorators import unauthenticated_user, allowed_users
import math, json

# Trang chủ
def home(request):
    if request.user.is_authenticated:
        kh = request.user.person
        chd = list(filter(lambda x: x.da_tra - x.tong_tien == -1 ,HoaDon.objects.filter(khach_hang = kh)))
        if len(chd) <= 0:
            newid_hd = len(HoaDon.objects.all())+1
            if int(newid_hd) <= 9:
                newid_hd = '0'+ str(newid_hd)
            newid_hd = 'HD_0'+ str(newid_hd)
            hd = HoaDon.objects.create(khach_hang = kh, id_HD=newid_hd, da_tra=-1, tong_tien=0)
        else:  
            hd = HoaDon.objects.get(khach_hang = kh, da_tra=-1, tong_tien=0)
        cartItems = hd.get_cart_items
        print('ID HOA DON: ',hd.id_HD, hd.da_tra, hd.tong_tien)
    else:
        cartItems = 0
    sach = Sach.objects.all()
    context = {'sach': sach, 'cartItems': cartItems}
    return render(request, 'book/home.html', context)

@login_required(login_url='login')
def cart(request):
    cart_info = get_cart_info(request)
    context = {'mat_hang': cart_info['mat_hang'], 'hd': cart_info['hd'], 'cartItems':cart_info['cartItems']}
    return render(request, 'book/cart.html', context)

@login_required(login_url='login')
def checkout(request):
    cart_info = get_cart_info(request)
    context = {'mat_hang': cart_info['mat_hang'], 'hd': cart_info['hd'], 'cartItems':cart_info['cartItems']}
    return render(request, 'book/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    bookId = data['bookId']
    action = data['action']

    kh = request.user.person
    sach = Sach.objects.get(id=bookId)
    hd = HoaDon.objects.get(khach_hang = kh, da_tra=-1, tong_tien=0)
    mat_hang, created = ChiTietHoaDon.objects.get_or_create(hoa_don=hd, sach=sach)

    if action == 'add':
        mat_hang.so_luong = (mat_hang.so_luong + 1)
    elif action == 'remove':
        mat_hang.so_luong = (mat_hang.so_luong - 1)
    elif action == 'add-amount':
        mat_hang.so_luong = (mat_hang.so_luong + int(data['quantity']))
    mat_hang.save()

    if action == 'clear' or mat_hang.so_luong <= 0:
        mat_hang.delete()

    return JsonResponse('Item was added', safe=False)

@login_required(login_url='login')
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

@login_required(login_url='login')
def listInvoice(request):
    user = request.user.person
    
    invoices = HoaDon.objects.filter(khach_hang__id=user.id)
    print(invoices)

    context = {'invoices': invoices}
    return render(request, 'book/list_invoice.html', context)

@login_required(login_url='login')
def reviewInvoice(request, pk):
    invoice = HoaDon.objects.get(id_HD=pk)
    details = ChiTietHoaDon.objects.filter(hoa_don=invoice)
    remain = invoice.tong_tien - invoice.da_tra
    context = {'invoice': invoice, 'remain': remain, 'details': details}
    return render(request, 'book/invoice.html', context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            #Create Customer have been taken care of (in signals)
            messages.success(request, 'Account was created for '+ username)
            return redirect('login')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")

    context = {'form': form}
    return render(request, 'book/register.html', context)

@unauthenticated_user
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

def logoutUser(request):
    logout(request)
    return redirect('home')

# Tạo một cuốn sách mới
@login_required(login_url='login')
@allowed_users(allowed_roles=['thủ kho'])
def createBook(request, ):
    # if request.method == "POST":
        # if formset.is_valid():
        #     formset.save()
        #     return redirect('/')

    context = {}

    return render(request, 'book/book_form.html', context)

# Cập nhật một cuốn sách
@login_required(login_url='login')
@allowed_users(allowed_roles=['thủ kho'])
def updateBook(request):
    # if request.method == "POST":
        # if form.is_valid() :
        #     form.save()
        #     return redirect('/')

    context = {}
    return render(request, 'book/book_form.html', context)

# Xóa một cuốn sách
@login_required(login_url='login')
@allowed_users(allowed_roles=['thủ kho'])
def deleteBook(request):

    # if request.method == "POST":
    #     book.delete()
    #     return redirect('/')

    context = {}
    return render(request, 'book/delete_book.html', context)

def book_details(request, pk):
    if request.user.is_authenticated:
        book = Sach.objects.get(id=pk) # truy vấn sách có mã pk từ csdl
        cart_info = get_cart_info(request)
        
    context = {'book': book, 'cartItems':cart_info['cartItems']}
    return render(request, 'book/book.html', context= context)