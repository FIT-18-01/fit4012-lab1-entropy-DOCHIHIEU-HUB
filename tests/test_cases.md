# Test Cases – FIT4012 Lab 1: Entropy, Redundancy & Modular Inverse

## Test Execution Checklist
- [x] Test case 1: "aaaa" - entropy thấp, redundancy cao
- [x] Test case 2: "abcd" - entropy cao hơn "aaaa"
- [x] Test case 3: "hello world" - entropy và redundancy được tính hợp lệ
- [x] Test case 4: Modulo inverse a=3, m=7 → 5
- [x] Test case 5: Modulo inverse a=10, m=17 → 12

Test cases bao gồm 2 phần chính: entropy/redundancy và modular inverse.

## Part 1: Entropy and Redundancy Calculation

**Công thức:**
- Entropy: H(X) = -Σ p(x) * log₂(p(x))
- Redundancy: R = log₂(N) - H(X), với N là kích thước alphabet

| Test # | Input | Expected Result | Pass |
|--------|-------|-----------------|------|
| 1 | `"aaaa"` | Entropy=0.0, Redundancy=8.0 (dữ liệu hoàn toàn dự đoán được) | - [x] |
| 2 | `"abcd"` | Entropy=2.0, Redundancy=6.0 (dữ liệu có nhiều tính chất ngẫu nhiên) | - [x] |
| 3 | `"hello world"` | Entropy≈2.845, Redundancy≈5.155 | - [x] |
| 4 | `"aabbcc"` | Entropy≈1.585, Redundancy≈6.415 | - [x] |
| 5 | `"aaaaabbbcc"` | Entropy≈1.485, Redundancy≈6.515 | - [x] |

**Nhận xét:**
- Chuỗi có ký tự giống nhau (entropy thấp) → redundancy cao
- Chuỗi có ký tự đa dạng (entropy cao) → redundancy thấp

## Part 2: Modular Inverse (Extended Euclidean Algorithm)

**Công thức:**
- Tìm x sao cho: a*x ≡ 1 (mod m)
- Điều kiện tồn tại: gcd(a, m) = 1

| Test # | a | m | GCD | Expected Inverse | Verification | Pass |
|--------|---|---|-----|------------------|--------------|------|
| 1 | 3 | 7 | 1 | 5 | 3*5 % 7 = 1 | - [x] |
| 2 | 10 | 17 | 1 | 12 | 10*12 % 17 = 1 | - [x] |
| 3 | 6 | 9 | 3 | N/A (không tồn tại) | gcd≠1 | - [x] |
| 4 | 7 | 26 | 1 | 15 | 7*15 % 26 = 1 | - [x] |
| 5 | 5 | 11 | 1 | 9 | 5*9 % 11 = 1 | - [x] |

**Nhận xét:**
- Khi gcd(a, m) = 1, luôn tồn tại nghịch đảo modulo duy nhất
- Khi gcd(a, m) ≠ 1, không tồn tại nghịch đảo modulo

## Tổng hợp
✓ **10 test cases**: 10 đã pass  
✓ **Entropy/Redundancy**: 5 test cases  
✓ **Modular Inverse**: 5 test cases  
✓ **Thời gian chạy**: < 1 giây (tất cả tests)
