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

# 2026.04.11 Challenge - Rook and Bishop Attack

My solution -> *[2026_04_11_rook_and_bishop_attack](2026_04_11_rook_and_bishop_attack.py)*

## **_Task condition:_**

Given a string for the location of a rook on a chess board, and another for the location of a bishop, determine if one piece can attack another.

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

- Rooks can move as many squares as they want in a horizontal or vertical direction.
- Bishops can move as many squares as they want in any diagonal direction.
- One piece can attack another if it can move to the location of that piece.

Return:

- `"rook"` if the rook can attack the bishop.
- `"bishop"` if the bishop can attack the rook.
- `"neither"` if neither piece can attack one another.

### **_Examples_**

```
Input: rook_bishop_attack("A1", "A5") => Output: "rook"

Input: rook_bishop_attack("C3", "F6") => Output: "bishop"

Input: rook_bishop_attack("D4", "D7") => Output: "rook"

Input: rook_bishop_attack("B7", "H1") => Output: "bishop"

Input: rook_bishop_attack("B3", "C5") => Output: "neither"

Input: rook_bishop_attack("G3", "E8") => Output: "neither"
```
#

<br />

# 2026.04.13 Challenge - Last Letter

My solution -> *[2026_04_13_name_initials](2026_04_13_name_initials.py)*

## **_Task condition:_**

Given a full name as a string, return their initials.

- Names to initialize are separated by a space.
- Initials should be made uppercase.
- Initials should be separated by dots.

For example, `"Tommy Millwood"` returns `"T.M."`.

### **_Examples_**

```
Input: get_initials("Tommy Millwood") => Output: "T.M."

Input: get_initials("Savanna Puddlesplash") => Output: "S.P."

Input: get_initials("Frances Cowell Conrad") => Output: "F.C.C."

Input: get_initials("Dragon") => Output: "D."

Input: get_initials("Dorothy Vera Clump Haverstock Norris") => Output: "D.V.C.H.N."
```
#

<br />

# 2026.04.14 Challenge - Last Letter

My solution -> *[2026_04_14_last_letter](2026_04_14_last_letter.py)*

## **_Task condition:_**

Given a string, return the letter from the string that appears last in the alphabet.

- If two or more letters tie for the last in the alphabet, return the first one.
- Ignore all non-letter characters.

### **_Examples_**

```
Input: get_last_letter("world") => Output: "w"

Input: get_last_letter("Hello World") => Output: "W"

Input: get_last_letter("The quick brown fox jumped over the lazy dog.") => Output: "L"

Input: get_last_letter("HeLl0") => Output: "z"

Input: get_last_letter("!#$ er@R asd fT.,> 2t0e9") => Output: "T"
```
#

<br />

# 2026.04.15 Challenge - Sorted Array Swap

My solution -> *[2026_04_15_sorted_array_swap](2026_04_15_sorted_array_swap.py)*

## **_Task condition:_**

Given an array of integers, return a new array using the following rules:

1. Sort the integers in ascending order
2. Then swap all values whose index is a multiple of `3` with the value before it.

### **_Examples_**

```
Input: sort_and_swap([3, 1, 2, 4, 6, 5]) => Output: [1, 2, 4, 3, 5, 6]

Input: sort_and_swap([9, 7, 5, 3, 1, 2, 4, 6, 8]) => Output: [1, 2, 4, 3, 5, 7, 6, 8, 9]

Input: sort_and_swap([1, 2, 3, 4, 5, 6, 7, 8, 9]) => Output: [1, 2, 4, 3, 5, 7, 6, 8, 9]

Input: sort_and_swap([12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11]) => Output: [1, 2, 4, 3, 5, 7, 6, 8, 10, 9, 11, 12]

Input: sort_and_swap([100, -50, 0, 75, -25, 50, -75, 25]) => Output: [-75, -50, 0, -25, 25, 75, 50, 100]

Input: sort_and_swap([5, 9, 13, 77, 88, 313, -10, -65, 0, 8, 99, 101, -4, 2]) => Output: [-65, -10, 0, -4, 2, 8, 5, 9, 77, 13, 88, 101, 99, 313]
```
#

