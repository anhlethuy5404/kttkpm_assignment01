### 1. Quản lý Database

**Tạo file migration** (Ghi nhận thay đổi trong `models.py`):
```bash
python manage.py makemigrations
```

**Thực thi migration** (Áp dụng thay đổi vào MySQL):
```bash
python manage.py migrate
```

### 2. Chạy ứng dụng

**Khởi động Server:**
```bash
python manage.py runserver
```

### 3. Khởi tạo Project

**Tạo project Django mới** (Dấu `.` để không tạo thêm folder con):
```bash
python -m django startproject bookstore01 .
```
