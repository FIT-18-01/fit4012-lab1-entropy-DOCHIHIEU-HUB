#!/usr/bin/env python3

def gcd(a, b):
    """Calculate GCD of a and b"""
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclid(a, b):
    """Extended Euclidean Algorithm
    Returns (gcd, x, y) where gcd = a*x + b*y
    """
    if b == 0:
        return a, 1, 0
    
    g, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(a, m):
    """Calculate modular inverse using Extended Euclidean Algorithm
    If inverse does not exist, return -1
    """
    g, x, y = extended_euclid(a, m)
    
    # Check if modular inverse exists (gcd must be 1)
    if g != 1:
        return -1
    
    # Return positive modular inverse
    return (x % m + m) % m

def main():
    a, m = map(int, input("Nhap a, m: ").split())
    
    if gcd(a, m) != 1:
        print("Khong ton tai nghich dao modulo vi gcd(a, m) != 1.")
        return
    
    inv = mod_inverse(a, m)
    print(f"Nghich dao cua {a} mod {m} la: {inv}")
    print(f"Kiem tra: {a} * {inv} % {m} = {(a * inv) % m}")

if __name__ == "__main__":
    main()
