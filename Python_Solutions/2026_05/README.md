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