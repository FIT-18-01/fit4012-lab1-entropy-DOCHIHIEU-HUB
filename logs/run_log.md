# Run Log – FIT4012 Lab 1

## Execution Environment
- **Date**: April 17, 2026
- **Platform**: Windows 10/11
- **Language**: C++ (tested with Python harness)
- **Compiler**: Python 3.10+

## Part 1: Entropy and Redundancy

### Test 1: Single Character Repetition
```
Input: "aaaa"
Output:
  Entropy: 0.0000000000
  Redundancy: 8.0000000000
Status: ✓ PASS
Interpretation: Chuỗi hoàn toàn dự đoán được (entropy=0), dư thừa tối đa
```

### Test 2: Diverse Characters
```
Input: "abcd"
Output:
  Entropy: 2.0000000000
  Redundancy: 6.0000000000
Status: ✓ PASS
Interpretation: Ký tự đa dạng, entropy cao hơn
```

### Test 3: Natural Language (English)
```
Input: "hello world"
Output:
  Entropy: 2.8453509366
  Redundancy: 5.1546490634
Status: ✓ PASS
Interpretation: Văn bản tự nhiên có entropy cao (nhiều ký tự khác nhau)
```

### Test 4: Mixed Repetition
```
Input: "aabbcc"
Output:
  Entropy: 1.5849625007
  Redundancy: 6.4150374993
Status: ✓ PASS
Interpretation: Dữ liệu có cấu trúc, entropy trung bình
```

### Test 5: Uneven Distribution
```
Input: "aaaaabbbcc"
Output:
  Entropy: 1.4854752972
  Redundancy: 6.5145247028
Status: ✓ PASS
Interpretation: Dữ liệu không đều, entropy thấp hơn
```

## Part 2: Modular Inverse (Extended Euclidean Algorithm)

### Test 1: Simple Case
```
Input: a=3, m=7
Output:
  GCD(3, 7) = 1
  Modular Inverse: 5
  Verification: 3 * 5 % 7 = 1
Status: ✓ PASS
```

### Test 2: Larger Modulus
```
Input: a=10, m=17
Output:
  GCD(10, 17) = 1
  Modular Inverse: 12
  Verification: 10 * 12 % 17 = 1
Status: ✓ PASS
```

### Test 3: No Inverse Exists
```
Input: a=6, m=9
Output:
  GCD(6, 9) = 3
  Result: Khong ton tai nghich dao modulo vi gcd(a, m) != 1
Status: ✓ PASS
Interpretation: Vì gcd≠1, không tồn tại nghịch đảo
```

### Test 4: Coprime Numbers
```
Input: a=7, m=26
Output:
  GCD(7, 26) = 1
  Modular Inverse: 15
  Verification: 7 * 15 % 26 = 1
Status: ✓ PASS
```

### Test 5: Small Modulus
```
Input: a=5, m=11
Output:
  GCD(5, 11) = 1
  Modular Inverse: 9
  Verification: 5 * 9 % 11 = 1
Status: ✓ PASS
```

## Test Summary
```
Total Tests: 10
  - Entropy/Redundancy: 5 tests ✓
  - Modular Inverse: 5 tests ✓
Passed: 10/10 (100%)
Failed: 0/10 (0%)
```

## Performance
- Entropy calculation: O(n log m) với n=độ dài chuỗi, m=số ký tự khác nhau
- Modular inverse: O(log(min(a,m))) - Linear time complexity
- Tổng thời gian chạy tất cả tests: < 100ms

## Kết luận
✓ Tất cả test cases đều pass  
✓ Hàm entropy và redundancy tính toán chính xác  
✓ Extended Euclidean Algorithm hoạt động đúng  
✓ Kiểm tra gcd trước khi tính modular inverse bảo vệ khỏi lỗi
