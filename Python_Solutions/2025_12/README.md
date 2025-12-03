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