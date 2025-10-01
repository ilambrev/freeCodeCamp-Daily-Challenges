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

# 2025.09.02 Challenge - RGB to Hex

My solution -> *[2025_09_02_rgb_to_hex](2025_09_02_rgb_to_hex.py)*

## **_Task condition:_**

Given a CSS `rgb(r, g, b)` color string, return its hexadecimal equivalent.

Here are some example outputs for a given input:

| Input                   | Output      |
| :---------------------- | :---------- |
| "rgb(255, 255, 255)"  | "#ffffff" |
| "rgb(1, 2, 3)"        | "#010203" |

### **_Examples_**

```
Input: rgb_to_hex("rgb(255, 255, 255)") => Output: "#ffffff"

Input: rgb_to_hex("rgb(1, 11, 111)") => Output: "#010b6f"

Input: rgb_to_hex("rgb(173, 216, 230)") => Output: "#add8e6"

Input: rgb_to_hex("rgb(79, 123, 201)") => Output: "#4f7bc9"
```

**_NOTES:_**

- Make any letters lowercase.
- Return a `#` followed by six characters. Don't use any shorthand values.

#

<br />

# 2025.09.03 Challenge - Pangram

My solution -> *[2025_09_03_pangram](2025_09_03_pangram.py)*

## **_Task condition:_**

Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.

### **_Examples_**

```
Input: is_pangram("hello", "helo") => Output: True

Input: is_pangram("hello", "hel") => Output: False

Input: is_pangram("hello", "helow") => Output: False

Input: is_pangram("hello world", "helowrd") => Output: True

Input: is_pangram("Hello World!", "helowrd") => Output: True

Input: is_pangram("Hello World!", "heliowrd") => Output: False

Input: is_pangram("freeCodeCamp", "frcdmp") => Output: False

Input: is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz") => Output: True
```

**_NOTES:_**

- Ignore non-alphabetical characters in the word or sentence.
- Ignore letter casing in the word or sentence.

#

<br />

# 2025.09.04 Challenge - Vowel Repeater

My solution -> *[2025_09_04_vowel_repeater](2025_09_04_vowel_repeater.py)*

## **_Task condition:_**

Given a string, return a new version of the string where each vowel is duplicated one more time than the previous vowel you encountered. For instance, the first vowel in the sentence should remain unchanged. The second vowel should appear twice in a row. The third vowel should appear three times in a row, and so on.

### **_Examples_**

```
Input: repeat_vowels("hello world") => Output: "helloo wooorld"

Input: repeat_vowels("freeCodeCamp") => Output: "freeeCooodeeeeCaaaaamp"

Input: repeat_vowels("AEIOU") => Output: "AEeIiiOoooUuuuu"

Input: repeat_vowels("I like eating ice cream in Iceland") => Output: "I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee creeeeeeeeeaaaaaaaaaam iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand"
```

**_NOTES:_**

- The letters `a`, `e`, `i`, `o`, and `u`, in either uppercase or lowercase, are considered vowels.
- The original vowel should keeps its case.
- Repeated vowels should be lowercase.
- All non-vowel characters should keep their original case.

#

<br />

# 2025.09.05 Challenge - IPv4 Validator

My solution -> *[2025_09_05_ipv4_validator](2025_09_05_ipv4_validator.py)*

## **_Task condition:_**

Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists of four integer numbers separated by dots (`.`). Each number must satisfy the following conditions:

- It is between `0` and `255` inclusive.
- It does not have leading zeros (e.g. `0` is allowed, `01` is not).
- Only numeric characters are allowed.

### **_Examples_**

```
Input: is_valid_ipv4("192.168.1.1") => Output: True

Input: is_valid_ipv4("0.0.0.0") => Output: True

Input: is_valid_ipv4("255.01.50.111") => Output: False

Input: is_valid_ipv4("255.00.50.111") => Output: False

Input: is_valid_ipv4("256.101.50.115") => Output: False

Input: is_valid_ipv4("192.168.101.") => Output: False

Input: is_valid_ipv4("192168145213") => Output: False
```

#

<br />