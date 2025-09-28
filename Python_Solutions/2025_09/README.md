# 2025.09.01 Challenge - Tribonacci Sequence

My solution -> *[2025_09_01_tribonacci_sequence](2025_09_01_tribonacci_sequence.py)*

## **_Task condition:_**

The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. When starting with `0`, `0` and `1`, the first 10 numbers in the sequence are `0`, `0`, `1`, `1`, `2`, `4`, `7`, `13`, `24`, `44`.

Given an array containing the first three numbers of a Tribonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

### **_Examples_**

```
Input: tribonacci_sequence([0, 0, 1], 20) => Output: [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513]

Input: tribonacci_sequence([21, 32, 43], 1) => Output: [21]

Input: tribonacci_sequence([0, 0, 1], 0) => Output: []

Input: tribonacci_sequence([10, 20, 30], 2) => Output: [10, 20]

Input: tribonacci_sequence([10, 20, 30], 3) => Output: [10, 20, 30]

Input: tribonacci_sequence([123, 456, 789], 8) => Output: [123, 456, 789, 1368, 2613, 4770, 8751, 16134]
```

**_NOTES:_**

- Your function should handle sequences of any length greater than or equal to zero.
- If the length is zero, return an empty array.
- Note that the starting numbers are part of the sequence.

#

<br />

