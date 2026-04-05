# 2026.04.02 Challenge - Capitalized Fibonacci

My solution -> *[2026_04_02_capitalized_fibonacci](2026_04_02_capitalized_fibonacci.py)*

## **_Task condition:_**

Given a string, return a new string where each letter is capitalized if its index is a Fibonacci number, and lowercased otherwise.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first `10` numbers in the sequence are `0`, `1`, `1`, `2`, `3`, `5`, `8`, `13`, `21`, `34`.

- The first character is at index `0`.
- If the index of non-letter characters is a Fibonacci number, leave it unchanged.

### **_Examples_**

```
Input: capitalize_fibonacci("hello world") => Output: "HELLo woRld"

Input: capitalize_fibonacci("HELLO WORLD") => Output: "HELLo woRld"

Input: capitalize_fibonacci("hello, world!") => Output: "HELLo, wOrld!"

Input: capitalize_fibonacci("The quick brown fox jumped over the lazy dog.") => Output: "THE qUicK broWn fox jUmped over thE lazy dog."

Input: capitalize_fibonacci("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar ex nibh, vel ullamcorper ligula egestas quis. Integer tincidunt fringilla accumsan. Integer et metus placerat, gravida felis at, pellentesque nisl.") => Output: "LOREm ipSum dOlor sit amet, consecTetur adipiscing elit. proin pulvinar ex nibh, vel ullaMcorper ligula egestas quis. integer tincidunt fringillA accumsan. integer et metus placerat, gravida felis at, pellentesque nisl."
```
#

<br />

# 2026.04.03 Challenge - Browser History

My solution -> *[2026_04_03_browser_history](2026_04_03_browser_history.py)*

## **_Task condition:_**

Given an array of browser commands, return an array with two values: the history as an array of URLs, and the index of the current page.

Valid commands are:

- `"URL"` - Where URL is a web address (`"freecodecamp.org"` for example). Navigates to the given URL, adds it to the history at the next position, and discards any forward history.
- `"Back"` - moves to the previous page in history, or stays on the current page if there isn't one.
- `"Forward"` - moves to the next page in history, or stays on the current page if there isn't one.

For example, given [`"freecodecamp.org", "freecodecamp.org/learn", "Back"`], return `[["freecodecamp.org", "freecodecamp.org/learn"], 0]`.

### **_Examples_**

```
Input: get_browser_history(["freecodecamp.org", "freecodecamp.org/learn", "Back"]) => Output: [["freecodecamp.org", "freecodecamp.org/learn"], 0]

Input: get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog"]) => Output: [["example.com", "example.com/about", "example.com/contact", "example.com/blog"], 3]

Input: get_browser_history(["example.com", "example.com/about", "Back", "example.com/contact", "example.com/blog", "Back", "Back", "Forward"]) => Output: [["example.com", "example.com/contact", "example.com/blog"], 1]

Input: get_browser_history(["example.com", "example.com/about", "example.com/contact", "example.com/blog", "Back", "Back", "Forward", "freecodecamp.org"]) => Output: [["example.com", "example.com/about", "example.com/contact", "freecodecamp.org"], 3]

Input: get_browser_history(["example.com", "example.com/about", "Back", "Back"]) => Output: [["example.com", "example.com/about"], 0]

Input: get_browser_history(["example.com", "example.com/about", "Forward"]) => Output: [["example.com", "example.com/about"], 1]
```
#

<br />

# 2026.04.04 Challenge - Equation Validation

My solution -> *[2026_04_04_equation_validation](2026_04_04_equation_validation.py)*

## **_Task condition:_**

Given a string representing a math equation, determine whether it is correct.

- The left side may contain up to three positive integers and the operators `+`, `-`, `*`, and `/`.
- The equation will be given in the format: `"number operator number = number"` (with two or three numbers on the left). For example: `"2 + 2 = 4"` or `"2 + 3 - 1 = 4"`.
- The right side will always be a single integer.

Follow standard order of operations: multiplication and division are evaluated before addition and subtraction, from left-to-right.

### **_Examples_**

```
Input: is_valid_equation("2 + 2 = 4") => Output: True

Input: is_valid_equation("2 + 3 - 1 = 4") => Output: True

Input: is_valid_equation("8 / 2 = 4") => Output: True

Input: is_valid_equation("10 * 5 = 50") => Output: True

Input: is_valid_equation("2 - 2 = 0") => Output: True

Input: is_valid_equation("2 + 9 / 3 = 5") => Output: True

Input: is_valid_equation("20 - 2 * 3 = 14") => Output: True

Input: is_valid_equation("2 + 5 = 6") => Output: False

Input: is_valid_equation("10 - 2 * 3 = 24") => Output: False

Input: is_valid_equation("3 + 9 / 3 = 4") => Output: False
```
#

<br />

# 2026.04.05 Challenge - Digit Rotation Escape

My solution -> *[2026_04_05_digit_rotation_escape](2026_04_05_digit_rotation_escape.py)*

## **_Task condition:_**

Given a positive integer, determine if it, or any of its rotations, is evenly divisible by its digit count.

A rotation means to move the first digit to the end. For example, after `1` rotation, `123` becomes `231`.

- Check rotation `0` (the given number) first.
- Given numbers won't contain any zeros.
- Return the first rotation number if one is found, or `"none"` if not.

### **_Examples_**

```
Input: get_rotation(123) => Output: 0

Input: get_rotation(13579) => Output: 3

Input: get_rotation(24681) => Output: "none"

Input: get_rotation(84138789345) => Output: 6
```
#

<br />