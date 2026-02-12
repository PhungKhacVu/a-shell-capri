# a-shell: Một terminal cho iOS, hỗ trợ nhiều cửa sổ

<p align="center">
<img src="https://img.shields.io/badge/Platform-iOS%2014.0+-lightgrey.svg" alt="Platform: iOS">
<a href="https://twitter.com/a_Shell_iOS"><img src="https://img.shields.io/badge/Twitter-@a__Shell__iOS-blue.svg?style=flat" alt="Twitter"/></a>
<a href="https://discord.gg/cvYnZm69Gy"><img src="https://img.shields.io/discord/935519150305050644?color=5865f2&label=Discord&style=flat" alt="Discord"/></a>
</p>

Mục tiêu của dự án này là cung cấp một terminal giống Unix đơn giản trên iOS. Nó sử dụng [ios_system](https://github.com/holzschu/ios_system/) để thông dịch lệnh, và bao gồm tất cả các lệnh từ hệ sinh thái [ios_system](https://github.com/holzschu/ios_system/) (nslookup, whois, python3, lua, pdflatex, lualatex...)

Dự án sử dụng khả năng của iPadOS 13 để tạo và quản lý nhiều cửa sổ. Mỗi cửa sổ có ngữ cảnh, giao diện, lịch sử lệnh và thư mục hiện tại riêng. `newWindow` mở một cửa sổ mới, `exit` đóng cửa sổ hiện tại.

Để được trợ giúp, hãy gõ `help` trong dòng lệnh. `help -l` liệt kê tất cả các lệnh có sẵn. `help -l | grep command` sẽ cho bạn biết liệu lệnh yêu thích của bạn đã được cài đặt chưa.

Bạn có thể thay đổi giao diện của a-Shell bằng lệnh `config`. Nó cho phép bạn thay đổi phông chữ, kích thước phông chữ, màu nền, màu văn bản, màu con trỏ và hình dạng con trỏ. Mỗi cửa sổ có thể có giao diện riêng. `config -p` sẽ làm cho các cài đặt của cửa sổ hiện tại trở thành vĩnh viễn, nghĩa là được sử dụng cho tất cả các cửa sổ trong tương lai. Với `config -t`, bạn cũng có thể cấu hình thanh công cụ (toolbar).

Khi mở một cửa sổ mới, a-Shell thực thi tệp `.profile` nếu nó tồn tại. Bạn có thể sử dụng cơ chế này để tùy chỉnh thêm, ví dụ: có các biến môi trường tùy chỉnh hoặc dọn dẹp các tệp tạm thời.

Để biết thêm mẹo về cách sử dụng a-Shell, hãy xem <a href="https://bianshen00009.gitbook.io/a-guide-to-a-shell/">tài liệu này</a>.

## AppStore

a-Shell hiện đã <a href="https://holzschu.github.io/a-Shell_iOS/">có sẵn trên AppStore</a>.

## Cách biên dịch (compile)?

Nếu bạn muốn tự biên dịch dự án, bạn sẽ cần thực hiện các bước sau:
* tải xuống toàn bộ dự án và các mô-đun con của nó: `git submodule update --init --recursive`
* tải xuống tất cả các xcFrameworks: `downloadFrameworks.sh`
    * lệnh này sẽ tải xuống các framework tiêu chuẩn của Apple (trong `xcfs/.build/artefacts/xcfs`, có kiểm tra checksum).
    * Có quá nhiều framework Python (hơn 2000) để tải xuống tự động. Bạn có thể xóa chúng khỏi bước "Embed" trong dự án, hoặc biên dịch chúng:
        * Bạn sẽ cần các công cụ dòng lệnh Xcode (Xcode command line tools), nếu bạn chưa có: `sudo xcode-select --install`
        * Bạn cũng cần các thư viện OpenSSL (libssl và libcrypto), XQuartz (freetype), và Node.js (npm) cho macOS (chúng tôi cung cấp các phiên bản cho iOS và trình giả lập).
        * chuyển thư mục đến `cpython`: `cd cpython`
        * build Python 3.11 và tất cả các thư viện / framework liên quan: `sh ./downloadAndCompile.sh` (bước này mất vài giờ trên máy Mac i5 2GHz, thời gian có thể thay đổi tùy máy).

a-Shell hiện chạy trên các thiết bị thật. a-Shell mini có thể chạy trên các thiết bị thật và trình giả lập.

Bởi vì Python 3.x sử dụng các hàm chỉ có sẵn trên SDK iOS 14, tôi đã đặt phiên bản iOS tối thiểu là 14.0. Nó cũng làm giảm kích thước của các tệp nhị phân, vì vậy `ios_system` và các framework khác cũng có cùng cài đặt này. Nếu bạn cần chạy nó trên thiết bị iOS 13, bạn sẽ phải biên dịch lại hầu hết các framework.

## Thư mục Home

Trong iOS, bạn không thể ghi vào thư mục `~`, chỉ có thể ghi vào `~/Documents/`, `~/Library/` và `~/tmp`. Hầu hết các chương trình Unix giả định các tệp cấu hình nằm trong `$HOME`.

Vì vậy, a-Shell thay đổi một số biến môi trường để chúng trỏ đến `~/Documents`. Gõ `env` để xem chúng.

Hầu hết các tệp cấu hình (gói Python, tệp TeX, Clang SDK...) đều nằm trong `~/Library`.

## Sandbox và Bookmarks

a-Shell sử dụng khả năng của iOS 13 để truy cập các thư mục trong sandbox của Ứng dụng khác. Gõ `pickFolder` để truy cập một thư mục bên trong Ứng dụng khác. Khi bạn đã chọn một thư mục, bạn có thể làm khá nhiều thứ bạn muốn ở đây, vì vậy hãy cẩn thận.

Tất cả các thư mục bạn truy cập bằng `pickFolder` đều được đánh dấu (bookmarked), vì vậy bạn có thể quay lại chúng sau mà không cần `pickFolder`. Bạn cũng có thể đánh dấu thư mục hiện tại bằng `bookmark`. `showmarks` sẽ liệt kê tất cả các dấu trang hiện có, `jump mark` và `cd ~mark` sẽ thay đổi thư mục hiện tại thành dấu trang cụ thể này, `renamemark` sẽ cho phép bạn đổi tên một dấu trang cụ thể và `deletemark` sẽ xóa một dấu trang.

Một tùy chọn có thể định cấu hình bởi người dùng trong Cài đặt cho phép bạn sử dụng các lệnh `s`, `g`, `l`, `r` và `d` thay thế hoặc bổ sung.

Nếu bạn bị lạc, `cd` sẽ luôn đưa bạn trở lại `~/Documents/`. `cd -` sẽ chuyển sang thư mục trước đó.

## Shortcuts (Phím tắt)

a-Shell tương thích với Apple Shortcuts, cho phép người dùng kiểm soát hoàn toàn Shell. Bạn có thể viết các Shortcuts phức tạp để tải xuống, xử lý và giải phóng các tệp bằng các lệnh a-Shell. Có ba loại shortcut:
- `Execute Command` (Thực thi lệnh), nhận danh sách các lệnh và thực thi chúng theo thứ tự. Đầu vào cũng có thể là một tệp hoặc một nút văn bản, trong trường hợp đó các lệnh bên trong nút sẽ được thực thi.
- `Put File` (Đặt tệp) và `Get File` (Lấy tệp) được sử dụng để chuyển tệp đến và đi từ a-Shell.

Shortcuts có thể được thực thi "Trong Tiện ích mở rộng" (In Extension) hoặc "Trong Ứng dụng" (In App). "Trong Tiện ích mở rộng" có nghĩa là shortcut chạy trong một phiên bản nhẹ của Ứng dụng, không có giao diện người dùng đồ họa. Nó tốt cho các lệnh nhẹ không yêu cầu tệp cấu hình hoặc thư viện hệ thống (mkdir, nslookup, whois, touch, cat, echo...). "Trong Ứng dụng" mở ứng dụng chính để thực thi shortcut. Nó có quyền truy cập vào tất cả các lệnh, nhưng sẽ mất nhiều thời gian hơn. Khi một shortcut đã mở Ứng dụng, bạn có thể quay lại ứng dụng Shortcuts bằng cách gọi lệnh `open shortcuts://`. Hành vi mặc định là cố gắng chạy các lệnh "trong Tiện ích mở rộng" càng nhiều càng tốt, dựa trên nội dung của các lệnh. Bạn có thể buộc một shortcut cụ thể chạy "trong Ứng dụng" hoặc "trong Tiện ích mở rộng", với cảnh báo rằng nó không phải lúc nào cũng hoạt động.

Cả hai loại shortcut đều chạy mặc định trong cùng một thư mục cụ thể, `$SHORTCUTS` hoặc `~shortcuts`. Tất nhiên, vì bạn có thể chạy các lệnh `cd` và `jump` trong một shortcut, bạn có thể đi đến bất cứ đâu.

## Lập trình / thêm nhiều lệnh hơn:

a-Shell có một số ngôn ngữ lập trình được cài đặt sẵn: Python, Lua, JS, C, C++ và TeX.

Đối với C và C++, bạn biên dịch các chương trình của mình bằng `clang program.c` và nó tạo ra một tệp webAssembly. Sau đó, bạn có thể thực thi nó bằng `wasm a.out` hoặc `a.out`. Bạn cũng có thể liên kết nhiều tệp đối tượng (object files) lại với nhau, tạo thư viện tĩnh bằng `ar`, v.v. Khi bạn hài lòng với chương trình của mình, nếu bạn di chuyển nó đến một thư mục trong `$PATH` (ví dụ: `~/Documents/bin`), nó sẽ được thực thi nếu bạn gõ `program` trên dòng lệnh.

Bạn cũng có thể biên dịch chéo (cross-compile) các chương trình trên máy tính chính của mình bằng [WASI-sdk](https://github.com/holzschu/wasi-sdk) đặc biệt của chúng tôi và chuyển tệp WebAssembly sang iPad hoặc iPhone của bạn.

Các lệnh WebAssembly được biên dịch sẵn dành riêng cho a-Shell có sẵn tại đây: https://github.com/holzschu/a-Shell-commands Chúng bao gồm `zip`, `unzip`, `xz`, `ffmpeg`... Bạn cài đặt chúng trên iPad của mình bằng lệnh `pkg`: `pkg install zip`.

Chúng tôi có những hạn chế của WebAssembly: không có socket, không có fork (hiện tại chúng tôi đã có đầu vào người dùng tương tác). Việc truyền đầu vào từ các lệnh khác bằng `command | wasm program.wasm` hoạt động tốt.

Đối với Python, bạn có thể cài đặt thêm các gói bằng `pip install packagename`, nhưng chỉ khi chúng là thuần Python (pure Python). Trình biên dịch C chưa thể tạo ra các thư viện động có thể được sử dụng bởi Python.

Các tệp TeX không được cài đặt theo mặc định. Gõ bất kỳ lệnh TeX nào và hệ thống sẽ nhắc bạn tải xuống chúng. Tương tự với các tệp LuaTeX.

## VoiceOver

Nếu bạn bật VoiceOver trong Cài đặt, a-Shell sẽ hoạt động với VoiceOver: đọc các lệnh khi bạn gõ chúng, đọc kết quả, cho phép bạn đọc màn hình bằng ngón tay...
