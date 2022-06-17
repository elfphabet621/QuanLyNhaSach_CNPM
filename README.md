# Project quản lý nhà sách
Project môn học thuộc bộ môn Công nghệ phần mềm trường đại học Khoa học tự nhiên ĐHQG TPHCM
## Thành viên
- Lê Kiệt – 19120554 
- Nguyễn Minh Lương – 19120571 
- Ngô Nguyễn Nhật Hạ – 19120498 
- Nguyễn Phạm Quang Dũng – 19120485 
- Nguyễn Phát Minh	– 19120586

## Bối cảnh
Với xu thế mua hàng trên Internet ngày một tăng của người dùng ở mọi độ tuổi, chúng ta cần có 1 cách nào đấy để tư vấn khách hàng về thông tin của 1 cuốn sách (nội dung, giá cả, bestselling,…). Ngoài ra, phía nhà quản lý sách cũng có thể kiểm soát và theo dõi tình hình nhà sách (số lượng sách, số lượng khách ghé thăm,…) một cách sát sao cũng như hỗ trợ khách hàng được chu đáo hơn. Nền tảng online BookManager cho phép nhóm có thể: <br>
- Quản lý đầu sách: cho phép nhập sách, điều chỉnh số lượng sách trong kho <br>
- Tra cứu sách: hỗ trợ việc tìm kiếm đầu sách theo ý khách hàng cũng như những đầu sách thuộc thể loại tương tự. Ngoài ra để hỗ trợ người dùng quyết định mua hàng, mỗi cuốn sách sẽ chứa thông tin cơ bản như nhà xuất bản, thể loại, đối tượng/lứa tuổi khách hàng phù hợp (trong trường hợp khách hàng mua cho người khác). Những thông tin này giúp cho việc cân nhắc mua sách của khách hàng tốt hơn <br>
- Quản lý tài khoản khách hàng: hỗ trợ đăng nhập, đăng xuất, quản lý thông tin cá nhân để khách hàng thuận tiện mua hàng và người quản lý nắm được danh sách khách hàng ra vào nhà sách <br>
- Tra cứu thông tin khách hàng: tra cứu theo tên khách hàng, từ đó biết được những nhu cầu cần thiết của khách hàng <br>
- Thực hiện tính toán hằng tháng, hỗ trợ xuất các biểu đồ: tính toán tổng tiền thu vào, lượng sách tồn, tính toán công nợ khách hàng <br>

## Mục tiêu project
Xây dựng một hệ thống quản lý thuận tiện cho nhà sách trên nền tảng là web, nhóm chúng em đã lên ý tưởng và thực hiện đồ án mang tên “Quản lý nhà sách”. Đồ án mong muốn mang lại một hệ thống quản lý thông minh, chính xác và hiệu quả nhất cho các doanh nghiệp bán sách. 

---
# Môi trường thực thi (phiên bản hệ điều hành, SDK, Dev Tools, cơ sở dữ liệu, etc.)
- Framework: Django <br>
- Ngôn ngữ lập trình : python3
- Hệ điều hành: hầu hết trên mọi hệ điều hành: Windows (Từ Windows 8 trở đi), Windows 7 (lưu ý: python < 3.9.13), macOS (64bit), Linux/Unix, Solaris <br>
- Cơ sở dữ liệu : sqlite3

---
# Hướng dẫn cấu hình project chạy local PC.

- Bước 1 : clone project django về máy <br>
```console
git clone {link project} 
```
<br> 

- Bước 2 : Mở bất kỳ IDE (ở đây nhóm sử dụng VSCode) và trỏ tới thư mục `source code/QLNhaSach` 
<br>

- Bước 3 : Cài đặt django bằng terminal <br>
```console
  pip install django
```
<br>

- Bước 4: Cài đặt và bật môi trường ảo trên terminal (hoặc nếu có sẵn môi trường ảo khác thì vẫn được)
  - Cài môi trường ảo: <br>
  ```console
  pip install virtualenv
  ```
  - Tạo môi trường ảo với tên tự đặt: <br>
  ```console
  virtual + {tên môi trường ảo}
  ```
  - Kích hoạt môi trường ảo: <br>
  ```console
  \Scripts\activate.bat
  ```
<br>

- Bước 5: tích hợp database và khởi động server <br> 
```console
python manage.py makemigrations 
python manage.py migrate 
python manage.py runserver
```
<br>

