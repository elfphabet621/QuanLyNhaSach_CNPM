# Project quản lý nhà sách
Project môn học thuộc bộ môn Công nghệ phần mềm trường đại học Khoa học tự nhiên ĐHQG TPHCM
#### Thành viên
- Lê Kiệt – 19120554 
- Nguyễn Minh Lương – 19120571 
- Ngô Nguyễn Nhật Hạ – 19120498 
- Nguyễn Phạm Quang Dũng – 19120485 
- Nguyễn Phát Minh	– 19120586

#### Context
Với xu thế mua hàng trên Internet ngày một tăng của người dùng ở mọi độ tuổi, chúng ta cần có 1 cách nào đấy để tư vấn khách hàng về thông tin của 1 cuốn sách (nội dung, giá cả, bestselling,…). Ngoài ra, phía nhà quản lý sách cũng có thể kiểm soát và theo dõi tình hình nhà sách (số lượng sách, số lượng khách ghé thăm,…) một cách sát sao cũng như hỗ trợ khách hàng được chu đáo hơn. Nền tảng online BookManager cho phép chủ nhà sách có thể:

#### Mục tiêu project
Xây dựng một hệ thống quản lý thuận tiện cho nhà sách trên nền tảng là web, nhóm chúng em đã lên ý tưởng và thực hiện đồ án mang tên “Quản lý nhà sách”. Đồ án mong muốn mang lại một hệ thống quản lý thông minh, chính xác và hiệu quả nhất cho các doanh nghiệp bán sách. 

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
<Điền vào đây>

---
## Link Google Drive hoặc Youtube video demo
[link]

---
## Current status: tóm tắt những gì đã hoàn thành 

| Page             | Role     |Chức năng      | Tính năng |
| ---------------- | -------- |-------------- | --------- |
| register         | guest    | đăng kí                 | - Kiểm tra input sai và cho guest tiếp tục nhập |
| login            | guest    | đăng nhập               | - Kiểm tra input và tìm role user để redirect đến page đúng với role |
| home             | user     | Giới thiệu sách | - Xem được bìa và giá những cuốn sách được hiện lên <br> - Thêm sách vào giỏ hàng <br> - Chọn thể loại sách <br> -  Xem được số lượng sách trong giỏ |
| user information | user     | Hiện thông tin khách hàng         | - Xem và chỉnh thông tin cá nhân |
| Hóa đơn          | user     | Hiện các hóa đơn đã thanh toán         | - Hiện sơ bộ thông tin hóa đơn như ID, ngày lập, tổng tiền,...  |
| Giỏ hàng         | user     | Hiện sản phẩm đã được cho vào giỏ         | - Hiện các sách và số lượng đã chọn <br> - Chỉnh sửa số lượng sách đã chọn (tăng giảm) <br> - Bỏ sách khỏi giỏ hàng <br> - Xem tổng tiền |
| Thanh toán       | user     | Chọn cách thanh toán         | - Lấy input thông tin khách hàng <br> - Chọn phương thức thanh toán |
| Nhập sách        | thủ kho  | Nhập sách mới vào kho         | - Lấy thông tin sách mới nhập vào database  |

---
## Future works: tóm tắt những gì cần làm thêm
- Sửa background các page <br>
- Cấp quyến các role đặc biệt <br>
- Lựa chọn và tìm kiếm sách bằng tên và thể loại <br>
- Xuất ra các cách thanh toán cụ thể <br>
- Thêm page chi tiết hóa đơn <br>
- Thêm page riêng cho các roll đặc biệt admin, nhân viên, thủ kho <br>
- Thêm page báo cáo tồn <br>
- Thêm page báo cáo nợ <br>
