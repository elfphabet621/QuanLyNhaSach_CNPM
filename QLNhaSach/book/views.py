from django.shortcuts import render, redirect
from .forms import CreateUserForm
from .forms import CreateBook
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *
from .utils import *
from django.http import JsonResponse
from .decorators import unauthenticated_user, allowed_users
import json
from .filters import BookFilter
from collections import defaultdict
from datetime import date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

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
    else:
        cartItems = 0
    
    
    sach = Sach.objects.order_by('ten_sach')
    myFilter = BookFilter(request.GET,  queryset=sach)
    sach = myFilter.qs

    page = request.GET.get('page', 1)
    paginator = Paginator(sach, 12)
    
    try:
        sach = paginator.page(page)
    except PageNotAnInteger:
        sach = paginator.page(1)
    except EmptyPage:
        sach = paginator.page(paginator.num_pages)
    context = {'sach': sach, 'cartItems': cartItems, 'myFilter': myFilter}

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
        if mat_hang.so_luong > mat_hang.sach.get_book_quantity:
            pass
        else:
            mat_hang.so_luong = (mat_hang.so_luong + 1)
            sach.so_luong -= 1
        

    elif action == 'remove':
        mat_hang.so_luong = (mat_hang.so_luong - 1)
        sach.so_luong += 1

    elif action == 'add-amount':
        mat_hang.so_luong = (mat_hang.so_luong + int(data['quantity']))
        sach.so_luong -= int(data['quantity'])

    mat_hang.save()
    sach.save()

    if action == 'clear':
        sach.so_luong += mat_hang.so_luong
        sach.save()
        mat_hang.delete()
    if mat_hang.so_luong <= 0:
        mat_hang.delete()

    return JsonResponse('Item was added', safe=False)

