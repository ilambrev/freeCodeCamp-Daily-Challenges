# 2026.03.01 Challenge - Flattened

My solution -> *[2026_03_01_flattened](2026_03_01_flattened.py)*

## **_Task condition:_**

Given an array, determine if it is flat.

- An array is flat if none of its elements are arrays.

### **_Examples_**

```
Input: is_flat([1, 2, 3, 4]) => Output: True

Input: is_flat([1, [2, 3], 4]) => Output: False

Input: is_flat([1, 0, False, True, "a", "b"]) => Output: True

Input: is_flat(["a", [0], "b", True]) => Output: False

Input: is_flat([1, [2, [3, [4, [5]]]], 6]) => Output: False
```
#

<br />

# 2026.03.02 Challenge - Sum the Letters

My solution -> *[2026_03_02_sum_the_letters](2026_03_02_sum_the_letters.py)*

## **_Task condition:_**

Given a string, return the sum of its letters.

- Letters are `A-Z` in uppercase or lowercase
- Letter values are: `"A"` = 1, `"B"` = 2, ..., `"Z"` = 26
- Uppercase and lowercase letters have the same value.
- Ignore all non-letter characters.

### **_Examples_**

```
Input: sum_letters("Hello") => Output: 52

Input: sum_letters("freeCodeCamp") => Output: 94

Input: sum_letters("The quick brown fox jumps over the lazy dog.") => Output: 473

Input: sum_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci.") => Output: 1681

Input: sum_letters("</404>") => Output: 0
```
#

<br />

# 2026.03.03 Challenge - Perfect Cube Count

My solution -> *[2026_03_03_perfect_cube_count](2026_03_03_perfect_cube_count.py)*

## **_Task condition:_**

Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

- The lower number is not garanteed to be the first argument.
- A number is a perfect cube if there exists an integer (`n`) where `n * n * n = number`. For example, `27` is a perfect cube because `3 * 3 * 3 = 27`.

### **_Examples_**

```
Input: count_perfect_cubes(3, 30) => Output: 2

Input: count_perfect_cubes(1, 30) => Output: 3

Input: count_perfect_cubes(30, 0) => Output: 4

Input: count_perfect_cubes(-64, 64) => Output: 9

Input: count_perfect_cubes(9214, -8127) => Output: 41
```
#

<br />

# 2026.03.04 Challenge - Playing Card Values

My solution -> *[2026_03_04_playing_card_values](2026_03_04_playing_card_values.py)*

## **_Task condition:_**

Given an array of playing cards, return a new array with the numeric value of each card.

Card Values:

- An Ace (`"A"`) has a value of `1`.
- Numbered cards (`"2"` - `"10"`) have their face value: `2` - `10`, respectively.
- Face cards: Jack (`"J"`), Queen (`"Q"`), and King (`"K"`) are each worth `10`.

Suits:

- Each card has a suit: Spades (`"S"`), Clubs (`"C"`), Diamonds (`"D"`), or Hearts (`"H"`).

Card Format:

- Each card is represented as a string: `"valueSuit"`. For Example: `"AS"` is the Ace of Spades, `"10H"` is the Ten of Hearts, and `"QC"` is the Queen of Clubs.

### **_Examples_**

```
Input: card_values(["3H", "4D", "5S"]) => Output: [3, 4, 5]

Input: card_values(["AS", "10S", "10H", "6D", "7D"]) => Output: [1, 10, 10, 6, 7]

Input: card_values(["8D", "QS", "2H", "JC", "9C"]) => Output: [8, 10, 2, 10, 9]

Input: card_values(["AS", "KS"]) => Output: [1, 10]

Input: card_values(["10H", "JH", "QH", "KH", "AH"]) => Output: [10, 10, 10, 10, 1]
```
#

<br />

# 2026.03.05 Challenge - Smallest Gap

My solution -> *[2026_03_05_smallest_gap](2026_03_05_smallest_gap.py)*

## **_Task condition:_**

Given a string, return the substring between the two identical characters that have the smallest number of characters between them (`smallest gap`).

- There will always be at least one pair of matching characters.
- The returned substring should exclude the matching characters.
- If two or more gaps are the same length, return the characters from the first one.

For example, given `"ABCDAC"`, return `"DA"`.

