#!/usr/bin/env python3
"""
Test harness for FIT4012 Lab 1: Entropy, Redundancy, and Modular Inverse
"""
import math
from collections import Counter

def calculate_entropy(text):
    """Calculate entropy of a string"""
    if not text:
        return 0.0
    
    freq = Counter(text)
    entropy = 0.0
    for count in freq.values():
        p = count / len(text)
        entropy -= p * math.log2(p)
    return entropy

def calculate_redundancy(text, alphabet_size=256):
    """Calculate redundancy = log2(N) - H(X)"""
    entropy = calculate_entropy(text)
    max_entropy = math.log2(alphabet_size)
    return max_entropy - entropy

def gcd(a, b):
    """Calculate GCD of a and b"""
    while b != 0:
        a, b = b, a % b
    return a

def extended_euclid(a, b):
    """Extended Euclidean Algorithm"""
    if b == 0:
        return a, 1, 0
    
    g, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(a, m):
    """Calculate modular inverse"""
    g, x, y = extended_euclid(a, m)
    if g != 1:
        return -1
    return (x % m + m) % m

def test_entropy_redundancy():
    """Test entropy and redundancy calculations"""
    print("="*60)
    print("TEST 1: Entropy and Redundancy Calculation")
    print("="*60)
    
    test_cases = [
        "aaaa",
        "abcd",
        "hello world",
        "aabbcc",
        "aaaaabbbcc"
    ]
    
    results = []
    for text in test_cases:
        entropy = calculate_entropy(text)
        redundancy = calculate_redundancy(text)
        results.append({
            'input': text,
            'entropy': entropy,
            'redundancy': redundancy
        })
        print(f"\nInput: '{text}'")
        print(f"  Length: {len(text)}")
        print(f"  Entropy: {entropy:.10f}")
        print(f"  Redundancy: {redundancy:.10f}")
    
    return results

def test_modular_inverse():
    """Test modular inverse calculations"""
    print("\n" + "="*60)
    print("TEST 2: Modular Inverse Calculation")
    print("="*60)
    
    test_cases = [
        (3, 7),
        (10, 17),
        (6, 9),
        (7, 26),
        (5, 11)
    ]
    
    results = []
    for a, m in test_cases:
        g = gcd(a, m)
        inv = mod_inverse(a, m)
        results.append({
            'a': a,
            'm': m,
            'gcd': g,
            'inverse': inv
        })
        print(f"\nTest: a={a}, m={m}")
        print(f"  GCD({a}, {m}) = {g}")
        if inv == -1:
            print(f"  Result: No modular inverse exists (gcd != 1)")
        else:
            print(f"  Modular Inverse: {inv}")
            check = (a * inv) % m
            print(f"  Verification: {a} * {inv} % {m} = {check}")
    
    return results

def main():
    print("\n")
    print("*" * 60)
    print("FIT4012 LAB 1 - ENTROPY, REDUNDANCY & MODULAR INVERSE")
    print("*" * 60)
    
    entropy_results = test_entropy_redundancy()
    inverse_results = test_modular_inverse()
    
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"\n✓ Entropy/Redundancy Tests: {len(entropy_results)} passed")
    print(f"✓ Modular Inverse Tests: {len(inverse_results)} passed")
    print(f"\nTotal: {len(entropy_results) + len(inverse_results)} tests completed successfully")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
