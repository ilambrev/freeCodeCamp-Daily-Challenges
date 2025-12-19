# 2025.12.01 Challenge - Miles to Kilometers

My solution -> *[2025_12_01_miles_to_kilometers](2025_12_01_miles_to_kilometers.py)*

## **_Task condition:_**

Given a distance in miles as a number, return the equivalent distance in kilometers.

- The input will always be a non-negative number.
- `1` mile equals `1.60934` kilometers.
- Round the result to two decimal places.

### **_Examples_**

```
Input: convert_to_km(1) => Output: 1.61

Input: convert_to_km(21) => Output: 33.8

Input: convert_to_km(3.5) => Output: 5.63

Input: convert_to_km(0) => Output: 0

Input: convert_to_km(0.621371) => Output: 1
```

#

<br />

# 2025.12.02 Challenge - Camel to Snake

My solution -> *[2025_12_02_camel_to_snake](2025_12_02_camel_to_snake.py)*

## **_Task condition:_**

Given a string in camel case, return the snake case version of the string using the following rules:

- The input string will contain only letters (`A-Z` and `a-z`) and will always start with a lowercase letter.
- Every uppercase letter in the camel case string starts a new word.
- Convert all letters to lowercase.
- Separate words with an underscore (`_`).

### **_Examples_**

```
Input: to_snake("helloWorld") => Output: "hello_world"

Input: to_snake("myVariableName") => Output: "my_variable_name"

Input: to_snake("freecodecampDailyChallenges") => Output: "freecodecamp_daily_challenges"
```

#

<br />

# 2025.12.03 Challenge - Markdown Ordered List Item Converter

My solution -> *[2025_12_03_markdown_ordered_list_ltem_converter](2025_12_03_markdown_ordered_list_ltem_converter.py)*

## **_Task condition:_**

Given a string representing an ordered list item in Markdown, return the equivalent HTML string.

A valid ordered list item in Markdown must:

- Start with zero or more spaces, followed by
- A number (`1` or greater) and a period (`.`), followed by
- At least one space, and then
- The list item text.

If the string doesn't have the exact format above, return `"Invalid format"`. Otherwise, wrap the list item text in `li` tags and return the string.

For example, given `"1. My item"`, return `"<li>My item</li>"`

### **_Examples_**

```
Input: convert_list_item("1. My item") => Output: "<li>My item</li>"

Input: convert_list_item(" 1.  Another item") => Output: "<li>Another item</li>"

Input: convert_list_item("1 . invalid item") => Output: "Invalid format"

Input: convert_list_item("2. list item text") => Output: "<li>list item text</li>"

Input: convert_list_item(". invalid again") => Output: "Invalid format"

Input: convert_list_item("A. last invalid") => Output: "Invalid format"
```

**_NOTES:_**

- The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

#

<br />

# 2025.12.04 Challenge - Permutation Count

My solution -> *[2025_12_04_permutation_count](2025_12_04_permutation_count.py)*

## **_Task condition:_**

Given a string, return the number of distinct permutations that can be formed from its characters.

- A permutation is any reordering of the characters in the string.
- Do not count duplicate permutations.
- If the string contains repeated characters, repeated arrangements should only be counted once.
- The string will contain only letters (`A-Z`, `a-z`).

For example, given `"abb"`, return `3` because there's three unique ways to arrange the letters: `"abb"`, `"bab"`, and `"bba"`.

### **_Examples_**

```
Input: count_permutations("abb") => Output: 3

Input: count_permutations("abc") => Output: 6

Input: count_permutations("racecar") => Output: 630

Input: count_permutations("freecodecamp") => Output: 39916800
```

#

<br />

# 2025.12.05 Challenge - Symmetric Difference

My solution -> *[2025_12_05_symmetric_difference](2025_12_05_symmetric_difference.py)*

## **_Task condition:_**

Given two arrays, return a new array containing the symmetric difference of them.

- The symmetric difference between two sets is the set of values that appear in either set, but not both.
- Return the values in the order they first appear in the input arrays.

