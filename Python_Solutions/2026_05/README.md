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