# 2026.05.01 Challenge - Anagram Groups

My solution -> *[2026_05_01_anagram_groups](2026_05_01_anagram_groups.py)*

## **_Task condition:_**

Given an array of words, return a `2d` array of the words grouped into anagrams.

- Words are anagrams if they contain the same letters in any order.
- Each word belongs to exactly one group.
- Return order doesn't matter.

For example, given `["listen", "silent", "hello", "enlist", "world"]`, return `[["listen", "silent", "enlist"], ["hello"], ["world"]]`.

### **_Examples_**

```
Input: group_anagrams(["listen", "silent", "hello", "enlist", "world"]) => Output: [["listen", "silent", "enlist"], ["hello"], ["world"]]

Input: group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) => Output: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

Input: group_anagrams(["care", "race", "acre", "pots", "stop", "tops", "opts", "post", "spot", "evil", "vile", "live", "veil"]) => Output: [["acre", "care", "race"], ["evil", "live", "veil", "vile"], ["opts", "post", "pots", "spot", "stop", "tops"]]

Input: group_anagrams(["algorithms", "logarithms", "education", "cautioned", "auctioned", "triangle", "integral", "alerting", "relating"]) => Output: [["alerting", "integral", "relating", "triangle"], ["algorithms", "logarithms"], ["auctioned", "cautioned", "education"]]
```
#

<br />

# 2026.05.03 Challenge - Good Day

My solution -> *[2026_05_03_good_day](2026_05_03_good_day.py)*

## **_Task condition:_**

Given a time string in `"HH:MM"` format (24-hour clock), return:

- `"Good morning"` for times `05:00` to `11:59`
- `"Good afternoon"` for times `12:00` to `17:59`
- `"Good evening"` for times `18:00` to `21:59`
- `"Good night"` for times `22:00` to `04:59`

### **_Examples_**

```
Input: get_greeting("06:30") => Output: "Good morning"

Input: get_greeting("12:00") => Output: "Good afternoon"

Input: get_greeting("21:59") => Output: "Good evening"

Input: get_greeting("00:01") => Output: "Good night"

Input: get_greeting("11:30") => Output: "Good morning"
```
#

<br />

# 2026.05.04 Challenge - Parsec Converter

My solution -> *[2026_05_04_parsec_converter](2026_05_04_parsec_converter.py)*

## **_Task condition:_**

In a distant galaxy, parsecs are used to measure both time and distance. Given an integer number of parsecs, return its equivalent in time or distance.

- If the given integer is odd, it represents time. If it's even, it represents distance.

Use these conversion rates:

| Parsecs | Time/Distance |
| :-----: | :-----------: |
| 1       | 2 hours       |
| 2       | 6 light years |

Return the converted value as an integer.

### **_Examples_**

```
Input: convert_parsecs(1) => Output: 2

Input: convert_parsecs(2) => Output: 6

Input: convert_parsecs(31) => Output: 62

Input: convert_parsecs(88) => Output: 264

Input: convert_parsecs(17) => Output: 34

Input: convert_parsecs(14) => Output: 42
```
#

<br />

# 2026.05.05 Challenge - Narcissistic Number

My solution -> *[2026_05_05_narcissistic_number](2026_05_05_narcissistic_number.py)*

## **_Task condition:_**

Given a positive integer, determine whether it is a narcissistic number.

- A number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.

For example, `153` has `3` digits, and <strong><i>1<sup>3</sup> + 5<sup>3</sup> + 3<sup>3</sup> = 153</i></strong>, so it is narcissistic.

### **_Examples_**

```
Input: is_narcissistic(153) => Output: True

Input: is_narcissistic(154) => Output: False

Input: is_narcissistic(371) => Output: True

Input: is_narcissistic(512) => Output: False

Input: is_narcissistic(9) => Output: True

Input: is_narcissistic(11) => Output: False

Input: is_narcissistic(9474) => Output: True

Input: is_narcissistic(6549) => Output: False
```
#

<br />

# 2026.05.06 Challenge - Allergen Friendly Meals

My solution -> *[2026_05_06_allergen_friendly_meals](2026_05_06_allergen_friendly_meals.py)*

## **_Task condition:_**

Given an array of meals and an array of allergens to avoid, return the names of all the meals that contain none of the given allergens.

- Each meal is in the format `[meal, allergens]`, where `meal` is the name of the meal, and `allergens` is an array of the allergens the meal contains. For example, `["pasta", ["wheat", "milk"]]`.
- Allergens to avoid will be an array of strings.

Return safe meal names in the same order given. If no meal is safe, return an empty array.

### **_Examples_**