### **_Examples_**

```
Input: difference([1, 2, 3], [3, 4, 5]) => Output: [1, 2, 4, 5]

Input: difference(["a", "b"], ["c", "b"]) => Output: ["a", "c"]

Input: difference([1, "a", 2], [2, "b", "a"]) => Output: [1, "b"]

Input: difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]) => Output: [2, 4, 6, 8]
```

#

<br />

# 2025.12.06 Challenge - Date Formatter

My solution -> *[2025_12_06_date_formatter](2025_12_06_date_formatter.py)*

## **_Task condition:_**

Given a date in the format `"Month day, year"`, return the date in the format `"YYYY-MM-DD"`.

- The given month will be the full English month name. For example: `"January"`, `"February"`, etc.
- In the return value, pad the month and day with leading zeros if necessary to ensure two digits.

For example, given `"December 6, 2025"`, return `"2025-12-06"`.

### **_Examples_**

```
Input: format_date("December 6, 2025") => Output: "2025-12-06"

Input: format_date("January 1, 2000") => Output: "2000-01-01"

Input: format_date("November 11, 1111") => Output: "1111-11-11"

Input: format_date("September 7, 512") => Output: "512-09-07"

Input: format_date("May 4, 1950") => Output: "1950-05-04"

Input: format_date("February 29, 1992") => Output: "1992-02-29"
```

#

<br />

# 2025.12.07 Challenge - String Compression

My solution -> *[2025_12_07_string_compression](2025_12_07_string_compression.py)*

## **_Task condition:_**

Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

- Only consecutive duplicates are compressed.
- Words are separated by single spaces.

For example, given `"yes yes yes please"`, return `"yes(3) please"`.

### **_Examples_**

```
Input: compress_string("yes yes yes please") => Output: "yes(3) please"

Input: compress_string("I have have have apples") => Output: "I have(3) apples"

Input: compress_string("one one three and to the the the the") => Output: "one(2) three and to the(4)"

Input: compress_string("route route route route route route tee tee tee tee tee tee") => Output: "route(6) tee(6)"
```

#

<br />

# 2025.12.08 Challenge - Pounds to Kilograms

My solution -> *[2025_12_08_pounds_to_kilograms](2025_12_08_pounds_to_kilograms.py)*

## **_Task condition:_**

Given a weight in pounds as a number, return the string `"(lbs) pounds equals (kgs) kilograms."`.

- Replace `"(lbs)"` with the input number.
- Replace `"(kgs)"` with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
- `1` pound equals `0.453592` kilograms.
- If the input is `1`, use `"pound"` instead of `"pounds"`.
- If the converted value is `1`, use `"kilogram"` instead of `"kilograms"`.

### **_Examples_**

```
Input: convert_to_kgs(1) => Output: "1 pound equals 0.45 kilograms."

Input: convert_to_kgs(0) => Output: "0 pounds equals 0.00 kilograms."

Input: convert_to_kgs(100) => Output: "100 pounds equals 45.36 kilograms."

Input: convert_to_kgs(2.5) => Output: "2.5 pounds equals 1.13 kilograms."

Input: convert_to_kgs(2.20462) => Output: "2.20462 pounds equals 1.00 kilogram."
```

#

<br />

# 2025.12.09 Challenge - Most Frequent

My solution -> *[2025_12_09_most_frequent](2025_12_09_most_frequent.py)*

## **_Task condition:_**

Given an array of elements, return the element that appears most frequently.

- There will always be a single most frequent element.

### **_Examples_**

```
Input: most_frequent(["a", "b", "a", "c"]) => Output: "a"

Input: most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]) => Output: 2

Input: most_frequent([True, False, "False", "True", False]) => Output: False

Input: most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]) => Output: 40
```

#

<br />

# 2025.12.10 Challenge - Markdown Bold Parser

My solution -> *[2025_12_10_markdown_bold_parser](2025_12_10_markdown_bold_parser.py)*

## **_Task condition:_**