- Only `"A"` and `"C"` repeat in the string.
- The number of characters between the two `"A"` characters is `3`, and between the `"C"` characters is `2`.
- So return the string between the two `"C"` characters.

### **_Examples_**

```
Input: smallest_gap("ABCDAC") => Output: "DA"

Input: smallest_gap("racecar") => Output: "e"

Input: smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4") => Output: "#q6e&rkf(p"

Input: smallest_gap("Hello World") => Output: ""

Input: smallest_gap("The quick brown fox jumps over the lazy dog.") => Output: "fox"
```
#

<br />

# 2026.03.06 Challenge - Trail Traversal

My solution -> *[2026_03_06_trail_traversal](2026_03_06_trail_traversal.py)*

## **_Task condition:_**

Given an array of strings representing your trail map, return a string of the moves needed to get to your goal.

The given strings will contain the values:

- `"C"`: Your current location
- `"G"`: Your goal
- `"T"`: Traversable parts of the trail
- `"-"`: Untraversable parts of the map

Return a string with the moves needed to follow the trail from your location to your goal where:

- `"R"` is a move right
- `"D"` is a move down
- `"L"` is a move left
- `"U"` is a move up
- There will always be a single continuous trail, without any branching, from your current location to your goal.
- Each trail location will have a maximum of two traversable locations touching it.

For example, given:

```
[
  "-CT--",
  "--T--",
  "--TT-",
  "---T-",
  "---G-"
]
```

Return `"RDDRDD"`.

### **_Examples_**

```
Input: navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"]) => Output: "RDDRDD"

Input: navigate_trail(["-----", "--TTG", "--T--", "--T--", "CTT--"]) => Output: "RRUUURR"

Input: navigate_trail(["-C----", "TT----", "T-----", "TTTTT-", "----G-"]) => Output: "DLDDRRRRD"

Input: navigate_trail(["--------", "-CTTT---", "----T---", "---GT---", "--------"]) => Output: "RRRDDL"

Input: navigate_trail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"]) => Output: "ULLLUUURRRRRRDDDR"
```
#

<br />

# 2026.03.07 Challenge - Element Size

My solution -> *[2026_03_07_element_size](2026_03_07_element_size.py)*

## **_Task condition:_**

Given a window size, the width of an element in viewport width `"vw"` units, and the height of an element in viewport height `"vh"` units, determine the size of the element in pixels.

- The given window size and returned element size are strings in the format `"width x height"`, `"1200 x 800"` for example.
- `"vw"` units are the percent of window width. `"50vw"` for example, is `50%` of the width of the window.
- `"vh"` units are the percent of window height. `"50vh"` for example, is `50%` of the height of the window.

### **_Examples_**

```
Input: get_element_size("1200 x 800", "50vw", "50vh") => Output: "600 x 400"

Input: get_element_size("320 x 480", "25vw", "50vh") => Output: "80 x 240"

Input: get_element_size("1000 x 500", "7vw", "3vh") => Output: "70 x 15"

Input: get_element_size("1920 x 1080", "95vw", "100vh") => Output: "1824 x 1080"

Input: get_element_size("1200 x 800", "0vw", "0vh") => Output: "0 x 0"

Input: get_element_size("1440 x 900", "100vw", "114vh") => Output: "1440 x 1026"
```
#

<br />

# 2026.03.08 Challenge - HSL Validator

My solution -> *[2026_03_08_hsl_validator](2026_03_08_hsl_validator.py)*

## **_Task condition:_**

Given a string, determine whether it is a valid CSS `hsl()` color value.

- A valid HSL value must be in the format `"hsl(h, s%, l%)"`, where:
  - `h` (hue) must be a number between `0` and `360` (inclusive).
  - `s` (saturation) must be a percentage between `0%` and `100%`.
  - `l` (lightness) must be a percentage between `0%` and `100%`.

- Spaces are only allowed:
  - After the opening parenthesis
  - Before and/or after the commas
  - Before and/or after closing parenthesis

- Optionally, the value can end with a semi-colon (`";"`).

For example, `"hsl(240, 50%, 50%)"` is a valid HSL value.

### **_Examples_**