```
Input: get_allergen_friendly_meals([["pasta", ["wheat", "milk"]], ["salad", ["nuts"]]], ["milk"]) => Output: ["salad"]

Input: get_allergen_friendly_meals([["steak", ["soy"]], ["fried rice", []], ["fish tacos", ["fish", "wheat"]], ["chicken parmesan", ["wheat", "milk"]]], ["soy", "fish"]) => Output: ["fried rice", "chicken parmesan"]

Input: get_allergen_friendly_meals([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["eggs", "milk"]) => Output: ["oatmeal", "granola", "toast"]

Input: get_allergen_friendly_meals([["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["wheat", "nuts"]) => Output: ["granola", "yogurt", "eggs"]
```
#

<br />

# 2026.05.09 Challenge - Transposed Matrix

My solution -> *[2026_05_09_transposed_matrix](2026_05_09_transposed_matrix.py)*

## **_Task condition:_**

Given a matrix (an array of arrays), return the transposed version of it.

To transpose the matrix, swap the rows and columns. E.g: a value at index `[0, 1]` should move to index `[1, 0]`.

For example, given:

```
[
  [1, 2, 3],
  [4, 5, 6]
]
```

Return:

```
[
  [1, 4],
  [2, 5],
  [3, 6]
]
```

### **_Examples_**

```
Input: transpose([[1, 2, 3], [4, 5, 6]]) => Output: [[1, 4], [2, 5], [3, 6]]

Input: transpose([[1, 2], [3, 4], [5, 6]]) => Output: [[1, 3, 5], [2, 4, 6]]

Input: transpose([[1, 2], [3, 4], [5, 6], [7, 8]]) => Output: [[1, 3, 5, 7], [2, 4, 6, 8]]

Input: transpose([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"]]) => Output: [["a", "d", "g", "j"], ["b", "e", "h", "k"], ["c", "f", "i", "l"]]

Input: transpose([[True, False, True, False], [False, True, False, True], [True, True, False, False], [False, False, True, True], [True, False, False, True]]) => Output: [[True, False, True, False, True], [False, True, True, False, False], [True, False, False, True, False], [False, True, False, True, True]]
```
#

<br />

# 2026.05.10 Challenge - ISBN-13 Validator

My solution -> *[2026_05_10_isbn_13_validator](2026_05_10_isbn_13_validator.py)*

## **_Task condition:_**

Given a string, determine if it is a valid `ISBN-13` number.

A valid `ISBN-13`:

- Contains only digits and hyphens
- Has exactly `13` digits after removing hyphens
- Passes the following check:
  1. Multiply each digit by `1` or `3`, alternating (multiply the first digit by `1`, the second by `3`, the third by `1`, and so on).
  2. The sum of the results must be divisible by `10`.

### **_Examples_**

```
Input: is_valid_isbn_13("9780306406157") => Output: True

Input: is_valid_isbn_13("97803064061570") => Output: False

Input: is_valid_isbn_13("978-0-13-595705-9") => Output: True

Input: is_valid_isbn_13("978-030-64061A-4") => Output: False

Input: is_valid_isbn_13("9-7-8-0-1-3-4-7-5-7-5-9-9") => Output: True
```
#

<br />

# 2026.05.11 Challenge - Oldest Person

My solution -> *[2026_05_11_oldest_person](2026_05_11_oldest_person.py)*

## **_Task condition:_**

Given an array of objects, each with a `"name"` and `"age"` property, return an array containing the name of the oldest person.

If multiple people share the oldest age, return all of their names in the order they appear in the input.

### **_Examples_**

```
Input: get_oldest([{ "name": "Brenda", "age": 40 }]) => Output: ["Brenda"]

Input: get_oldest([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }]) => Output: ["Alice"]

Input: get_oldest([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }]) => Output: ["Bill", "Carol"]

Input: get_oldest([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]) => Output: ["George", "Holly", "Zach"]
```
#

<br />

# 2026.05.12 Challenge - Character Frequency

My solution -> *[2026_05_12_character_frequency](2026_05_12_character_frequency.py)*

## **_Task condition:_**

Given a string, return dictionary mapping each character to the number of times it appears.

### **_Examples_**

