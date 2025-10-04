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

# 2025.10.02 Challenge - Decimal To Binary

My solution -> *[2025_10_02_decimal_to_binary](2025_10_02_decimal_to_binary.py)*

## **_Task condition:_**

Given a non-negative integer, return its binary representation as a string.

A binary number uses only the digits `0` and `1` to represent any number. To convert a decimal number to binary, repeatedly divide the number by `2` and record the remainder. Repeat until the number is zero. Read the remainders last recorded to first. For example, to convert `12` to binary:

```
12 ÷ 2 = 6 remainder 0
6 ÷ 2 = 3 remainder 0
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1
```

`12` in binary is `1100`.

### **_Examples_**

```
Input: to_binary(5) => Output: "101"

Input: to_binary(12) => Output: "1100"

Input: to_binary(50) => Output: "110010"

Input: to_binary(99) => Output: "1100011"
```

#

<br />

# 2025.10.03 Challenge - P@ssw0rd Str3ngth!

My solution -> *[2025_10_03_password_strength](2025_10_03_password_strength.py)*

## **_Task condition:_**

Given a password string, return `"weak"`, `"medium"`, or `"strong"` based on the strength of the password.

A password is evaluated according to the following rules:

- It is at least `8` characters long.
- It contains both uppercase and lowercase letters.
- It contains at least one number.
- It contains at least one special character from this set: `!`, `@`, `#`, `$`, `%`, `^`, `&`, or `*`.

Return `"weak"` if the password meets fewer than two of the rules. Return `"medium"` if the password meets 2 or 3 of the rules. Return `"strong"` if the password meets all `4` rules.

### **_Examples_**

```
Input: check_strength("123456") => Output: "weak"

Input: check_strength("pass!!!") => Output: "weak"

Input: check_strength("Qwerty") => Output: "weak"

Input: check_strength("PASSWORD") => Output: "weak"

Input: check_strength("PASSWORD!") => Output: "medium"

Input: check_strength("PassWord%^!") => Output: "medium"

Input: check_strength("qwerty12345") => Output: "medium"

Input: check_strength("PASSWORD!") => Output: "medium"

Input: check_strength("PASSWORD!") => Output: "medium"

Input: check_strength("S3cur3P@ssw0rd") => Output: "strong"

Input: check_strength("C0d3&Fun!") => Output: "strong"
```

#

<br />

# 2025.10.04 Challenge - Space Week Day 1: Stellar Classification

My solution -> *[2025_10_04_space_week_day_1_stellar_classification](2025_10_04_space_week_day_1_stellar_classification.py)*

## **_Task condition:_**

October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.

For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar classification based on the following ranges:

- `"O"`: 30,000 K or higher
- `"B"`: 10,000 K - 29,999 K
- `"A"`: 7,500 K - 9,999 K
- `"F"`: 6,000 K - 7,499 K
- `"G"`: 5,200 K - 5,999 K
- `"K"`: 3,700 K - 5,199 K
- `"M"`: 0 K - 3,699 K

Return the classification of the given star.



### **_Examples_**

```
Input: classification(5778) => Output: "G"

Input: classification(2400) => Output: "M"

Input: classification(9999) => Output: "A"

Input: classification(3700) => Output: "K"

Input: classification(3699) => Output: "M"

Input: classification(210000) => Output: "O"

Input: classification(6000) => Output: "F"

Input: classification(11432) => Output: "B"
```

#

<br />