# 2025.08.11 Challenge - Vowel Balance

My solution -> *[2025_08_11_vowel_balance](2025_08_11_vowel_balance.py)*

## **_Task condition:_**

Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

### **_Examples_**

```
Input: is_balanced("racecar") => Output: True

Input: is_balanced("Lorem Ipsum") => Output: True

Input: is_balanced("Kitty Ipsum") => Output: False

Input: is_balanced("string") => Output: False

Input: is_balanced(" ") => Output: True

Input: is_balanced("abcdefghijklmnopqrstuvwxyz") => Output: False

Input: is_balanced("123A#b!E&*456-o.U") => Output: True
```

**_NOTES:_**

- The string can contain any characters.
- The letters `a`, `e`, `i`, `o`, and `u`, in either uppercase or lowercase, are considered vowels.
- If there's an odd number of characters in the string, ignore the center character.

#

<br />

# 2025.08.12 Challenge - Base Check

My solution -> *[2025_08_12_base_check](2025_08_12_base_check.py)*

## **_Task condition:_**

Given a string representing a number, and an integer base from `2` to `36`, determine whether the number is valid in that base.

### **_Examples_**

```
Input: is_valid_number("10101", 2) => Output: True

Input: is_valid_number("10201", 2) => Output: False

Input: is_valid_number("76543210", 8) => Output: True

Input: is_valid_number("9876543210", 8) => Output: False

Input: is_valid_number("9876543210", 10) => Output: True

Input: is_valid_number("ABC", 10) => Output: False

Input: is_valid_number("ABC", 16) => Output: True

Input: is_valid_number("Z", 36) => Output: True

Input: is_valid_number("ABC", 20) => Output: True

Input: is_valid_number("4B4BA9", 16) => Output: True

Input: is_valid_number("5G3F8F", 16) => Output: False

Input: is_valid_number("5G3F8F", 17) => Output: True

Input: is_valid_number("abc", 10) => Output: False

Input: is_valid_number("abc", 16) => Output: True

Input: is_valid_number("AbC", 16) => Output: True

Input: is_valid_number("z", 36) => Output: True
```

**_NOTES:_**

- The string may contain integers, and uppercase or lowercase characters.
- The check should be case-insensitive.
- The base can be any number `2-36`.
- A number is valid if every character is a valid digit in the given base.
- Example of valid digits for bases:
    - **Base 2**: `0-1`
    - **Base 8**: `0-7`
    - **Base 10**: `0-9`
    - **Base 16**: `0-9 and A-F`
    - **Base 36**: `0-9 and A-Z`

#

<br />
