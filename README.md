[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sHB0KmgB)

# FIT4012 – Lab 1: Entropy, Độ dư thừa thông tin và Nghịch đảo modulo

**Sinh viên:** Đỗ Chi Hiếu  
**Lớp:** FIT-18-01  
**Ngày nộp:** April 17, 2026

## Mục tiêu bài lab

Sau khi hoàn thành bài này, sinh viên có thể:
- ✓ Đọc hiểu và chạy được chương trình tính entropy của một chuỗi ký tự
- ✓ Bổ sung chức năng tính độ dư thừa thông tin dựa trên entropy thực tế  
- ✓ Cài đặt hàm tìm nghịch đảo modulo bằng thuật toán Euclid mở rộng
- ✓ Tổ chức, kiểm thử và nộp bài bằng GitHub repo

## Cấu trúc repo

```
fit4012-lab1-entropy-DOCHIHIEU-HUB/
├── src/
│   ├── entropy_redundancy.cpp    # Q1, Q2: Entropy & Redundancy
│   ├── entropy_redundancy.py     # Python test version
│   ├── mod_inverse.cpp           # Q3: Modular Inverse
│   └── mod_inverse.py            # Python test version
├── tests/
│   ├── test_cases.md             # 10 test cases (5+5)
│   └── test_runner.py            # Test harness (chạy được)
├── logs/
│   └── run_log.md                # Log kết quả chạy thử (detailed)
├── README.md                     # Tài liệu này
├── report-page.md                # Báo cáo 1 trang (chi tiết)
└── .git/                         # Git repository
```

## Q1: Entropy Calculation

**Công thức:** $H(X) = -\sum_{i=1}^{n} p(x_i) \log_2(p(x_i))$

Entropy đo lường độ bất định trong dữ liệu:
- Entropy thấp (0) → dữ liệu hoàn toàn dự đoán được
- Entropy cao (log₂n) → dữ liệu hoàn toàn ngẫu nhiên

**Ví dụ:**
```cpp
string text = "aaaa";
double entropy = calculate_entropy(text);  // Kết quả: 0.0
```

## Q2: Redundancy Calculation

**Công thức:** $R = \log_2(N) - H(X)$, với $N$ = kích thước alphabet (256)

Redundancy biểu thị phần thông tin dự đoán được hoặc lặp lại:
- Redundancy cao → dữ liệu có nhiều phần lặp lại
- Redundancy thấp → dữ liệu random/mới lạ

**Ví dụ:**
```cpp
double redundancy = calculate_redundancy(text);  // Kết quả: 8.0
```

## Q3: Modular Inverse (Extended Euclidean Algorithm)

**Bài toán:** Tìm $x$ sao cho $a \times x \equiv 1 \pmod{m}$

**Điều kiện:** $\gcd(a, m) = 1$ (a và m phải là coprime)

**Thuật toán:** Extended Euclidean Algorithm
```
gcd(a, b) = a*x + b*y
Khi b = m: a*x + m*y = 1 → a*x ≡ 1 (mod m)
```

**Ví dụ:**
```cpp
int inverse = mod_inverse(3, 7);  // Kết quả: 5
// Verification: 3 * 5 % 7 = 1 ✓
```

## Kết quả thực nghiệm

### Test Suite: 10 tests (✓ 10/10 passed = 100%)

#### Part 1: Entropy & Redundancy (5 tests)
| Test | Input | Entropy | Redundancy | Status |
|------|-------|---------|------------|--------|
| 1 | `"aaaa"` | 0.0000 | 8.0000 | ✓ |
| 2 | `"abcd"` | 2.0000 | 6.0000 | ✓ |
| 3 | `"hello world"` | 2.8454 | 5.1546 | ✓ |
| 4 | `"aabbcc"` | 1.5850 | 6.4150 | ✓ |
| 5 | `"aaaaabbbcc"` | 1.4855 | 6.5145 | ✓ |

#### Part 2: Modular Inverse (5 tests)
| Test | a | m | Result | Verification | Status |
|------|---|---|--------|--------------|--------|
| 1 | 3 | 7 | 5 | 3×5 % 7 = 1 | ✓ |
| 2 | 10 | 17 | 12 | 10×12 % 17 = 1 | ✓ |
| 3 | 6 | 9 | N/A | gcd≠1 | ✓ |
| 4 | 7 | 26 | 15 | 7×15 % 26 = 1 | ✓ |
| 5 | 5 | 11 | 9 | 5×9 % 11 = 1 | ✓ |

### Chi tiết kết quả:
- **Entropy & Redundancy:** Tất cả kết quả phù hợp công thức toán học
- **Modular Inverse:** Extended Euclidean Algorithm hoạt động chính xác
- **Edge cases:** Xử lý đúng trường hợp gcd≠1 (không tồn tại inverse)
- **Performance:** Tất cả tests hoàn thành < 100ms

## Hướng dẫn chạy

### Chạy Test Suite (Python)
```bash
cd tests
python test_runner.py
```

### Chạy chương trình C++ (entropy_redundancy)
```bash
cd src
g++ -o entropy_redundancy entropy_redundancy.cpp
./entropy_redundancy
# Nhập chuỗi ký tự: hello
# Output: Entropy và Redundancy
```

### Chạy chương trình C++ (mod_inverse)
```bash
cd src
g++ -o mod_inverse mod_inverse.cpp
./mod_inverse
# Nhập: 3 7
# Output: Modular inverse của 3 mod 7 = 5
```

## Tệp quan trọng

- **[src/entropy_redundancy.cpp](src/entropy_redundancy.cpp)** - Đầy đủ Q1, Q2
- **[src/mod_inverse.cpp](src/mod_inverse.cpp)** - Đầy đủ Q3 (Extended Euclidean)
- **[tests/test_cases.md](tests/test_cases.md)** - 10 test cases chi tiết
- **[logs/run_log.md](logs/run_log.md)** - Output của tất cả tests
- **[report-page.md](report-page.md)** - Báo cáo 1 trang (phân tích, công thức)

## Git Commits

```
✓ Complete Q1 entropy walkthrough
✓ Implement redundancy calculation  
✓ Implement modular inverse with extended Euclid
✓ Add tests and report
```

## Kết luận

### Những gì đã học được:
1. **Entropy** - đo lường độ bất định/ngẫu nhiên trong dữ liệu
2. **Redundancy** - biểu thị phần thông tin lặp lại/dự đoán được
3. **Extended Euclidean Algorithm** - công cụ mạnh mẽ để tìm modular inverse
4. **Ứng dụng thực tế:**
   - Entropy: nén dữ liệu, mã hóa, phân tích tín hiệu
   - Modular Inverse: RSA encryption, key generation, cryptography

### Khó khăn và cách giải quyết:
- Hiểu công thức logarit → ôn lại toán rời rạc
- Debug Extended Euclidean → trace through step by step
- Xác minh kết quả → tạo test cases đa dạng

---

**Status:** ✓ Hoàn thành 100%  
**Test Results:** ✓ 10/10 passed (100%)  
**Ready for submission:** ✓ YES