<br />

# 2026.04.16 Challenge - String Math

My solution -> *[2026_04_16_string_math](2026_04_16_string_math.py)*

## **_Task condition:_**

Given a string with numbers and other characters, perform math on the numbers based on the count of non-digit characters between the numbers.

- If the count of characters separating two numbers is even, use addition.
- If it's odd, use subtraction.
- Consecutive digits form a single number.
- Operations are applied left to right.
- Ignore leading and trailing characters that aren't digits.

For example, given `"3ab10c8"`, return `5`. Add `3` and `10` to get `13` because there's an even number of characters between them. Then subtract `8` from `13` because there's an odd number of characters between the result and `8`.

### **_Examples_**

```
Input: do_math("3ab10c8") => Output: 5

Input: do_math("6MINUS4") => Output: 2

Input: do_math("9plus3") => Output: 12

Input: do_math("5fkwo#10i#%.<>15P=@20!#B/25") => Output: 15

Input: do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt") => Output: 67
```
#

<br />

# 2026.04.17 Challenge - Hidden Key

My solution -> *[2026_04_17_hidden_key](2026_04_17_hidden_key.py)*

## **_Task condition:_**

Welcome to the `250th` daily challenge!

Given an encoded string, decode it using an encryption key and return it.

To find the key:
- Look at all daily challenges up to today whose challenge number is a multiple of `25` (including this one).
- Take the first letter from each of those challenge titles and combine them into a string. If the title starts with a non-letter, find its first letter.

To decode the message, go over each letter in the encoded message and:
1. Look at the corresponding letter in the key (repeat the key if the message is longer than the key).
2. Convert the key letter to its corresponding number: `"A"` = 1, `"B"` = 2, ..., `"Z"` = 26.
3. Shift the encoded letter backward in the alphabet by that number.
4. If the shift goes before `"A"`, wrap around to `"Z"`.

For example, if the encoded message starts with `"Y"` and the first key letter is `"V"` (`22`), shift `"Y"` back `22` places to get `"C"`. Repeat this process for each letter to decode the full message.

- Only letters are shifted, spaces are returned as-is.
- All given and returned letters are uppercase.

### **_Examples_**

```
Input: decode("YAVJYNXE") => Output: "CONGRATS"

Input: decode("YALLUT PQUMJP") => Output: "CODING LEGEND"

Input: decode("UAC DYR EISAKYM") => Output: "YOU ARE AWESOME"

Input: decode("GQMS NBMZU") => Output: "KEEP GOING"

Input: decode("W IQQURV UG I ZDMDTRV IVW JQDHY TMHSA QB") => Output: "A WINNER IS A DREAMER WHO NEVER GIVES UP"
```
#

<br />

# 2026.04.20 Challenge - Acronym Finder

My solution -> *[2026_04_20_acronym_finder](2026_04_20_acronym_finder.py)*

## **_Task condition:_**

Given a string representing an acronym, return the full name of the organization it belongs to from the list below:

- `"National Avocado Storage Authority"`
- `"Cats Infiltration Agency"`
- `"Fluffy Beanbag Inspectors"`
- `"Department Of Jelly"`
- `"Wild Honey Organization"`
- `"Eating Pancakes Administration"`

Each letter in the given acronym should match the first letter of each word in the organization it belongs to, in the same order.

### **_Examples_**

```
Input: find_org("NASA") => Output: "National Avocado Storage Authority"

Input: find_org("CIA") => Output: "Cats Infiltration Agency"

Input: find_org("FBI") => Output: "Fluffy Beanbag Inspectors"

Input: find_org("DOJ") => Output: "Department Of Jelly"

Input: find_org("WHO") => Output: "Wild Honey Organization"

Input: find_org("EPA") => Output: "Eating Pancakes Administration"
```
#

<br />