```
Input: is_valid_hsl("hsl(240, 50%, 50%)") => Output: True

Input: is_valid_hsl("hsl( 200 , 50% , 75% )") => Output: True

Input: is_valid_hsl("hsl(99,60%,80%);") => Output: True

Input: is_valid_hsl("hsl(0, 0%, 0%) ;") => Output: True

Input: is_valid_hsl("hsl(  10  ,  20%   ,  30%   )    ;") => Output: True

Input: is_valid_hsl("hsl(361, 50%, 80%)") => Output: False

Input: is_valid_hsl("hsl(300, 101%, 70%)") => Output: False

Input: is_valid_hsl("hsl(200, 55%, 75)") => Output: False

Input: is_valid_hsl("hsl (80, 20%, 10%)") => Output: False
```
#

<br />

# 2026.03.09 Challenge - Array Sum

My solution -> *[2026_03_09_array_sum](2026_03_09_array_sum.py)*

## **_Task condition:_**

Given an array of numbers, return the sum of all the numbers.

### **_Examples_**

```
Input: sum_array([1, 2, 3, 4, 5]) => Output: 15

Input: sum_array([42]) => Output: 42

Input: sum_array([5, -2, 7, -3]) => Output: 7

Input: sum_array([203, 145, -129, 6293, 523, -919, 845, 2434]) => Output: 9395

Input: sum_array([0, 0]) => Output: 0
```
#

<br />

# 2026.03.10 Challenge - Array Insertion

My solution -> *[2026_03_10_array_insertion](2026_03_10_array_insertion.py)*

## **_Task condition:_**

Given an array, a value to insert into the array, and an index to insert the value at, return a new array with the value inserted at the specified index.

### **_Examples_**

```
Input: insert_into_array([2, 4, 8, 10], 6, 2) => Output: [2, 4, 6, 8, 10]

Input: insert_into_array(["the", "quick", "fox"], "brown", 2) => Output: ["the", "quick", "brown", "fox"]

Input: insert_into_array([], 0, 0) => Output: [0]

Input: insert_into_array([0, 1, 1, 2, 3, 8, 13], 5, 5) => Output: [0, 1, 1, 2, 3, 5, 8, 13]
```
#

<br />

# 2026.03.11 Challenge - Word Length Converter

My solution -> *[2026_03_11_word_length_converter](2026_03_11_word_length_converter.py)*

## **_Task condition:_**

Given a string of words, return a new string where each word is replaced by its length.

- Words in the given string will be separated by a single space
- Keep the spaces in the returned string.

For example, given `"hello world"`, return `"5 5"`.

### **_Examples_**

```
Input: convert_words("hello world") => Output: "5 5"

Input: convert_words("Thanks and happy coding") => Output: "6 3 5 6"

Input: convert_words("The quick brown fox jumps over the lazy dog") => Output: "3 5 5 3 5 4 3 4 3"

Input: convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl") => Output: "5 5 5 3 4 11 10 4 5 2 6 8 7 4 3 6 4"
```
#

<br />

# 2026.03.12 Challenge - Domino Chain Validator

My solution -> *[2026_03_12_domino_chain_validator](2026_03_12_domino_chain_validator.py)*

## **_Task condition:_**

Given a `2D` array representing a sequence of dominoes, determine whether it forms a valid chain.

- Each element in the array represents a domino and will be an array of two numbers from `1` to `6`, (inclusive).
- For the chain to be valid, the second number of each domino must match the first number of the next domino.
- The first number of the first domino and the last number of the last domino don't need to match anything.

### **_Examples_**

```
Input: is_valid_domino_chain([[1, 3], [3, 6], [6, 5]]) => Output: True

Input: is_valid_domino_chain([[6, 2], [3, 4], [4, 1]]) => Output: False

Input: is_valid_domino_chain([[2, 5], [5, 6], [5, 1]]) => Output: False

Input: is_valid_domino_chain([[4, 3], [3, 1], [1, 6], [6, 6], [6, 5], [5, 1], [1, 1], [1, 4], [4, 4], [4, 2]]) => Output: True

Input: is_valid_domino_chain([[2, 3], [3, 3], [3, 6], [6, 1], [1, 4], [3, 5], [5, 5], [5, 4], [4, 2], [2, 2]]) => Output: False
```
#

<br />

