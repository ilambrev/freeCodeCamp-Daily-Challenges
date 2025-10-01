# 2025.10.01 Challenge - Binary To Decimal

My solution -> *[2025_10_01_binary_to_decimal](2025_10_01_binary_to_decimal.py)*

## **_Task condition:_**

Given a string representing a binary number, return its decimal equivalent as a number.

A binary number uses only the digits `0` and `1` to represent any number. To convert binary to decimal, multiply each digit by a power of `2` and add them together. Start by multiplying the rightmost digit by `2^0`, the next digit to the left by `2^1`, and so on. Once all digits have been multiplied by a power of `2`, add the result together.

For example, the binary number `101` equals `5` in decimal because:

```
1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5
```

### **_Examples_**

```
Input: to_decimal("101") => Output: 5

Input: to_decimal("1010") => Output: 10

Input: to_decimal("10010") => Output: 18

Input: to_decimal("1010101") => Output: 85
```

#

<br />
