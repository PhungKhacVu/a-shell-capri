# Hướng Dẫn 03: Lập Trình C/C++ & WebAssembly

Một trong những tính năng mạnh mẽ nhất của a-Shell là khả năng biên dịch mã nguồn C/C++ thành WebAssembly (WASM) và chạy trực tiếp trên thiết bị. Điều này biến iPhone thành một môi trường dev C/C++ thực thụ.

## 1. Trình Biên Dịch `clang`
a-Shell tích hợp sẵn `clang` (LLVM) hỗ trợ biên dịch ra định dạng WASM.

### Ví dụ "Hello World"
1. Tạo file `hello.c`:
   ```c
   #include <stdio.h>

   int main() {
       printf("Hello WebAssembly from a-Shell!\n");
       return 0;
   }
   ```
   Bạn có thể dùng `vim hello.c` hoặc `nano hello.c` để soạn thảo.

2. Biên dịch:
   ```bash
   $ clang hello.c -o hello.wasm
   ```
   Lệnh này sẽ tạo ra file `hello.wasm`.

3. Chạy chương trình:
   ```bash
   $ wasm hello.wasm
   # Hoặc đơn giản là:
   $ ./hello.wasm
   ```

## 2. Biên Dịch C++
Tương tự như C, bạn dùng `clang` (hoặc `clang++`) cho C++.

1. Tạo file `math.cpp`:
   ```cpp
   #include <iostream>
   #include <vector>

   int main() {
       std::vector<int> nums = {1, 2, 3, 4, 5};
       std::cout << "Numbers: ";
       for(int n : nums) std::cout << n << " ";
       std::cout << "\n";
       return 0;
   }
   ```

2. Biên dịch:
   ```bash
   $ clang++ math.cpp -o math.wasm
   ```

3. Chạy:
   ```bash
   $ ./math.wasm
   ```

## 3. Quản Lý Dự Án Với `make`
a-Shell hỗ trợ `make`, cho phép bạn build các dự án phức tạp hơn.
- Tạo `Makefile` chuẩn.
- Chạy `make`.

**Lưu ý**: Do môi trường là WASM, các cờ biên dịch (flags) mặc định thường hướng tới kiến trúc `wasm32-wasi`.

## 4. WebAssembly (WASM) Là Gì Trong a-Shell?
- Các file thực thi (`.wasm`) chạy trong một máy ảo (VM) tích hợp sẵn.
- **Hạn chế**:
  - Không hỗ trợ `fork()` hoặc `exec()` (không thể tạo tiến trình con theo cách Unix truyền thống).
  - Không hỗ trợ socket network đầy đủ (giống Python).
  - WebAssembly chỉ truy cập được các file trong thư mục hiện tại và các thư mục con (sandbox).

## 5. Mẹo Nâng Cao
- **Biên dịch thư viện tĩnh (`.a`)**: Bạn có thể dùng `ar` để đóng gói các object file `.o` thành thư viện tĩnh và link vào chương trình chính.
- **WASI-SDK**: Nếu bạn muốn biên dịch trên máy tính (Mac/Linux) rồi copy vào iPhone chạy, hãy sử dụng [WASI-sdk](https://github.com/holzschu/wasi-sdk) để đảm bảo tương thích.

Tiếp theo: [Tính năng nâng cao & Scripting](./04_Advanced_Features.md)