# Hướng dẫn deploy project lên Heroku.
- Bước 1: đăng nhập Heroku, tại giao diện chọn New $\to$ Create New App
- Bước 2: tạo app có tên qlns-group5 và nhấn **Create App**, được kết quả như hình dưới 
- Bước 4: bấm vào **qlns-group5**. ở tab **Deploy**, chọn **GitHub** và kết nối tới tài khoản github của mình. Sau khi kết nối thành công, thì thẻ **GitHub** hiển thị chữ <font color='green'>Connected</font>
- Bước 5: tạo 1 repo tên **"QLNhaSach"** trên GitHub và clone hoặc pull GitHub [này](https://github.com/LeKiet258/QLNhaSach) về repo vừa tạo.
- Bước 6: trở lại Heroku, ta tìm kiếm repo **QLNhaSach** vừa tạo ở ô tìm kiếm. Kết quả là nó tìm thấy repo này $\to$ ấn **Connect**
- Bước 7: chỉnh lại nhánh để deploy là nhánh **master** 
- Bước 8: ấn **Deploy branch**, chờ cho Heroku chạy. Sau khi chạy thành công, sẽ có nút <font color='green'>View</font> $\to$ ấn vào nút <font color='green'>View</font> để tới trang web sau khi deploy 

---
# Link Google Drive hoặc Youtube video demo
- Link Google Drive: [link](https://drive.google.com/drive/folders/1VAljnaSdJ3CFKZkjPJd3iN1vkvWRX2TR)

---
# Current status

| Page             | Role     |Chức năng                          | Tính năng                                                             |
| ---------------- | -------- |---------------------------------- | --------------------------------------------------------------------- |
| register         | guest    | đăng kí                           | - Kiểm tra input sai và cho guest tiếp tục nhập                       |
| login            | guest    | đăng nhập                         | - Kiểm tra input và tìm role user để redirect đến page đúng với role  |
| home             | user     | Giới thiệu sách                   | - Xem được bìa và giá những cuốn sách được hiện lên <br> - Thêm sách vào giỏ hàng <br> - Chọn thể loại sách <br> -  Xem được số lượng sách trong giỏ                                                                                    |
| user information | user     | Hiện thông tin khách hàng         | - Xem và chỉnh thông tin cá nhân                                      |
| Hóa đơn          | user     | Hiện các hóa đơn đã thanh toán    | - Hiện sơ bộ thông tin hóa đơn như ID, ngày lập, tổng tiền,...        |
| Chi tiết hóa đơn | user     | Hiện thông tin cụ thể hóa đơn     | - Hiện toàn bộ thông tin sách, số lượng, tiền sách, số tiền thanh toán, số tiền còn lại <br> - Thanh toán hóa đơn                                                                                                                        |
| Giỏ hàng         | user     | Hiện sản phẩm đã được cho vào giỏ | - Hiện các sách và số lượng đã chọn <br> - Chỉnh sửa số lượng sách đã chọn (tăng giảm) <br> - Bỏ sách khỏi giỏ hàng <br> - Xem tổng tiền                                                                                                   |
| Thanh toán       | user     | Chọn cách thanh toán              | - Lấy input thông tin khách hàng <br> - Chọn phương thức thanh toán   |
| Nhập sách        | thủ kho  | Nhập sách mới vào kho             | - Lấy thông tin sách mới nhập vào database                            |
| Báo cáo tồn      | thủ kho  | Xem báo cáo tháng                 | - Xem được tồn đầu, phát sinh, tồn cuối                               |
| Báo cáo nợ       | thủ kho  | Xem báo cáo tháng                 | - Xem được nợ đầu, phát sinh, nợ cuối                                 |

---
# Future work
- Sửa background các page <br>
- Cấp quyền các role đặc biệt <br>
- Lựa chọn và tìm kiếm sách bằng tên và thể loại <br>
- Xuất ra các cách thanh toán cụ thể <br>
- Thêm page riêng cho các roll đặc biệt admin, nhân viên, thủ kho <br>
- Thêm các cách thanh toán khác

---
# Tham khảo chéo các project liên quan : 
- Project: https://github.com/divanov11/crash-course-CRM/tree/Part-20-Password-Reset-Email
- Project: https://github.com/justdjango/django-ecommerce

---
# Các tham khảo khác : 
- [cs.unb.ca](http://www.cs.unb.ca/~bhavsar/courses/cs3013/cs3013/lab7.htm)
- [Fix django.forms](https://www.youtube.com/watch?v=ufI9Skz10xM)
- [Django Ecommerce Website](https://www.youtube.com/playlist?list=PL-51WBLyFTg0omnamUjL1TCVov7yDTRng)
- [Django (3.0) Crash Course Tutorials | Customer Management App](https://www.youtube.com/playlist?list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO)
- [W3Schools Online Web Tutorials](https://www.w3schools.com/)
- [Boootstrap](https://getbootstrap.com/)
