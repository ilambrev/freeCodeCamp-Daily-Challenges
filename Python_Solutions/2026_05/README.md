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