@login_required(login_url='login')
def customer_info(request):
    customer = request.user.person
    form = CustomerInfo(instance=customer)
    
    if request.method == "POST":
        form = CustomerInfo(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            if form.cleaned_data['profile_pic'] is None:
                form['profile_pic'] = "profile1.png"

            # print(form.cleaned_data['profile_pic'])

            form.save()
    
    cart_info = get_cart_info(request)
    context = {'form': form, 'cartItems':cart_info['cartItems']}
    return render(request, 'book/customer_info.html', context)

@login_required(login_url='login')
def listInvoice(request):
    user = request.user.person
    
    invoices = HoaDon.objects.filter(khach_hang__id=user.id).exclude(tong_tien=0, da_tra=-1)

    cart_info = get_cart_info(request)
    context = {'invoices': invoices, 'cartItems':cart_info['cartItems']}
    return render(request, 'book/list_invoice.html', context)

@login_required(login_url='login')
def reviewInvoice(request, pk):
    invoice = HoaDon.objects.get(id_HD=pk)
    details = ChiTietHoaDon.objects.filter(hoa_don=invoice)
    remain = invoice.tong_tien - invoice.da_tra
    cart_info = get_cart_info(request)
    context = {'invoice': invoice, 'remain': remain, 'details': details,  'cartItems':cart_info['cartItems']}
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
        # else:
        #     print("Error")
            # messages.error(request, "Unsuccessful registration. Invalid information.")

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

@login_required(login_url='login')
@allowed_users(allowed_roles=['thủ kho'])
def book_entry(request):
    tk = request.user.person
    sach = Sach.objects.all()
    ns = NhapSach(so_luong=0)
    
    form = CreateBook()
    if request.method == "POST":
        form = CreateBook(request.POST, request.FILES)
        form.nguoi_nhap = request.user.person
        if form.is_valid():
            for s in sach :
                if s.ten_sach == form.cleaned_data.get('ten_sach') :
                    if  (form.cleaned_data.get('so_luong') < 150) | (s.so_luong >= 300) :
                        messages.info(request, 'Lượng nhập tối thiểu 150 và lượng tồn phải nhỏ hơn 300')
                        return redirect('book_entry')
                    else :
                        s.ten_sach = form.cleaned_data.get('ten_sach')
                        s.ngay_nhap = form.cleaned_data.get('ngay_nhap')
                        s.the_loai = form.cleaned_data.get('the_loai') 
                        s.tac_gia = form.cleaned_data.get('tac_gia')
                        s.don_gia = form.cleaned_data.get('don_gia')
                        s.gia_ban = form.cleaned_data.get('gia_ban')
                        s.nha_xuat_ban = form.cleaned_data.get('nha_xuat_ban')
                        s.nam_xuat_ban = form.cleaned_data.get('nam_xuat_ban')
                        s.mo_ta = form.cleaned_data.get('mo_ta')
                        s.so_luong += form.cleaned_data.get('so_luong')
                        s.save()
                        
                        # cập nhật ns
                        ns.ten_sach = s.ten_sach
                        ns.ngay_nhap = s.ngay_nhap 
                        ns.so_luong = s.so_luong
                        ns.save()
                        
                        messages.info(request, 'Success')
                        return redirect('book_entry')

            if  form.cleaned_data.get('so_luong') < 150 :
                messages.info(request, 'Số lượng sách nhập phải lớn hơn 150')
                return redirect('book_entry')
            else :
                form.ten_sach = form.cleaned_data.get('ten_sach')
                form.ngay_nhap = form.cleaned_data.get('ngay_nhap')
                form.the_loai = form.cleaned_data.get('the_loai') 
                form.tac_gia = form.cleaned_data.get('tac_gia')
                form.don_gia = form.cleaned_data.get('don_gia')
                form.gia_ban = form.cleaned_data.get('gia_ban')
                form.nha_xuat_ban = form.cleaned_data.get('nha_xuat_ban')
                form.nam_xuat_ban = form.cleaned_data.get('nam_xuat_ban')
                form.mo_ta = form.cleaned_data.get('mo_ta')
                form.so_luong = form.cleaned_data.get('so_luong')
                form.save()
                
                # cập nhật ns
                ns.ten_sach = form.ten_sach
                ns.ngay_nhap = form.ngay_nhap 
                ns.so_luong = form.so_luong
                ns.save()
                        
                messages.info(request, 'Thành công')
                return redirect('book_entry')
        else:
            messages.info(request, 'Nhập sai thông tin')
            return redirect('book_entry')

    context = {'form': form, 'sach': sach}
    return render(request, 'book/book_entry.html', context)

# # Tạo một cuốn sách mới
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['thủ kho'])
# def createBook(request, ):
#     # if request.method == "POST":
#         # if formset.is_valid():
#         #     formset.save()
#         #     return redirect('/')

#     context = {}

#     return render(request, 'book/book_form.html', context)

# # Cập nhật một cuốn sách
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['thủ kho'])
# def updateBook(request):
#     # if request.method == "POST":
#         # if form.is_valid() :
#         #     form.save()
#         #     return redirect('/')

#     context = {}
#     return render(request, 'book/book_form.html', context)

# Xóa một cuốn sách
@login_required(login_url='login')
@allowed_users(allowed_roles=['thủ kho'])
def deleteBook(request):

    # if request.method == "POST":
    #     book.delete()
    #     return redirect('/')

    context = {}
    return render(request, 'book/delete_book.html', context)

@login_required(login_url='login')
def book_details(request, pk):
    if request.user.is_authenticated:
        book = Sach.objects.get(id=pk) # truy vấn sách có mã pk từ csdl
        cart_info = get_cart_info(request)
        
    context = {'book': book, 'cartItems':cart_info['cartItems']}

    return render(request, 'book/book.html', context= context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['thủ kho'])