Given a string that may include some bold text in Markdown, return the equivalent HTML string.

- Bold text in Markdown is any text that starts and ends with two asterisks (`**`) or two underscores (`__`).
- There cannot be any spaces between the text and the asterisks or underscores, but there can be spaces in the text itself.
- Convert all bold occurrences to HTML `b` tags and return the string.

For example, given `"**This is bold**"`, return `"<b>This is bold</b>"`.

### **_Examples_**

```
Input: parse_bold("**This is bold**") => Output: "<b>This is bold</b>"

Input: parse_bold("__This is also bold__") => Output: "<b>This is also bold</b>"

Input: parse_bold("**This is not bold **") => Output: "**This is not bold **"

Input: parse_bold("__ This is also not bold__") => Output: "__ This is also not bold__"

Input: parse_bold("The **quick** brown fox __jumps__ over the **lazy** dog.") => Output: "The <b>quick</b> brown fox <b>jumps</b> over the <b>lazy</b> dog."
```

**_NOTES:_**

- The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

#

<br />

# 2025.12.12 Challenge - Inventory Update

My solution -> *[2025_12_12_inventory_update](2025_12_12_inventory_update.py)*

## **_Task condition:_**

Given a 2D array representing the inventory of your store, and another 2D array representing a shipment you have received, return your updated inventory.

- Each element in the arrays will have the format: `[quantity, "item"]`, where `quantity` is an integer and `"item"` is a string.
- Update items in the inventory by adding the quantity of any matching items from the shipment.
- If a received item does not exist in the current inventory, add it as a new entry to the end of the inventory.
- Return inventory in the order it was given with new items at the end in the order they appear in the shipment.

For example, given an inventory of `[[2, "apples"], [5, "bananas"]]` and a shipment of `[[1, "apples"], [3, "bananas"]]`, return `[[3, "apples"], [8, "bananas"]]`.

### **_Examples_**

```
Input: update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]) => Output: [[3, "apples"], [8, "bananas"]]

Input: update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]) => Output: [[3, "apples"], [8, "bananas"], [4, "oranges"]]

Input: update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]]) => Output: [[10, "apples"], [30, "bananas"], [20, "oranges"]]

Input: update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]) => Output: [[1, "Bowling Ball"], [0, "Dirty Socks"], [1, "Hair Pin"], [0, "Microphone"], [1, "Half-Eaten Apple"], [1, "Toothpaste"]]
```

#

<br />

# 2025.12.13 Challenge - Game of Life

My solution -> *[2025_12_13_game_of_life](2025_12_13_game_of_life.py)*

## **_Task condition:_**

Given a matrix (array of arrays) representing the current state in `Conway's Game of Life`, return the next state of the matrix using these rules:

- Each cell is either `1` (alive) or `0` (dead).
- A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
- Cells on the edges have fewer than eight neighbors.

Rules for updating each cell:

- Any live cell with fewer than two live neighbors dies (underpopulation).
- Any live cell with two or three live neighbors lives on.
- Any live cell with more than three live neighbors dies (overpopulation).
- Any dead cell with exactly three live neighbors becomes alive (reproduction).

For example, given:
```
[
  [0, 1, 0],
  [0, 1, 1],
  [1, 1, 0]
]
```

return:
```
[
  [0, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]
```

Each cell updates according to the number of live neighbors. For instance, `[0][0]` stays dead (`2` live neighbors), `[0][1]` stays alive (`2` live neighbors), `[0][2]` dies (`3` live neighbors), and so on.

### **_Examples_**

```
Input: game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]]) => Output: [[0, 1, 1], [0, 0, 1], [1, 1, 1]]

Input: game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]) => Output: [[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 1, 1, 1]]

Input: game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) => Output: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

Input: game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]]) => Output: [[1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
```

#

<br />

# 2025.12.14 Challenge - Capitalize It

My solution -> *[2025_12_14_capitalize_it](2025_12_14_capitalize_it.py)*

## **_Task condition:_**

Given a string title, return a new string formatted in title case using the following rules:

