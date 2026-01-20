1. Tạo file migration (Ghi nhận thay đổi code)

python manage.py makemigrations

2. Thực thi vào Database (Tạo bảng trong MySQL)

python manage.py migrate

3. Chạy server: 

python manage.py runserver

4. Tạo project: có dấu chấm sau cùng thì không tạo folder con cùng tên

python -m django startproject bookstore01 . 

