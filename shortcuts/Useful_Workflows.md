# Các Quy Trình Làm Việc Hữu Ích (Workflows) Với a-Shell

Dưới đây là một số ý tưởng và hướng dẫn tạo Shortcuts kết hợp với a-Shell để giải quyết các vấn đề thực tế.

## 1. Tải Video Youtube & Chuyển Đổi Sang MP3
**Mục tiêu**: Tải video (dùng `yt-dlp` cài qua pip) và tách lấy âm thanh.

**Các bước trong Shortcuts**:
1. **Nhận đầu vào**: Từ Share Sheet (URL Youtube).
2. **a-Shell: Execute Command**:
   ```bash
   # Cài yt-dlp nếu chưa có
   # pip install yt-dlp
   cd ~/Documents/Downloads
   yt-dlp -x --audio-format mp3 "$shortcutInput"
   ```
   *Lưu ý: `$shortcutInput` là biến Shortcut truyền vào.*
3. **a-Shell: Get File**: Lấy file mp3 mới nhất từ thư mục Downloads.
4. **Save File**: Lưu vào iCloud Drive hoặc Share ra ứng dụng khác.

## 2. Git Sync Nhanh
**Mục tiêu**: Đồng bộ hóa một thư mục Obsidian hoặc Notes (đang để trong a-Shell) lên GitHub chỉ bằng 1 cú chạm.

**Các bước trong Shortcuts**:
1. **a-Shell: Execute Command**:
   ```bash
   cd ~/Documents/MyNotes
   git add .
   git commit -m "Auto sync from iPhone $(date)"
   git pull --rebase
   git push
   ```
2. **Show Notification**: Hiển thị thông báo "Sync Complete" khi lệnh chạy xong.

## 3. Nén Ảnh Hàng Loạt
**Mục tiêu**: Chọn nhiều ảnh từ Photos, nén giảm dung lượng và gom vào file ZIP.

**Các bước trong Shortcuts**:
1. **Select Photos**: Chọn ảnh (Multiple).
2. **a-Shell: Put File**: Lưu các ảnh này vào thư mục `~/tmp/compress_input`.
3. **a-Shell: Execute Command**:
   ```bash
   cd ~/tmp/compress_input
   mkdir -p ../compress_output
   # Dùng ffmpeg nén từng ảnh
   for f in *.jpg; do
       ffmpeg -i "$f" -q:v 10 "../compress_output/$f"
   done
   cd ../compress_output
   zip -r compressed_photos.zip .
   ```
4. **a-Shell: Get File**: Lấy file `compressed_photos.zip`.
5. **Share**: Gửi file zip qua AirDrop hoặc Mail.

## 4. Chạy Python Script Xử Lý Text
**Mục tiêu**: Xử lý văn bản đang chọn (ví dụ: format JSON, dịch, tóm tắt) bằng script Python tự viết.

**Các bước trong Shortcuts**:
1. **Nhận đầu vào**: Text (từ Share Sheet hoặc Clipboard).
2. **a-Shell: Execute Command**:
   - Chọn "Input" là Text.
   ```bash
   # Script python đọc từ stdin và in ra stdout
   python process_text.py
   ```
3. **Copy to Clipboard**: Copy kết quả đầu ra của a-Shell.

---
**Mẹo**: Để các Shortcut chạy mượt mà, hãy cố gắng sử dụng tùy chọn "Run in Extension" nếu lệnh không tốn quá nhiều RAM. Nếu lệnh nặng (như `ffmpeg` hay `yt-dlp`), hãy để nó mở ứng dụng a-Shell ("Open Window") để tránh bị iOS đóng băng tiến trình.
