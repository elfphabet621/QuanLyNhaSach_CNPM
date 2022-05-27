# Project quản lý nhà sách
## Giới thiệu project
### Project quản lý nhà sách bộ môn CNPM trường đại học Khoa học tự nhiên ĐHQG TPHCM
---
## Tham khảo chéo các project liên quan : 
- Project: [https://github.com/divanov11/crash-course-CRM/tree/Part-20-Password-Reset-Email]
- project: []

---
## Môi trường thực thi (phiên bản hệ điều hành, SDK, Dev Tools, cơ sở dữ liệu, etc.)
Sử dụng Django <br>
Chạy trên hầu hết mọi máy tính có thể chạy ngôn ngữ lập trình Python 3: <br>
- Windows : Từ window 8 trở đi, bản python 3.9.13(mới nhất) ko thể chạy được trên win 7 
- macOS : 64bit
- Linux / Unix 
- Solaris <br>
Cơ sở dữ liệu : sqlite3

---
## Hướng dẫn cấu hình project chạy local PC. <br>
Bước 1 : clone project django về máy <br>
VD : git clone {link project} <br>
Bước 2 : Mở visual studio code <br>
Bước 3 : download django bằng terminal <br>
pip install django <br>
Bước 4 : download và bật môi trường ảo trên terminal (Hoặc nếu có sẵn môi trường ảo khác thì vẫn được) <br>
code > pip install virtualenv <br>
code > virtual + tên môi trường ảo <br>
code > env\Scripts\activate.bat <br>
Bước 5 : open folder project bằng visual studio code <br>
Bước 6 : chạy code <br>
code > python manage.py runserver <br>
Nếu bị lỗi thì thử migrate trước <br>
code > python manage.py makemigrations <br>
code > python manage.py migrate <br>

---
## Hướng dẫn deploy project lên Heroku.
(Link hướng dẫn)[https://docs.google.com/document/d/1vBemN9QKKlEHl0a9cXVem1iwH00dEsFnypPcr1AUeFA/edit?usp=sharing]
  
---
## Link Google Drive hoặc Youtube video demo
[link]

---
## Current status: tóm tắt những gì đã hoàn thành 

| Page             | Role     |Chức năng      | Tính năng |
| ---------------- | -------- |-------------- | --------- |
| register         | guest    | đăng kí       | Kiểm tra input sai và cho guest tiếp tục nhập |
| login            | guest    | đăng nhập     | Kiểm tra input và tìm role user để redirect đến page đúng với role |
| home             | user     | Test2         | - Xem được bìa và giá những cuốn sách được hiện lên <br> - |
| user information | all role | Test2         | Toronto  |
| Hóa đơn          | user     | Test2         | Toronto  |
| Giỏ hàng         | user     | Test2         | Toronto  |
| Thanh toán       | user     | Test2         | Toronto  |
| Nhập sách        | thủ kho  | Test2         | Toronto  |

---
## Future works: tóm tắt những gì cần làm thêm
