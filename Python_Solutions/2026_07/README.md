# 2026.07.01 Challenge - Lucky Number

My solution -> *[2026_07_01_lucky_number](2026_07_01_lucky_number.py)*

## **_Task condition:_**

Given a string of a person's first and last name, calculate their lucky number using the following rules:

- First and last names are separated by a space
- Find the vowel and consonant count for each name
- Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
- Do the same for the two larger counts and the larger name
- Subtract the smaller value from the larger one to get their lucky number

If the final value is zero (`0`), return `13`.

### **_Examples_**

```
Input: get_lucky_number("John Doe") => Output: 21

Input: get_lucky_number("Olivia Lewis") => Output: 52

Input: get_lucky_number("James Wilson") => Output: 18

Input: get_lucky_number("Elizabeth Hernandez") => Output: 81

Input: get_lucky_number("Mike Walker") => Output: 32

Input: get_lucky_number("Chloe Perez") => Output: 13
```
#

<br />