# 2026.03.13 Challenge - Parking Fee Calculator

My solution -> *[2026_03_13_parking_fee_calculator](2026_03_13_parking_fee_calculator.py)*

## **_Task condition:_**

Given two strings representing the time you parked your car and the time you picked it up, calculate the parking fee.

- The given strings will be in the format `"HH:MM"` using a `24-hour` clock. So `"14:00"` is `2pm` for example.
- The first string will be the time you parked your car, and the second will be the time you picked it up.
- If the pickup time is earlier than the entry time, it means the parking spanned past midnight into the next day.

Fee rules:

- Each hour parked costs `$3`.
- Partial hours are rounded up to the next full hour.
- If the parking spans overnight (past midnight), an additional `$10` overnight fee is applied.
- There is a minimum fee of `$5` (only used if the total would be less than `$5`).

Return the total cost in the format `"$cost"`, `"$5"` for example.

### **_Examples_**

```
Input: calculate_parking_fee("09:00", "11:00") => Output: "$6"

Input: calculate_parking_fee("10:00", "10:30") => Output: "$5"

Input: calculate_parking_fee("08:10", "10:45") => Output: "$9"

Input: calculate_parking_fee("14:40", "23:10") => Output: "$27"

Input: calculate_parking_fee("18:15", "01:30") => Output: "$34"

Input: calculate_parking_fee("11:11", "11:10") => Output: "$82"
```
#

<br />

# 2026.03.14 Challenge - Pi Day

My solution -> *[2026_03_14_pi_day](2026_03_14_pi_day.py)*

## **_Task condition:_**

Happy pi (π) day!

Given an integer (`n`), where `n` is between `1` and `1000` (inclusive), return the `n`th decimal of `π`.

- Make sure to return a number not a string.

`π` with its first five decimals is `3.14159`. So given `5` for example, return `9`, the fifth decimal.

You may have to find the first 1000 decimals of π somewhere.

### **_Examples_**

```
Input: get_pi_decimal(5) => Output: 9

Input: get_pi_decimal(10) => Output: 5

Input: get_pi_decimal(22) => Output: 6

Input: get_pi_decimal(39) => Output: 7

Input: get_pi_decimal(76) => Output: 2

Input: get_pi_decimal(384) => Output: 4

Input: get_pi_decimal(601) => Output: 0

Input: get_pi_decimal(1000) => Output: 9
```
#

<br />

# 2026.03.15 Challenge - Captured Chess Pieces

My solution -> *[2026_03_15_captured_chess_pieces](2026_03_15_captured_chess_pieces.py)*

## **_Task condition:_**

Given an array of strings representing chess pieces you still have on the board, calculate the value of the pieces your opponent has captured.

- In chess, you start with `16` pieces:

| Piece  | Abbreviation | Quantity | Value |
| :----: | :----------: | :------: | :---: |
| Pawn   | `"P"`        | 8        | 1     |
| Rook   | `"R"`        | 2        | 5     |
| Knight | `"N"`        | 2        | 3     |
| Bishop | `"B"`        | 2        | 3     |
| Queen  | `"Q"`        | 1        | 9     |
| King   | `"K"`        | 1        | 0     |

- The given array will only contain the abbreviations above.
- Any of the `16` pieces not included in the given array have been captured.
- Return the total value of all captured pieces, unless...
- If the King has been captured, return "Checkmate".

### **_Examples_**

```
Input: get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]) => Output: 8

Input: get_captured_value(["P", "P", "P", "P", "P", "R", "B", "K"]) => Output: 26

Input: get_captured_value(["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"]) => Output: 16

Input: get_captured_value(["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"]) => Output: 4

Input: get_captured_value(["P", "K"]) => Output: 38

Input: get_captured_value(["N", "P", "P", "B", "K", "P", "Q", "N", "P", "P", "R", "R", "P", "P", "P", "B"]) => Output: 0

Input: get_captured_value(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"]) => Output: "Checkmate"
```
#

<br />

# 2026.03.16 Challenge - Evenly Divisible

My solution -> *[2026_03_16_evenly_divisible](2026_03_16_evenly_divisible.py)*

## **_Task condition:_**

Given two integers, determine if you can evenly divide the first one by the second one.

### **_Examples_**

