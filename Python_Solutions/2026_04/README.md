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

# 2026.04.06 Challenge - What Day Is It?

My solution -> *[2026_04_06_what_day_is_it](2026_04_06_what_day_is_it.py)*

## **_Task condition:_**

Given a Unix timestamp in milliseconds, return the day of the week.

Valid return days are:

| Day of week   |
| :-----------: |
| `"Sunday"`    |
| `"Monday"`    |
| `"Tuesday"`   |
| `"Wednesday"` |
| `"Thursday"`  |
| `"Friday"`    |
| `"Saturday"`  |

Be sure to ignore time zones.

### **_Examples_**

```
Input: get_day_of_week(1775492249000) => Output: "Monday"

Input: get_day_of_week(1766246400000) => Output: "Saturday"

Input: get_day_of_week(33791256000000) => Output: "Tuesday"

Input: get_day_of_week(1773576000000) => Output: "Sunday"

Input: get_day_of_week(0) => Output: "Thursday"
```
#

<br />

# 2026.04.07 Challenge - Palindrome Characters

My solution -> *[2026_04_07_palindrome_characters](2026_04_07_palindrome_characters.py)*

## **_Task condition:_**

Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

- A palindrome is a string that is the same forward and backward.
- If it's not a palindrome, return `"none"`.

### **_Examples_**

```
Input: palindrome_locator("racecar") => Output: "e"

Input: palindrome_locator("level") => Output: "v"

Input: palindrome_locator("freecodecamp") => Output: "none"

Input: palindrome_locator("noon") => Output: "oo"

Input: palindrome_locator("11100111") => Output: "00"
```
#

<br />

# 2026.04.09 Challenge - Next Bingo Number

My solution -> *[2026_04_09_next_bingo_number](2026_04_09_next_bingo_number.py)*

## **_Task condition:_**

Given a bingo number, return the next bingo number sequentially.

A bingo number is a single letter followed by a number in its range according to this chart:

| Letter | Number Range |
| :----: | :----------: |
| "B"    | 1-15         |
| "I"    | 16-30        |
| "N"    | 31-45        |
| "G"    | 46-60        |
| "O"    | 61-75        |

For example, given `"B10"`, return `"B11"`, the next bingo number. If given the last bingo number, return `"B1"`.

### **_Examples_**

```
Input: get_next_bingo_number("B10") => Output: "B11"

Input: get_next_bingo_number("N33") => Output: "N34"

Input: get_next_bingo_number("I30") => Output: "N31"

Input: get_next_bingo_number("G60") => Output: "O61"

Input: get_next_bingo_number("O75") => Output: "B1"
```
#

<br />

# 2026.04.10 Challenge - Rook Attack

My solution -> *[2026_04_10_rook_attack](2026_04_10_rook_attack.py)*

## **_Task condition:_**

Given two strings for the location of two rooks on a chess board, determine if they can attack each other.

A standard chessboard is `8x8`, with columns labeled `A` through `H` (left to right) and rows labeled `1` through `8` (bottom to top). It looks like this:

|**A8**|**B8**|**C8**|**D8**|**E8**|**F8**|**G8**|**H8**|
|------|------|------|------|------|------|------|------|
|**A7**|**B7**|**C7**|**D7**|**E7**|**F7**|**G7**|**H7**|
|**A6**|**B6**|**C6**|**D6**|**E6**|**F6**|**G6**|**H6**|
|**A5**|**B5**|**C5**|**D5**|**E5**|**F5**|**G5**|**H5**|
|**A4**|**B4**|**C4**|**D4**|**E4**|**F4**|**G4**|**H4**|
|**A3**|**B3**|**C3**|**D3**|**E3**|**F3**|**G3**|**H3**|
|**A2**|**B2**|**C2**|**D2**|**E2**|**F2**|**G2**|**H2**|
|**A1**|**B1**|**C1**|**D1**|**E1**|**F1**|**G1**|**H1**|

Rooks can move as many squares as they want in a horizontal or vertical direction. So if they are on the same row or column, they can attack each other.

### **_Examples_**

```
Input: rook_attack("A1", "A8") => Output: True

Input: rook_attack("B4", "F4") => Output: True

Input: rook_attack("E3", "D4") => Output: False

Input: rook_attack("H7", "F6") => Output: False
```
#

<br />