```
Input: get_frequency("test") => Output: {"t": 2, "e": 1, "s": 1}

Input: get_frequency("mississippi") => Output: {"m": 1, "i": 4, "s": 4, "p": 2}

Input: get_frequency("hello world") => Output: {"h": 1, "e": 1, "l": 3, "o": 2, " ": 1, "w": 1, "r": 1, "d": 1}

Input: get_frequency("She sells seashells by the seashore.") => Output: {"S": 1, "h": 4, "e": 7, " ": 5, "s": 7, "l": 4, "a": 2, "b": 1, "y": 1, "t": 1, "o": 1, "r": 1, ".": 1}

Input: get_frequency("The quick brown fox jumps over the lazy dog.") => Output: {"T": 1, "h": 2, "e": 3, " ": 8, "q": 1, "u": 2, "i": 1, "c": 1, "k": 1, "b": 1, "r": 2, "o": 4, "w": 1, "n": 1, "f": 1, "x": 1, "j": 1, "m": 1, "p": 1, "s": 1, "v": 1, "t": 1, "l": 1, "a": 1, "z": 1, "y": 1, "d": 1, "g": 1, ".": 1}
```
#

<br />

# 2026.05.14 Challenge - Mirror Image

My solution -> *[2026_05_14_mirror_image](2026_05_14_mirror_image.py)*

## **_Task condition:_**

Given two strings, determine if the second string is a mirror image of the first.

A mirror image is formed by reversing the string and replacing each character with its mirror equivalent.

- Symmetric characters look like themselves in a mirror:

`W`, `T`, `Y`, `U`, `I`, `O`, `H`, `A`, `X`, `V`, `M`, `w`, `o`, `x`, `v`, `0`, `8`, `=`, `+`, `:`, `|`, `-`, `_`, `*`, `^`, `!`, `.`, and the space (` `).

- Mirrored pairs swap with each other in a mirror:

| Character | Swaps with |
| :-------: | :--------: |
| `[`       | `]`        |
| `{`       | `}`        |
| `<`       | `>`        |
| `b`       | `d`        |
| `p`       | `q`        |
| `(`       | `)`        |

If either string includes a character not in the lists above, it doesn't have mirror image that can be created from the characters.

For example, the mirrored image of `"[HOW]"` is `"[WOH]"`.

### **_Examples_**

```
Input: is_mirror_image("[HOW]", "[WOH]") => Output: True

Input: is_mirror_image("MOM", "MOM") => Output: True

Input: is_mirror_image("vow", "wov") => Output: True

Input: is_mirror_image("TIM", "TIM") => Output: False

Input: is_mirror_image("{WOW}", "}WOW{") => Output: False

Input: is_mirror_image("XXVII", "IIV%X") => Output: False

Input: is_mirror_image("><(((*>", "<*)))><") => Output: True

Input: is_mirror_image("WTYUIOHAXVMwoxv08=+:|-_*^!.[]{}<>bdpq()", "()pqbd<>{}[].!^*_-|:+=80vxowMVXAHOIUYTW") => Output: True
```
#

<br />

# 2026.05.15 Challenge - Coffee Order Parser

My solution -> *[2026_05_15_coffee_order_parser](2026_05_15_coffee_order_parser.py)*

## **_Task condition:_**

Given a string for a coffee order, identify any menu items and return a formatted order.

Use the following menu items and prices:

| Item                | Price |
| :-----------------: | :---: |
| `"cold brew"`       | $4.50 |
| `"oat latte"`       | $5.00 |
| `"cappuccino"`      | $4.75 |
| `"espresso"`        | $3.00 |
| `"vanilla syrup"`   | $0.75 |
| `"caramel drizzle"` | $0.60 |
| `"extra shot"`      | $0.50 |
| `"oat milk"`        | $0.75 |
| `"cream"`           | $0.75 |

Return a string with the matched items joined by `" + "`, followed by a colon and space (`": "`), and the total price.

For example, given `"I'd like an oat latte with vanilla syrup and an extra shot please.", return "oat latte + vanilla syrup + extra shot: $6.25"`

Items should appear in the order they appear in the menu and the total price should always have two decimal places.

### **_Examples_**

```
Input: format_coffee_order("I'd like an oat latte with vanilla syrup and an extra shot please.") => Output: "oat latte + vanilla syrup + extra shot: $6.25"

Input: format_coffee_order("Give me a cappuccino with caramel drizzle, vanilla syrup, and some oat milk.") => Output: "cappuccino + vanilla syrup + caramel drizzle + oat milk: $6.85"

Input: format_coffee_order("Can I get a cold brew with some cream and an extra shot.") => Output: "cold brew + extra shot + cream: $5.75"

Input: format_coffee_order("Just an espresso please.") => Output: "espresso: $3.00"

Input: format_coffee_order("I'll take an oat latte with cream and an extra shot, and some vanilla syrup and caramel drizzle.") => Output: "oat latte + vanilla syrup + caramel drizzle + extra shot + cream: $7.60"
```
#

<br />

