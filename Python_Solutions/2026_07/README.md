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

# 2026.07.02 Challenge - Max Profit

My solution -> *[2026_07_02_max_profit](2026_07_02_max_profit.py)*

## **_Task condition:_**

Given an array of daily stock prices and a budget (in dollars), calculate the maximum profit you could make by buying and selling the stock over the given period.

- You may only sell after you buy.
- You can only buy whole shares.
- Return the maximum possible profit as a string, rounded down to the nearest cent and formatted to two decimal places.

### **_Examples_**

```
Input: get_max_profit([5, 6], 50) => Output: "10.00"

Input: get_max_profit([8, 2, 5, 10], 20) => Output: "80.00"

Input: get_max_profit([4, 5, 3, 6], 20) => Output: "18.00"

Input: get_max_profit([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200) => Output: "8.31"

Input: get_max_profit([15.38, 15.01, 14.99, 14.62, 14.28], 80) => Output: "0.00"

Input: get_max_profit([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25) => Output: "73.80"
```
#

<br />