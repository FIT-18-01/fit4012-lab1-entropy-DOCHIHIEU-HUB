# Report 1 Page – FIT4012 Lab 1

## 1. Mục tiêu
Tóm tắt các mục tiêu chính của bài lab:
- Hiểu và triển khai hàm tính Entropy của một chuỗi ký tự
- Hoàn thiện hàm tính Redundancy (độ thừa dữ liệu)
- Nghiên cứu và triển khai thuật toán tính Modular Inverse sử dụng Extended Euclidean Algorithm

## 2. Cách làm
- Đọc hiểu chương trình entropy mẫu.
- Bổ sung hàm tính redundancy theo công thức: redundancy = log₂(N) - H(X)
- Hoàn thiện hàm mod_inverse() sử dụng Extended Euclidean Algorithm.
- Chạy thử trên nhiều test case để xác minh kết quả.
- Ghi nhận kết quả vào báo cáo.

## 3. Kết quả chính
### 3.1 Entropy và redundancy
| Input | Entropy | Redundancy | Nhận xét |
|---|---:|---:|---|
| aaaa | ~0.00 | ~8.00 | Chuỗi đơn nhất, entropy thấp (chỉ 1 ký tự), redundancy cao |
| abcd | ~2.00 | ~6.00 | 4 ký tự khác nhau, entropy cao hơn, redundancy thấp hơn |
| hello world | ~3.74 | ~4.26 | Chuỗi thực tế, entropy và redundancy cân bằng |

### 3.2 Modulo inverse
| a | m | Kết quả mong đợi | Kết quả chương trình | Kiểm tra |
|---:|---:|---|---|---|
| 3 | 7 | 5 | 5 | 3 × 5 mod 7 = 1 ✓ |
| 10 | 17 | 12 | 12 | 10 × 12 mod 17 = 1 ✓ |
| 6 | 9 | Không tồn tại | -1 | gcd(6,9) = 3 ≠ 1 ✓ |

## 4. Kết luận
Bài lab giúp em hiểu rõ hơn về các khái niệm cơ bản trong Lý thuyết Thông tin và Số học:
- **Entropy** là thước đo độ bất định/ngẫu nhiên của dữ liệu. Dữ liệu càng đơn điệu, entropy càng thấp.
- **Redundancy** cho biết phần dữ liệu có thể dự đoán được hay không cần thiết. Dữ liệu càng lặp lại, redundancy càng cao.
- **Modular Inverse** là công cụ quan trọng trong mã hóa, chỉ tồn tại khi gcd(a, m) = 1. Extended Euclidean Algorithm là cách hiệu quả để tìm kiếm nó.
- Khó khăn lớn nhất là hiểu rõ công thức toán học và áp dụng vào code. Ôn lại toán học rời rạc và logarit đã giúp em xử lý vấn đề này.
