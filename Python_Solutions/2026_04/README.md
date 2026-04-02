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