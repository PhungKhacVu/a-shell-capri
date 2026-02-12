# Tích Hợp a-Shell với Apple Shortcuts

a-Shell cung cấp khả năng tích hợp mạnh mẽ với ứng dụng **Shortcuts (Phím tắt)** của Apple, cho phép bạn kết hợp sức mạnh của dòng lệnh Unix với các tính năng tự động hóa của iOS.

## Các Action Chính

a-Shell cung cấp 3 action chính trong Shortcuts:

1. **Execute Command (Thực thi lệnh)**
   - Chạy một hoặc nhiều lệnh shell.
   - **Input**: Có thể nhận text hoặc file từ action trước đó.
   - **Output**: Trả về kết quả (stdout) của lệnh dưới dạng text hoặc file.
   - **Tùy chọn**:
     - *Open Window*: Mở a-Shell để chạy lệnh (chế độ đầy đủ).
     - *Run in Extension*: Chạy ngầm (nhanh hơn, nhưng giới hạn bộ nhớ và tính năng).

2. **Put File (Lưu file)**
   - Chuyển file từ Shortcuts vào sandbox của a-Shell.
   - Rất hữu ích khi bạn download file từ Safari và muốn xử lý bằng Python/ffmpeg trong a-Shell.

3. **Get File (Lấy file)**
   - Lấy file từ a-Shell ra để sử dụng trong các bước tiếp theo của Shortcut (ví dụ: gửi mail, lưu vào Photos).

## Tại Sao Nên Dùng?
- **Tự động hóa**: Thay vì gõ lệnh thủ công mỗi ngày (ví dụ: `git pull`, `pip upgrade`), bạn có thể gói gọn vào một icon trên màn hình chính.
- **Xử lý dữ liệu**: Dùng Python để xử lý dữ liệu từ Clipboard hoặc Share Sheet mà Shortcuts mặc định không làm được.
- **Media**: Dùng `ffmpeg` để convert video ngay từ thư viện ảnh.

Xem chi tiết các ví dụ cụ thể tại [Useful_Workflows.md](./Useful_Workflows.md).
