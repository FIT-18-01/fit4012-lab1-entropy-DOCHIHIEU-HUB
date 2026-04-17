# Report 1 Page – FIT4012 Lab 1: Entropy, Redundancy & Modular Inverse

## 1. Mục tiêu
- Hiểu và triển khai hàm tính **Entropy** của một chuỗi ký tự
- Hoàn thiện hàm tính **Redundancy** (độ thừa dữ liệu) dựa trên entropy thực tế
- Cài đặt hàm tìm **Modular Inverse** sử dụng **Extended Euclidean Algorithm**
- Tổ chức, kiểm thử và nộp bài trên GitHub

## 2. Nội dung và Phương pháp

### Q1: Entropy Calculation
**Công thức:** $H(X) = -\sum_{i} p(x_i) \log_2(p(x_i))$

Đo lường độ bất định/ngẫu nhiên trong dữ liệu. Entropy cao = dữ liệu ngẫu nhiên; Entropy thấp = dữ liệu dự đoán được.

### Q2: Redundancy Calculation  
**Công thức:** $R = \log_2(N) - H(X)$, với $N$ = kích thước alphabet (256 cho ASCII)

Biểu thị phần thông tin lặp lại hoặc dự đoán được trong dữ liệu.

### Q3: Modular Inverse
**Công thức:** Tìm $x$ sao cho $a \cdot x \equiv 1 \pmod{m}$, với điều kiện $\gcd(a, m) = 1$

Sử dụng **Extended Euclidean Algorithm**: Nếu $\gcd(a,b) = ax + by$, ta có $a \cdot x \equiv 1 \pmod{b}$ khi $b = m$.

## 3. Kết quả Thực nghiệm

### Part 1: Entropy & Redundancy (5 test cases ✓)
| Input | Length | Entropy | Redundancy | Nhận xét |
|---|---:|---:|---:|---|
| `aaaa` | 4 | 0.0000 | 8.0000 | Ký tự đơn nhất, hoàn toàn dự đoán |
| `abcd` | 4 | 2.0000 | 6.0000 | 4 ký tự khác nhau, entropy cực đại |
| `hello world` | 11 | 2.8454 | 5.1546 | Văn bản tự nhiên, entropy trung bình |
| `aabbcc` | 6 | 1.5850 | 6.4150 | Cấu trúc có lặp lại |
| `aaaaabbbcc` | 10 | 1.4855 | 6.5145 | Phân bố không đều |

### Part 2: Modular Inverse (5 test cases ✓)
| a | m | GCD | Result | Verification | Status |
|---:|---:|---:|---:|---|---|
| 3 | 7 | 1 | 5 | $3 \times 5 \bmod 7 = 1$ | ✓ |
| 10 | 17 | 1 | 12 | $10 \times 12 \bmod 17 = 1$ | ✓ |
| 6 | 9 | 3 | N/A | gcd≠1 → không tồn tại | ✓ |
| 7 | 26 | 1 | 15 | $7 \times 15 \bmod 26 = 1$ | ✓ |
| 5 | 11 | 1 | 9 | $5 \times 9 \bmod 11 = 1$ | ✓ |

**Kết quả:** 10/10 tests passed (100%) ✓

## 4. Phân Tích & Kết Luận

### Entropy & Redundancy
- Entropy luôn trong khoảng $[0, \log_2(256)] = [0, 8]$
- Chuỗi có ký tự lặp lại → entropy thấp → redundancy cao
- Chuỗi có ký tự đa dạng → entropy cao → redundancy thấp
- **Ứng dụng:** Nén dữ liệu, xác định độ random, phát hiện pattern

### Modular Inverse & Extended Euclidean
- **Điều kiện tồn tại:** $\gcd(a, m) = 1$ (a và m là coprime)
- **Độ phức tạp:** $O(\log \min(a, m))$
- **Ứng dụng:** Mã hóa RSA, giải phương trình modulo, key generation

### Rút kinh nghiệm
✓ Hiểu sâu hơn lý thuyết thông tin và số học ứng dụng  
✓ Triển khai thuật toán từ lý thuyết thành code đúng đắn  
✓ Kiểm thử toàn diện → tin cậy kết quả  
✓ Extended Euclidean Algorithm là công cụ mạnh mẽ trong mã hóa
