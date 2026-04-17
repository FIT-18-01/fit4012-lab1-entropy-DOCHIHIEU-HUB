#!/usr/bin/env python3
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

def main():
    text = input("Enter a string of characters: ")
    
    entropy = calculate_entropy(text)
    redundancy = calculate_redundancy(text)
    
    print(f"Entropy: {entropy:.10f}")
    print(f"Redundancy: {redundancy:.10f}")

if __name__ == "__main__":
    main()
