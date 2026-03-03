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