```
Input: is_evenly_divisible(4, 2) => Output: True

Input: is_evenly_divisible(7, 3) => Output: False

Input: is_evenly_divisible(5, 10) => Output: False

Input: is_evenly_divisible(48, 6) => Output: True

Input: is_evenly_divisible(3186, 9) => Output: True

Input: is_evenly_divisible(4192, 11) => Output: False
```
#

<br />

# 2026.03.17 Challenge - Anniversary Milestones

My solution -> *[2026_03_17_anniversary_milestones](2026_03_17_anniversary_milestones.py)*

## **_Task condition:_**

Given an integer representing the number of years a couple has been married, return their most recent anniversary milestone according to this chart:

| Years Married | Milestone    |
| :-----------: | :----------: |
| 1             | `"Paper"`    |
| 5             | `"Wood"`     |
| 10            | `"Tin"`      |
| 25            | `"Silver"`   |
| 40            | `"Ruby"`     |
| 50            | `"Gold"`     |
| 60            | `"Diamond"`  |
| 70            | `"Platinum"` |

- If they haven't reached the first milestone, return "Newlyweds".

### **_Examples_**

```
Input: get_milestone(0) => Output: "Newlyweds"

Input: get_milestone(1) => Output: "Paper"

Input: get_milestone(8) => Output: "Wood"

Input: get_milestone(10) => Output: "Tin"

Input: get_milestone(26) => Output: "Silver"

Input: get_milestone(45) => Output: "Ruby"

Input: get_milestone(50) => Output: "Gold"

Input: get_milestone(64) => Output: "Diamond"

Input: get_milestone(71) => Output: "Platinum"
```
#

<br />

# 2026.03.18 Challenge - Largest Number

My solution -> *[2026_03_18_largest_number](2026_03_18_largest_number.py)*

## **_Task condition:_**

Given a string of numbers separated by various punctuation, return the largest number.

- The given string will only contain numbers and separators.
- Separators can be commas (`","`), exclamation points (`"!"`), question marks (`"?"`), colons (`":"`), or semi-colons (`";"`).

### **_Examples_**

```
Input: largest_number("1,2") => Output: 2

Input: largest_number("4;15:60,26?52!0") => Output: 60

Input: largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011") => Output: -402

Input: largest_number("12;-50,99.9,49.1!-10.1?88?16") => Output: 99.9
```
#

<br />

# 2026.03.19 Challenge - Inverted Matrix

My solution -> *[2026_03_19_inverted_matrix](2026_03_19_inverted_matrix.py)*

## **_Task condition:_**

Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one value are swapped with the other.

For example, given:

```
[
  ["a", "b"],
  ["a", "a"]
]
```

Return:

```
[
  ["b", "a"],
  ["b", "b"]
]
```

### **_Examples_**

```
Input: invert_matrix([["a", "b"], ["a", "a"]]) => Output: [["b", "a"], ["b", "b"]]

Input: invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]) => Output: [[0, 1, 0], [0, 0, 0], [1, 0, 1]]

Input: invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]]) => Output: [["banana", "apple", "apple", "banana"], ["apple", "banana", "banana", "apple"], ["apple", "apple", "apple", "banana"]]

Input: invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]]) => Output: [[7, 6, 6, 6, 7], [6, 7, 6, 7, 6], [6, 6, 7, 6, 6], [6, 7, 6, 7, 6], [7, 6, 6, 6, 7]]

Input: invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]]) => Output: [[2.1, 1.2, 1.2, 1.2], [1.2, 2.1, 1.2, 2.1], [2.1, 2.1, 1.2, 1.2]]
```
#

<br />

# 2026.03.20 Challenge - Equinox Shadows

My solution -> *[2026_03_20_equinox_shadows](2026_03_20_equinox_shadows.py)*

## **_Task condition:_**

Today is the equinox, when the sun is directly above the equator and perfectly overhead at noon. Given a time, determine the shadow cast by a 4-foot vertical pole.

- The time will be a string in `"HH:MM"` 24-hour format (for example, `"15:00"` is 3pm).
- You will only be given a time in `30` minute increments.

Rules:

- The sun rises at 6am directly `"east"`, and sets at 6pm directly `"west"`.
- A shadow always points opposite the sun.
- The shadow's length (in feet) is the number of hours away from noon, cubed.
- There is no shadow before sunrise (`before 6am`), after sunset (`6pm or later`), or at noon.

Return:

- If a shadow exists, return `"(length)ft (direction)"`. For example, `"8ft west"`.
- Otherwise, return `"No shadow"`.

For example, given `"10:00"`, return `"8ft west"` because 10am is 2 hours from noon, so 2<sup>3</sup> = 8 feet, and the shadow points west because the sun is in the east at 10am.

### **_Examples_**

```
Input: get_shadow("10:00") => Output: "8ft west"

Input: get_shadow("15:00") => Output: "27ft east"

Input: get_shadow("12:00") => Output: "No shadow"

Input: get_shadow("17:30") => Output: "166.375ft east"

Input: get_shadow("05:00") => Output: "No shadow"

Input: get_shadow("06:00") => Output: "216ft west"

Input: get_shadow("18:00") => Output: "No shadow"

Input: get_shadow("07:30") => Output: "91.125ft west"

Input: get_shadow("00:00") => Output: "No shadow"
```
#

<br />

# 2026.03.21 Challenge - QR Decoder

My solution -> *[2026_03_21_qr_decoder](2026_03_21_qr_decoder.py)*

## **_Task condition:_**

Given a `6x6` matrix (array of arrays), representing a `QR code`, return the string of binary data in the code.

- The `QR code` may be given in any rotation of `90` degree increments.
- A correctly oriented code has a `2x2` group of `1`'s (orientation markers) in the bottom-left, top-left, and top-right corners.
- The three `2x2` orientation markers are not part of the binary data.
- The binary data is read left-to-right, top-to-bottom (like a book) when the `QR code` is correctly oriented.
- A code will always have exactly one valid orientation.

For example, given:

```
[
  "110011",
  "110011",
  "000000",
  "000000",
  "110000",
  "110001"
]
```

or given the same code with a different orientation:

```
[
  "110011",
  "110011",
  "000000",
  "000000",
  "000011",
  "100011"
]
```

Return `"000000000000000000000001"`, all the binary data excluding the three `2x2` orientation markers.

### **_Examples_**

```
Input: decode_qr(["110011", "110011", "000000", "000000", "110000", "110001"]) => Output: "000000000000000000000001"

Input: decode_qr(["100011", "000011", "000000", "000000", "110011", "110011"]) => Output: "000000000000000000000001"

Input: decode_qr(["110011", "111111", "010000", "110000", "110011", "110100"]) => Output: "001101000011000000110100"

Input: decode_qr(["011011", "101011", "101000", "100010", "110011", "111011"]) => Output: "010001000100010101010110"

Input: decode_qr(["111100", "110001", "100011", "001101", "110011", "110011"]) => Output: "010000100100100101001110"
```
#

<br />

# 2026.03.22 Challenge - Coffee Roast Detector

My solution -> *[2026_03_22_coffee_roast_detector](2026_03_22_coffee_roast_detector.py)*

## **_Task condition:_**

Given a string representing the beans used to make a cup of coffee, determine the roast of the cup.

- The given string will contain the following characters, each representing a type of bean:
  - An apostrophe (`'`) is a light roast bean worth `1` point each.
  - A dash (`-`) is a medium roast bean worth `2` points each.
  - A period (`.`) is a dark roast bean worth `3` points each.
- The roast level is determined by the average of all the beans.

Return:

- `"Light"` if the average is less than `1.75`.
- `"Medium"` if the average is `1.75` to `2.5`.
- `"Dark"` if the average is greater than `2.5`.

### **_Examples_**

```
Input: detect_roast("''-''''''-'-''--''''") => Output: "Light"

Input: detect_roast(".'-''-''..'''.-.-''-") => Output: "Medium"

Input: detect_roast("--.''--'-''.--..-.--") => Output: "Medium"

Input: detect_roast("-...'-......-..-...-") => Output: "Dark"

Input: detect_roast(".--.-..-......----.'") => Output: "Medium"

Input: detect_roast("..-..-..-..-....-.-.") => Output: "Dark"

Input: detect_roast("-'-''''''..-'.''-'.'") => Output: "Light"
```
#

<br />