# 2026.05.17 Challenge - Mongo ID Date

My solution -> *[2026_05_17_mongo_id_date](2026_05_17_mongo_id_date.py)*

## **_Task condition:_**

Given a MongoDB ID string, return its creation time as an ISO 8601 string.

- A MongoDB ID is a 24-character hex string. The first 8 characters represent a Unix timestamp (in seconds) encoded as a base-16 integer.

For example, `"6a094b50bcf86cd799439011"` has a timestamp of `"6a094b50"` in hex, which is `1778994000` in decimal, representing a creation time of `"2026-05-17T05:00:00.000Z"`.

### **_Examples_**

```
Input: mongo_id_to_date("6a094b50bcf86cd799439011") => Output: "2026-05-17T05:00:00.000Z"

Input: mongo_id_to_date("695344eb1f4a4c1123042128") => Output: "2025-12-30T03:20:11.000Z"

Input: mongo_id_to_date("386da62df34123ac54617e56") => Output: "2000-01-01T07:01:01.000Z"

Input: mongo_id_to_date("69f571c3d7711807afd3dd55") => Output: "2026-05-02T03:38:43.000Z"

Input: mongo_id_to_date("68adce01c0e1144d0a90295a") => Output: "2025-08-26T15:08:49.000Z"
```
#

<br />

# 2026.05.18 Challenge - Bingo Range

My solution -> *[2026_05_18_bingo_range](2026_05_18_bingo_range.py)*

## **_Task condition:_**

Given a bingo letter, return the number range associated with that letter.

| Letter | Number Range |
| :----: | :----------: |
| "B"    | 1-15         |
| "I"    | 16-30        |
| "N"    | 31-45        |
| "G"    | 46-60        |
| "O"    | 61-75        |

Return an array with all numbers in the range from smallest to largest.

### **_Examples_**

```
Input: get_bingo_range("B") => Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Input: get_bingo_range("I") => Output: [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

Input: get_bingo_range("N") => Output: [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]

Input: get_bingo_range("G") => Output: [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]

Input: get_bingo_range("O") => Output: [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
```
#

<br />

# 2026.05.19 Challenge - Sleep Debt

My solution -> *[2026_05_19_sleep_debt](2026_05_19_sleep_debt.py)*

## **_Task condition:_**

Given an array of hours slept each night leading up to today, and a target number of hours per night, return how many hours of sleep you need tonight to eliminate your sleep debt.

- Include tonight's hours in the total time needed to catch up.
- If you've slept enough to cover tonight's target or more, return `0`.

### **_Examples_**

```
Input: sleep_debt([6, 6, 6, 6, 6, 6], 8) => Output: 20

Input: sleep_debt([6, 7, 8, 4, 8, 6], 7) => Output: 10

Input: sleep_debt([10, 10, 9, 10, 9, 11], 9) => Output: 4

Input: sleep_debt([8, 7, 6, 7, 6, 8], 6) => Output: 0

Input: sleep_debt([8, 9, 10, 9, 10, 7], 7) => Output: 0
```
#

<br />

# 2026.05.20 Challenge - String Zipper

My solution -> *[2026_05_20_string_zipper](2026_05_20_string_zipper.py)*

## **_Task condition:_**

Given two strings, return a new string that interleaves their characters one at a time. If one string is longer, append the remaining characters at the end.

Begin with the first character of the first string.

### **_Examples_**

```
Input: zip_strings("abc", "123") => Output: "a1b2c3"

Input: zip_strings("acegikmoqsuwy", "bdfhjlnprtvxz") => Output: "abcdefghijklmnopqrstuvwxyz"

Input: zip_strings("day", "night") => Output: "dnaiyght"

Input: zip_strings("python", "javascript") => Output: "pjyatvhaosncript"

Input: zip_strings("feCdCm", "reoeap") => Output: "freeCodeCamp"
```
#

<br />

# 2026.05.21 Challenge - I Before E

My solution -> *[2026_05_21_i_before_e](2026_05_21_i_before_e.py)*

## **_Task condition:_**

Given a word or sentence, return a corrected version where every word follows the `"I before E except after C"` rule.

- If a word contains `"ei"` not preceded by `"c"`, replace it with `"ie"`.
- If a word contains `"ie"` preceded by `"c"`, replace it with `"ei"`.
- All other words are left unchanged.

### **_Examples_**

```
Input: i_before_e("beleive") => Output: "believe"

Input: i_before_e("recieve") => Output: "receive"

Input: i_before_e("we recieved a breif") => Output: "we received a brief"

Input: i_before_e("she beleived the friendly niece could percieve the greif") => Output: "she believed the friendly niece could perceive the grief"

Input: i_before_e("we recieved relief after the theif gave us a breif piece of feirce deceit") => Output: "we received relief after the thief gave us a brief piece of fierce deceit"
```
#