def debt_report(request):
    current_year, current_month = 2022, 1
    hd_month = HoaDon.objects.filter(ngay_lap_HD__year=current_year, 
                                    ngay_lap_HD__month=current_month)
    
    # nợ đầu: accumulate từ tháng current_month-1 trở về trước
    debt_users = defaultdict(int)
    for i in range(1, current_month):
        hd_month_i = HoaDon.objects.filter(ngay_lap_HD__year=current_year, ngay_lap_HD__month= i)
        for hd in hd_month_i:
            if hd.tong_tien - hd.da_tra != 0:
                debt_users[hd.khach_hang] += (hd.tong_tien - hd.da_tra)
    
    # với những khách nợ, coi thử tháng current_month có phát sinh (nợ) thêm j ko
    incur_user = defaultdict(int)
    for user in debt_users.keys():
        hd_cur_month = HoaDon.objects.filter(khach_hang = user,
                                            ngay_lap_HD__year= current_year, ngay_lap_HD__month= current_month)
        # print('kiem tra: ', hd_cur_month[0].tong_tien)
        try:
            phat_sinh = hd_cur_month[0].tong_tien - hd_cur_month[0].da_tra 
            # if hd_cur_month[0].da_tra == -1: để sửa giỏ hàng, chưa test
            #     phat_sinh = 0
        except:
            phat_sinh = 0
        incur_user[user] += phat_sinh
        
    # biến các debt_users thành các instance thuộc model Debt
    list_debt = []
    is_empty = True
    if request.method == "POST":
        current_month = int(request.POST.get('month'))
        current_year = int(request.POST.get('year'))
        hd_month = HoaDon.objects.filter(ngay_lap_HD__year=current_year, 
                                        ngay_lap_HD__month=current_month,
                                        da_tra__gt=-1)
        
        # nợ đầu: accumulate từ tháng current_month-1 trở về trước
        debt_users = defaultdict(int)
        for i in range(1, current_month):
            hd_month_i = HoaDon.objects.filter(ngay_lap_HD__year=current_year, ngay_lap_HD__month= i, da_tra__gt=-1)
            
            for hd in hd_month_i:
                if hd.tong_tien - hd.da_tra != 0:
                    debt_users[hd.khach_hang] += (hd.tong_tien - hd.da_tra)
        
        # với những khách nợ, coi thử tháng current_month có phát sinh (nợ) thêm j ko
        incur_user = defaultdict(int)
        for user in debt_users.keys():
            hd_cur_month = HoaDon.objects.filter(khach_hang = user,
                                                ngay_lap_HD__year= current_year, ngay_lap_HD__month= current_month, da_tra__gt=-1)
            for hd in hd_cur_month: # 1 kh có thể có nhiều hd
                phat_sinh = hd.tong_tien - hd.da_tra 
                incur_user[user] += phat_sinh
            
        # biến các debt_users thành các instance thuộc model Debt
        list_debt = []
        for kh, no_dau in debt_users.items():
            debt_user = Debt(khach_hang = kh, no_dau = no_dau, phat_sinh = incur_user[kh])
            list_debt.append(debt_user)
            
        if list_debt: is_empty = False
    
    context = {'hd_month': hd_month, 'list_debt': list_debt, 'is_empty': is_empty,
                'months': [i for i in range(1,13)], 'current_month': current_month,
                'years': [2019, 2020, 2021, 2022], 'current_year': current_year}
    
    return render(request, 'book/debt_report.html', context= context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['thủ kho'])