# 2026.03.23 Challenge - No Consecutive Repeats

My solution -> *[2026_03_23_no_consecutive_repeats](2026_03_23_no_consecutive_repeats.py)*

## **_Task condition:_**

Given a string, determine if it has no repeating characters.

- A string has no repeats if it does not have the same character two or more times in a row.

### **_Examples_**

```
Input: has_no_repeats("hi world") => Output: True

Input: has_no_repeats("hello world") => Output: False

Input: has_no_repeats("abcdefghijklmnopqrstuvwxyz") => Output: True

Input: has_no_repeats("freeCodeCamp") => Output: False

Input: has_no_repeats("The quick brown fox jumped over the lazy dog.") => Output: True

Input: has_no_repeats("Mississippi") => Output: False
```
#

<br />

# 2026.03.24 Challenge - Passing Exam Count

My solution -> *[2026_03_24_passing_exam_count](2026_03_24_passing_exam_count.py)*

## **_Task condition:_**

Given an array of student exam scores and the score needed to pass it, return the number of students that passed the exam.

### **_Examples_**

```
Input: passing_count([90, 85, 75, 60, 50], 70) => Output: 3

Input: passing_count([100, 80, 75, 88, 72, 74, 79, 71, 60, 92], 75) => Output: 6

Input: passing_count([79, 60, 88, 72, 74, 59, 75, 71, 80, 92], 60) => Output: 9

Input: passing_count([76, 79, 80, 70, 71, 65, 79, 78, 59, 72], 85) => Output: 0

Input: passing_count([84, 65, 98, 53, 58, 71, 91, 80, 92, 70, 73, 83, 86, 69, 84, 77, 72, 58, 69, 75, 66, 68, 72, 96, 90, 63, 88, 63, 80, 67], 60) => Output: 27
```
#

<br />

# 2026.03.25 Challenge - Cooldown Time

My solution -> *[2026_03_25_cooldown_time](2026_03_25_cooldown_time.py)*

## **_Task condition:_**

Given two timestamps, the first representing when a user finished an exam, and the second representing the current time, determine whether the user can take an exam again.

- Both timestamps will be given the format: `"YYYY-MM-DDTHH:MM:SS"`, for example `"2026-03-25T14:00:00"`. Note that the time is `24-hour` clock.
- A user must wait at least `48` hours before retaking an exam.

### **_Examples_**

```
Input: can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00") => Output: True

Input: can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00") => Output: False

Input: can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00") => Output: True

Input: can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59") => Output: False
```
#

<br />

# 2026.03.26 Challenge - Movie Night

My solution -> *[2026_03_26_movie_night](2026_03_26_movie_night.py)*

## **_Task condition:_**

Given a string for the day of the week, another string for a showtime, and an integer number of tickets, return the total cost of the movie tickets for that showing.

The given day will be one of:

- `"Monday"`
- `"Tuesday"`
- `"Wednesday"`
- `"Thursday"`
- `"Friday"`
- `"Saturday"`
- `"Sunday"`

The showtime will be given in the format `"H:MMam"` or `"H:MMpm"`. For example `"10:00am"` or `"10:00pm"`.

Return the total cost in the format `"$D.CC"` using these rules:

- Weekend (`Friday - Sunday`): `$12.00` per ticket.
- Weekday (`Monday - Thursday`): `$10.00` per ticket.
- Matinee (`before 5:00pm`): subtract `$2.00` per ticket (except on `Tuesdays`).
- Tuesdays: all tickets are `$5.00` each.

### **_Examples_**

```
Input: get_movie_night_cost("Saturday", "10:00pm", 1) => Output: "$12.00"

Input: get_movie_night_cost("Sunday", "10:00am", 1) => Output: "$10.00"

Input: get_movie_night_cost("Tuesday", "7:20pm", 2) => Output: "$10.00"

Input: get_movie_night_cost("Wednesday", "5:40pm", 3) => Output: "$30.00"

Input: get_movie_night_cost("Monday", "11:50am", 4) => Output: "$32.00"

Input: get_movie_night_cost("Friday", "4:30pm", 5) => Output: "$50.00"

Input: get_movie_night_cost("Tuesday", "11:30am", 1) => Output: "$5.00"
```
#

<br />