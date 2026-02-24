# Hướng Dẫn 02: Lập Trình Python trên iOS

a-Shell tích hợp sẵn Python (phiên bản 3.11), cho phép bạn chạy script, tính toán và học lập trình ngay trên điện thoại.

## 1. Chạy Python
- **Chế độ tương tác (REPL)**:
  Gõ `python` để vào môi trường tương tác. Tại đây bạn có thể gõ lệnh Python và thấy kết quả ngay.
  ```python
  $ python
  Python 3.11.0 (main, Oct 24 2022, 18:26:48) [Clang 14.0.0 (https://github.com/llvm/llvm-project ...)] on ios
  Type "help", "copyright", "credits" or "license" for more information.
  >>> print("Hello from iPhone!")
  Hello from iPhone!
  >>> exit()
  ```

- **Chạy Script**:
  Nếu bạn có file `hello.py`, chạy lệnh:
  ```bash
  $ python hello.py
  ```

## 2. Quản Lý Thư Viện (`pip`)
a-Shell hỗ trợ `pip` để cài đặt các thư viện Python.
**Lưu ý quan trọng**: Bạn chỉ có thể cài đặt các thư viện **Pure Python** (viết hoàn toàn bằng Python). Các thư viện cần biên dịch C extension (như `numpy` bản gốc, `pandas`, `opencv`) sẽ không cài được trực tiếp qua pip (tuy nhiên `numpy` đã được tích hợp sẵn trong bản a-Shell chuẩn, nhưng không có trong bản mini).

- **Cài đặt thư viện**:
  ```bash
  $ pip install requests
  ```

- **Gỡ cài đặt**:
  ```bash
  $ pip uninstall requests
  ```

- **Liệt kê thư viện đã cài**:
  ```bash
  $ pip list
  ```

## 3. Môi Trường Ảo (Virtual Environments)
Để tránh xung đột thư viện giữa các dự án, bạn nên dùng `venv`.

1. **Tạo môi trường ảo**:
   ```bash
   $ python -m venv myenv
   ```

2. **Kích hoạt môi trường**:
   ```bash
   $ source myenv/bin/activate
   ```
   Lúc này dấu nhắc lệnh sẽ đổi thành `(myenv) $`. Mọi thư viện bạn cài bằng `pip` sẽ nằm trong thư mục `myenv`.

3. **Thoát môi trường**:
   ```bash
   $ deactivate
   ```

## 4. Giới Hạn & Cách Khắc Phục
- **Không có đa luồng (Threading)**: WebAssembly và iOS hạn chế việc tạo thread mới theo cách thông thường. Một số thư viện dùng `threading` có thể gây lỗi.
- **Không hỗ trợ socket server**: Bạn không thể chạy server Django/Flask để lắng nghe kết nối từ bên ngoài (nhưng có thể chạy local để test nhẹ).
- **Giải pháp**:
  - Với các tính toán nặng, hãy dùng `numpy` (đã được tối ưu sẵn trong a-Shell bản đầy đủ).
  - Để chạy web server, hãy thử các framework nhẹ và kiểm tra kỹ log lỗi.

## 5. Ví dụ: Script lấy dữ liệu thời tiết
Tạo file `weather.py`:
```python
import requests

response = requests.get("https://wttr.in/Hanoi?format=3")
print("Thời tiết hiện tại:")
print(response.text)
```
Chạy thử:
```bash
$ pip install requests
$ python weather.py
```

Tiếp theo: [Lập trình C/C++ & WebAssembly](./03_C_Cpp_Programming.md)