<br />

# 2026.05.22 Challenge - Meeting Time

My solution -> *[2026_05_22_meeting_time](2026_05_22_meeting_time.py)*

## **_Task condition:_**

Given a 3D array representing availability windows for multiple people, return the earliest time where everyone has one hour free. If no such time exists, return `"None"`.

- Each person's availability is an array of `[start, end]` integer pairs in `24-hour` time. For example, `[10, 12]` would mean the person is available from `10 to 12`. Start times range from `0-23`, and end times range from `1-24`.

For example, given:

```
[
  [[10, 12], [15, 16]], // person 1
  [[11, 14], [15, 16]]  // person 2
]
```

Return `11`, the start of their first shared free hour.

### **_Examples_**

```
Input: get_meeting_time([[[10, 12], [15, 16]], [[11, 14], [15, 16]]]) => Output: 11

Input: get_meeting_time([[[9, 10], [12, 15]], [[10, 11], [13, 14]], [[9, 11], [10, 14]]]) => Output: 13

Input: get_meeting_time([[[7, 8], [9, 11], [12, 14], [15, 16]], [[8, 11], [12, 13], [14, 15]]]) => Output: 9

Input: get_meeting_time([[[7, 8], [10, 12], [13, 15]], [[8, 11], [12, 13], [14, 15]], [[6, 7], [8, 9], [12, 13]]]) => Output: None

Input: get_meeting_time([[[1, 3], [4, 6], [8, 10], [20, 23]], [[15, 16], [17, 18], [19, 22], [23, 24]], [[14, 16], [17, 23]], [[2, 4], [5, 6], [18, 19], [21, 22], [23, 24]]]) => Output: 21
```
#

<br />

# 2026.05.25 Challenge - Secret Number

My solution -> *[2026_05_25_secret_number](2026_05_25_secret_number.py)*

## **_Task condition:_**

Given a secret number and a guess, determine if the guess is correct.

Return:

- `"higher"` if the secret number is higher than the guess.
- `"lower"` if the secret number is lower than the guess.
- `"you got it!"` if the guess is correct.

### **_Examples_**

```
Input: guess_number(50, 30) => Output: "higher"

Input: guess_number(85, 99) => Output: "lower"

Input: guess_number(2026, 2026) => Output: "you got it!"

Input: guess_number(92904, 11283) => Output: "higher"

Input: guess_number(230495, 423920) => Output: "lower"

Input: guess_number(120349, 120349) => Output: "you got it!"
```
#

<br />

# 2026.05.26 Challenge - Sum of Differences

My solution -> *[2026_05_26_sum_of_differences](2026_05_26_sum_of_differences.py)*

## **_Task condition:_**

Given an array of numbers, return the sum of the differences between each number and the one that follows it.

For example, given `[1, 3, 4]`, return `3` (2 + 1).

### **_Examples_**

```
Input: sum_of_differences([1, 3, 4]) => Output: 3

Input: sum_of_differences([5, -3, 3, 9, 10]) => Output: 5

Input: sum_of_differences([9, 6, 15, -20, 33, 14, 25, 16, -7]) => Output: -16

Input: sum_of_differences([50, 102, -46, 82, -49, 29, 71, 902, -237, 111, -61, 75]) => Output: 25
```
#

<br />

# 2026.05.27 Challenge - Pizza Party

My solution -> *[2026_05_27_pizza_party](2026_05_27_pizza_party.py)*

## **_Task condition:_**

Given an array of hours worked today per person, return the number of pizzas to order for a pizza party.

- Divide each person's hours worked by `3` to get their slice count.
- You can't eat a partial slice, so round each person's slice count up to the nearest whole number.
- Each person gets a minimum of two slices.
- Each pizza has `8` slices. Round the total number of pizzas up to the nearest whole pizza.

### **_Examples_**

```
Input: get_pizzas_to_order([8, 8, 8]) => Output: 2

Input: get_pizzas_to_order([10, 9, 8, 2, 2, 6, 10]) => Output: 3

Input: get_pizzas_to_order([1, 2, 3, 4, 5]) => Output: 2

Input: get_pizzas_to_order([8, 8, 8, 8, 8, 8, 8, 8]) => Output: 3

Input: get_pizzas_to_order([9, 9, 6]) => Output: 1

Input: get_pizzas_to_order([10, 12, 16, 9, 8, 11, 15, 8, 0]) => Output: 5
```
#

<br />