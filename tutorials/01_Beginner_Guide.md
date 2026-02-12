# Hướng Dẫn 01: Nhập Môn a-Shell (Cho Người Mới Bắt Đầu)

Nếu bạn chưa bao giờ sử dụng dòng lệnh (terminal), a-Shell là nơi tuyệt vời để bắt đầu ngay trên iPhone của bạn.

## 1. Giao Diện & Điều Khiển Cơ Bản
- **Terminal**: Là màn hình đen nơi bạn gõ lệnh và nhận kết quả.
- **Dấu nhắc lệnh (`$`)**: Nơi bạn bắt đầu gõ lệnh.
- **Bàn phím phụ**: Hàng phím trên bàn phím ảo cung cấp các phím đặc biệt như `Tab` (tự động hoàn thành), `Esc`, mũi tên di chuyển, `Ctrl`.

## 2. Các Lệnh Unix Cơ Bản
Hãy thử gõ các lệnh sau và nhấn Enter:

- `pwd`: (Print Working Directory) Cho biết bạn đang ở thư mục nào.
  ```bash
  $ pwd
  /private/var/mobile/Containers/Data/Application/.../Documents
  ```

- `ls`: (List) Liệt kê các file và thư mục con tại vị trí hiện tại.
  ```bash
  $ ls
  .profile  Library  Documents
  ```

- `cd`: (Change Directory) Di chuyển đến thư mục khác.
  - `cd Library`: Vào thư mục Library.
  - `cd ..`: Quay lại thư mục cha.
  - `cd ~`: Quay về thư mục gốc (Home).

- `clear`: Xóa sạch màn hình terminal.

## 3. Làm Việc Với File Hệ Thống iOS
iOS có cơ chế bảo mật "Sandbox", nghĩa là ứng dụng này không thể tự ý xem file của ứng dụng khác. a-Shell giải quyết việc này bằng lệnh `pickFolder`.

### Truy cập thư mục bên ngoài
1. Gõ `pickFolder`.
2. Trình quản lý file của iOS sẽ hiện ra.
3. Chọn một thư mục bất kỳ (ví dụ: một thư mục trong "Trên iPhone" hoặc "iCloud Drive").
4. a-Shell sẽ "bookmark" thư mục đó và chuyển bạn vào đó ngay lập tức.

### Quản lý Bookmarks
- `showmarks`: Xem danh sách các thư mục bạn đã cấp quyền.
- `jump [tên]`: Nhảy nhanh đến thư mục đã bookmark (ví dụ: `jump Downloads`).

## 4. Tùy Biến Giao Diện (`config`)
Bạn có thể thay đổi màu sắc và cỡ chữ cho dễ nhìn hơn.
- Gõ `config`.
- Một menu sẽ hiện ra cho phép bạn chọn:
  - **Font size**: Cỡ chữ.
  - **Font family**: Kiểu chữ (Menlo, Courier...).
  - **Color**: Màu nền và màu chữ (Dark, Light, Retro...).
  - **Cursor**: Hình dạng con trỏ (Block, Underline, Bar).

## 5. Mẹo "Sống Còn"
- **Tự động hoàn thành**: Khi gõ tên file dài, hãy gõ vài ký tự đầu rồi nhấn phím `Tab` trên thanh công cụ. a-Shell sẽ tự điền phần còn lại.
- **Lịch sử lệnh**: Nhấn mũi tên `Lên` trên thanh công cụ để gọi lại các lệnh đã gõ trước đó.
- **Thoát lệnh bị treo**: Nếu một lệnh chạy mãi không dừng, nhấn `Ctrl` + `C` (biểu tượng `^C` hoặc nút `Ctrl` rồi nhấn `C`).

Tiếp theo: [Lập trình Python trên iOS](./02_Python_Development.md)
