# Hướng Dẫn 04: Tính Năng Nâng Cao & Scripting

Khi đã thành thạo các lệnh cơ bản, bạn có thể biến a-Shell thành công cụ tự động hóa mạnh mẽ.

## 1. Shell Scripting (Bash)
a-Shell sử dụng `dash` (một phiên bản nhẹ của bash) làm shell mặc định. Bạn có thể viết các script `.sh` để tự động hóa công việc.

### Ví dụ: Script sao lưu ảnh
Tạo file `backup_photos.sh`:
```bash
#!/bin/sh

# Tạo thư mục backup nếu chưa có
mkdir -p backup

# Copy tất cả file ảnh từ thư mục hiện tại vào backup
echo "Đang sao lưu..."
cp *.jpg backup/ 2>/dev/null
cp *.png backup/ 2>/dev/null

echo "Sao lưu hoàn tất!"
ls -l backup/
```
Chạy script:
```bash
$ sh backup_photos.sh
# Hoặc cấp quyền thực thi:
$ chmod +x backup_photos.sh
$ ./backup_photos.sh
```

## 2. Xử Lý Đa Phương Tiện với `ffmpeg`
a-Shell tích hợp `ffmpeg` (chạy qua WebAssembly), cho phép xử lý video/audio mạnh mẽ.

- **Chuyển đổi định dạng video**:
  ```bash
  $ ffmpeg -i input.mov output.mp4
  ```
- **Tách âm thanh từ video**:
  ```bash
  $ ffmpeg -i video.mp4 -vn audio.mp3
  ```
- **Nén ảnh**:
  ```bash
  $ ffmpeg -i high_res.jpg -q:v 5 low_res.jpg
  ```

*Lưu ý: Tốc độ xử lý của ffmpeg trên WASM sẽ chậm hơn so với native app, nhưng rất tiện lợi cho các file nhỏ.*

## 3. Soạn Thảo Văn Bản: Vim & Nano
- **Nano**: Giao diện đơn giản, dễ dùng cho người mới.
  - `Ctrl + O`: Lưu file.
  - `Ctrl + X`: Thoát.
- **Vim**: Trình soạn thảo mạnh mẽ cho developer.
  - `i`: Vào chế độ Insert (để gõ).
  - `Esc`: Thoát chế độ Insert.
  - `:wq`: Lưu và thoát.
  - `:q!`: Thoát không lưu.
  - a-Shell hỗ trợ file `.vimrc` để cấu hình Vim.

## 4. TeX / LaTeX
a-Shell có thể biên dịch tài liệu LaTeX ngay trên iPhone.
- Lần đầu chạy lệnh `pdflatex`, ứng dụng sẽ hỏi để tải gói tài nguyên (khá lớn).
- Ví dụ:
  ```bash
  $ pdflatex report.tex
  ```
- Kết quả là file PDF có thể xem ngay bằng lệnh `view report.pdf`.

## 5. Tương Tác Với Ứng Dụng Khác (URL Schemes)
Bạn có thể mở các ứng dụng khác từ dòng lệnh:
- Mở Safari:
  ```bash
  $ open https://google.com
  ```
- Mở Shortcuts:
  ```bash
  $ open shortcuts://
  ```
- Gọi điện (yêu cầu xác nhận):
  ```bash
  $ open tel:0901234567
  ```

## 6. Lời Kết
Với khả năng scripting, biên dịch C/C++, chạy Python và xử lý media, a-Shell không chỉ là một terminal giả lập mà là một môi trường làm việc bỏ túi. Hãy kết hợp nó với ứng dụng **Shortcuts** của Apple để đạt hiệu quả tối đa (xem thư mục `shortcuts/` để biết thêm chi tiết).
