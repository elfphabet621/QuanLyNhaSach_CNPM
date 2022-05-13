from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Trang chủ
def home(request):

    # context = {}
    return render(request, 'book/main.html')

# Trang đăng ký tài khoản
def registerPage(request):

    # if request.method == "POST":
        
    #     if form.is_valid():
    #         messages.success(request, 'Account was created for '+ username)
    #         return redirect('login')

    context = {}
    return render(request, 'book/register.html', context)

# Trang đăng nhập
def loginPage(request):
    # if request.method == "POST":
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')

    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.info(request, 'Username Or Password is incorrect')
    context = {}
    return render(request, 'book/login.html', context)

# Đăng xuất
def logoutUser(request):
    logout(request)
    return redirect('login')

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