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

# 2025.10.05 Challenge - Space Week Day 2: Exoplanet Search

My solution -> *[2025_10_05_space_week_day_2_exoplanet_search](2025_10_05_space_week_day_2_exoplanet_search.py)*

## **_Task condition:_**

For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

- Luminosity readings only comprise of characters `0-9` and `A-Z` where each reading corresponds to the following numerical values:
- Characters `0-9` correspond to luminosity levels `0-9`.
- Characters `A-Z` correspond to luminosity levels `10-35`.

A star is considered to have an exoplanet if any single reading is less than or equal to `80%` of the average of all readings. For example, if the average luminosity of a star is `10`, it would be considered to have a exoplanet if any single reading is `8` or less.

### **_Examples_**

```
Input: has_exoplanet("665544554") => Output: False

Input: has_exoplanet("FGFFCFFGG") => Output: True

Input: has_exoplanet("MONOPLONOMONPLNOMPNOMP") => Output: False

Input: has_exoplanet("FREECODECAMP") => Output: True

Input: has_exoplanet("9AB98AB9BC98A") => Output: False

Input: has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE") => Output: True
```

#

<br />

# 2025.10.06 Challenge - Space Week Day 3: Phone Home

My solution -> *[2025_10_06_space_week_day_3_phone_home](2025_10_06_space_week_day_3_phone_home.py)*

## **_Task condition:_**

For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:

- The first value in the array is the distance from your location to the first satellite.
- Each subsequent value, except for the last, is the distance to the next satellite.
- The last value in the array is the distance from the previous satellite to your home planet.
- The message travels at `300,000 km/s`.
- Each satellite the message `passes through` adds a `0.5` second transmission delay.
- Return a number rounded to `4` decimal places, with trailing zeros removed.

### **_Examples_**

```
Input: send_message([300000, 300000]) => Output: 2.5

Input: send_message([384400, 384400]) => Output: 3.0627

Input: send_message([54600000, 54600000]) => Output: 364.5

Input: send_message([1000000, 500000000, 1000000]) => Output: 1674.3333

Input: send_message([10000, 21339, 50000, 31243, 10000]) => Output: 2.4086

Input: send_message([802101, 725994, 112808, 3625770, 481239]) => Output: 21.1597
```

#

<br />