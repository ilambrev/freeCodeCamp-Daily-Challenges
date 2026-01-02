# 2026.01.01 Challenge - Resolution Streak

My solution -> *[2026_01_01_resolution_streak](2026_01_01_resolution_streak.py)*

## **_Task condition:_**

Given an array of arrays, where each sub-array represents a day of your resolution activities and contains three integers: the number of steps walked that day, the minutes of screen time that day, and the number of pages read that day; determine if you are keeping your resolutions.

- The first sub-array is `day 1`, and second `day 2`, and so on.

A day is considered successful if all three of the following goals are met:

- You walked at least `10,000` steps.
- You had no more than `120` minutes of screen time.
- You read at least `five` pages.

If all of the given days are successful, return `"Resolution on track: N day streak."` Where `N` is the number of successful days.

If one or more days is not a success, return `"Resolution failed on day X: N day streak."`. Where `X` is the day number of the first unsuccessful day, and N is the number of successful days before the first unsuccessful day.

### **_Examples_**

```
Input: resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9]]) => Output: "Resolution on track: 3 day streak."

Input: resolution_streak([[10000, 120, 5], [10950, 121, 11]]) => Output: "Resolution failed on day 2: 1 day streak."

Input: resolution_streak([[15000, 110, 8], [12300, 60, 13], [10100, 120, 4], [9000, 125, 4]]) => Output: "Resolution failed on day 3: 2 day streak."

Input: resolution_streak([[11600, 76, 13], [12556, 64, 26], [10404, 32, 59], [9999, 44, 124], [7508, 23, 167], [10900, 80, 0]]) => Output: "Resolution failed on day 4: 3 day streak."

Input: resolution_streak([[10500, 75, 15], [11000, 90, 10], [10650, 100, 9], [10200, 60, 10], [10678, 87, 9], [12431, 67, 13], [10444, 107, 19], [10111, 95, 5], [10000, 120, 7], [11980, 101, 8]]) => Output: "Resolution on track: 10 day streak."
```

#

<br />

# 2026.01.02 Challenge - Nth Fibonacci Number

My solution -> *[2026_01_02_nth_fibonacci_number](2026_01_02_nth_fibonacci_number.py)*

## **_Task condition:_**

Given an integer `n`, return the `nth` number in the fibonacci sequence.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first `10` numbers in the sequence are `0`, `1`, `1`, `2`, `3`, `5`, `8`, `13`, `21`, `34`.


### **_Examples_**

```
Input: nth_fibonacci(4) => Output: 2

Input: nth_fibonacci(10) => Output: 34

Input: nth_fibonacci(15) => Output: 377

Input: nth_fibonacci(40) => Output: 63245986

Input: nth_fibonacci(75) => Output: 1304969544928657
```

#

<br />