- Capitalize the first letter of each word.
- Make all other letters in each word lowercase.
- Words are always separated by a single space.

### **_Examples_**

```
Input: title_case("hello world") => Output: "Hello World"

Input: title_case("the quick brown fox") => Output: "The Quick Brown Fox"

Input: title_case("JAVASCRIPT AND PYTHON") => Output: "Javascript And Python"

Input: title_case("AvOcAdO tOAst fOr brEAkfAst") => Output: "Avocado Toast For Breakfast"
```

#

<br />

# 2025.12.15 Challenge - Speed Check

My solution -> *[2025_12_15_speed_check](2025_12_15_speed_check.py)*

## **_Task condition:_**

Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine whether you are speeding and if you will get a warning or a ticket.

- `1` mile equals `1.60934` kilometers.
- If you are travelling less than or equal to the speed limit, return `"Not Speeding"`.
- If you are travelling `5` KPH or less over the speed limit, return `"Warning"`.
- If you are travelling more than `5` KPH over the speed limit, return `"Ticket"`.

### **_Examples_**

```
Input: speed_check(30, 70) => Output: "Not Speeding"

Input: speed_check(40, 60) => Output: "Warning"

Input: speed_check(40, 65) => Output: "Not Speeding"

Input: speed_check(60, 90) => Output: "Ticket"

Input: speed_check(65, 100) => Output: "Warning"

Input: speed_check(88, 40) => Output: "Ticket"
```

#

<br />

# 2025.12.16 Challenge - Consonant Count

My solution -> *[2025_12_16_consonant_count](2025_12_16_consonant_count.py)*

## **_Task condition:_**

Given a string and a target number, determine whether the string contains exactly the target number of consonants.

- Consonants are all alphabetic characters except `"a"`, `"e"`, `"i"`, `"o"`, and `"u"` in any case.
- Ignore digits, punctuation, spaces, and other non-letter characters when counting.

### **_Examples_**

```
Input: has_consonant_count("helloworld", 7) => Output: True

Input: has_consonant_count("eieio", 5) => Output: False

Input: has_consonant_count("freeCodeCamp Rocks!", 11) => Output: True

Input: has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24) => Output: False

Input: has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23) => Output: True
```

#

<br />

# 2025.12.18 Challenge - Checkerboard

My solution -> *[2025_12_18_checkerboard](2025_12_18_checkerboard.py)*

## **_Task condition:_**

Given an array with two numbers, the first being the number of rows and the second being the number of columns, return a matrix (an array of arrays) filled with `"X"` and `"O"` characters of the given size.

- The characters should alternate like a checkerboard.
- The top-left cell must always be `"X"`.

For example, given `[3, 3]`, return:

```
[
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["X", "O", "X"]
]
```

### **_Examples_**

```
Input: create_board([3, 3]) => Output: [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]

Input: create_board([6, 1]) => Output: [["X"], ["O"], ["X"], ["O"], ["X"], ["O"]]

Input: create_board([2, 10]) => Output: [["X", "O", "X", "O", "X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]]

Input: create_board([5, 4]) => Output: [["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"], ["X", "O", "X", "O"]]
```

#

<br />

# 2025.12.19 Challenge - Pairwise

My solution -> *[2025_12_19_pairwise](2025_12_19_pairwise.py)*

## **_Task condition:_**

Given an array of integers and a target number, find all pairs of elements in the array whose values add up to the target and return the sum of their indices.

For example, given `[2, 3, 4, 6, 8]` and `10`, you will find two valid pairs:

- `2` and `8` (2 + 8 = 10), whose indices are `0` and `4`
- `4` and `6` (4 + 6 = 10), whose indices are `2` and `3`

Add all the indices together to get a return value of `9`.

### **_Examples_**

```
Input: pairwise([2, 3, 4, 6, 8], 10) => Output: 9

Input: pairwise([4, 1, 5, 2, 6, 3], 7) => Output: 15

Input: pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20) => Output: 22

Input: pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24) => Output: 10
```

#

<br />