def inventory_report(request):
    
    book_list = Sach.objects.all()
    is_empty = False
    inventory = []
    select_month, select_year = 6,2022
    if request.method == "POST":
        select_month = int(request.POST.get('month'))
        select_year = int(request.POST.get('year'))
        if select_month > date.today().month:
            is_empty = True
        sell_book = defaultdict(int)
        entry_book = defaultdict(int)
        for i in range(select_month,date.today().month + 1):
            # Lọc ra số sách bán từ tháng được chọn đến tháng hiện tại. 
            hd_month_i = HoaDon.objects.filter(ngay_lap_HD__year=select_year, ngay_lap_HD__month= i)
            for hd in hd_month_i:
                cthds =  ChiTietHoaDon.objects.filter(hoa_don=hd)
                for cthd in cthds:
                    sell_book[cthd.sach.ten_sach] += cthd.so_luong

            ns_month_i = NhapSach.objects.filter(ngay_nhap__year=select_year, ngay_nhap__month= i)
            for ns in ns_month_i:
                entry_book[ns.ten_sach] += ns.so_luong
        # TỒN ĐẦU: sách hiện tại - phát sinh từ tháng chọn ( với phát sinh = nhập - bán )
        #TỔNG PHÁT SINH TỪ THÁNG CHỌN ĐẾN HIỆN TẠI:

        phatsinh_n_month_book = {k: entry_book.get(k,0) - sell_book.get(k,0) for k in set(entry_book) | set(sell_book)}
        for book in book_list:
            for s, sl in phatsinh_n_month_book.items():
                if book.ten_sach == s:
                    book.so_luong -= sl


        phatsinh_month = defaultdict(int)
        for book in book_list:
            phatsinh_month[book.ten_sach] = 0
        #PHÁT SINH TRONG THÁNG ĐƯỢC CHỌN:
        sell_book_month = defaultdict(int)
        entry_book_month = defaultdict(int)
        hd_month = HoaDon.objects.filter(ngay_lap_HD__year=select_year, ngay_lap_HD__month= select_month)
        for hd in hd_month:
            cthds = ChiTietHoaDon.objects.filter(hoa_don=hd)
            for cthd in cthds:
                sell_book_month[cthd.sach.ten_sach] += cthd.so_luong

        ns_month = NhapSach.objects.filter(ngay_nhap__year=select_year, ngay_nhap__month=select_month)
        for ns in ns_month:
            entry_book_month[ns.ten_sach] += ns.so_luong

        phatsinh_month_book = {k: entry_book_month.get(k,0) - sell_book_month.get(k,0) for k in set(entry_book_month) | set(sell_book_month)}
        phatsinh_1_month = {k: phatsinh_month.get(k,0) + phatsinh_month_book.get(k,0) for k in set(phatsinh_month) | set(phatsinh_month_book)}

        
        for book in book_list:
            book_inventory = Inventory(ten_sach= book.ten_sach, ton_dau = book.so_luong, phat_sinh = phatsinh_1_month[book.ten_sach])
            inventory.append(book_inventory)
       
                
    
    context = {'inventory':inventory, 'is_empty': is_empty,
                'months': [i for i in range(1,13)], 'select_month': select_month,
                'years': [2022], 'select_year': select_year}
    return render(request, 'book/inventory_report.html', context= context)

# @login_required(login_url='login')
def create_invoice(request):
    context = {}

    data = json.loads(request.body)
    kh = request.user.person
    hd = HoaDon.objects.get(khach_hang = kh, da_tra=-1, tong_tien=0)
    hd.da_tra = data['pay']
    hd.phuong_thuc_thanh_toan = "Tiền mặt" if data['method'] == "tien-mat" else "Thẻ ngân hàng"
    hd.tong_tien = data['total']
    date = datetime.datetime.now()
    hd.ngay_lap_HD = date
    hd.save()

    return JsonResponse('HD was added', safe=False)

def success(request):
    return render (request, 'book/success.html')

@allowed_users(allowed_roles=['khách hàng'])
def pay_debt(request):
    kh = Person.objects.filter(user = request.user)
    debt_bills = HoaDon.objects.filter(khach_hang = kh[0], da_tra__gt=-1)
    
    hd_no = []
    is_debt = False
    for bill in debt_bills:
        if bill.tong_tien - bill.da_tra != 0: 
            hd_no.append(bill)
    if hd_no:
        is_debt = True 
    
    if request.method == "POST":
        bill_id = request.POST.get('which')
        which_bill = HoaDon.objects.get(id_HD=bill_id)
        which_bill.da_tra = which_bill.tong_tien
        which_bill.save()
        
        return redirect('/pay_debt')
        
    context = {'hd_no': hd_no, 'is_debt': is_debt}
    return render(request, 'book/pay_debt.html', context= context)

