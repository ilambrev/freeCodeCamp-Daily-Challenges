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