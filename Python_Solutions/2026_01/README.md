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

# 2026.01.03 Challenge - Left-Handed Seat at the Table

My solution -> *[2026_01_03_left_handed_seat_at_the_table](2026_01_03_left_handed_seat_at_the_table.py)*

## **_Task condition:_**

Given a `4x2` matrix (array of arrays) representing the seating arrangement for a meal, determine how many seats a left-handed person can sit at.

- A left-handed person cannot sit where a right-handed person would be in the seat to the immediate left of them.

In the given matrix:

- An `"R"` is a seat occupied by a right-handed person.
- An `"L"` is a seat occupied by a left-handed person.
- An `"U"` is an unoccupied seat.
- Only unoccupied seats are available to sit at.
- The seats in the top row are facing `"down"`, and the seats in the bottom row are facing `"up"` (like a table), so left and right are relative to the seat's orientation.
- Corner seats only have one seat next to them.

For example, in the given matrix:

```
[
  ["U", "R", "U", "L"],
  ["U", "R", "R", "R"]
]
```

The top-left seat is cannot be sat in because there's a right-handed person to the left. The other two open seats can be sat in because there isn't a right-handed person to the left.

### **_Examples_**

```
Input: find_left_handed_seats([["U", "R", "U", "L"], ["U", "R", "R", "R"]]) => Output: 2

Input: find_left_handed_seats([["U", "U", "U", "U"], ["U", "U", "U", "U"]]) => Output: 8

Input: find_left_handed_seats([["U", "R", "U", "R"], ["L", "R", "R", "U"]]) => Output: 0

Input: find_left_handed_seats([["L", "U", "R", "R"], ["L", "U", "R", "R"]]) => Output: 1

Input: find_left_handed_seats([["U", "R", "U", "U"], ["U", "U", "L", "U"]]) => Output: 5
```

#

<br />

# 2026.01.04 Challenge - Leap Year Calculator

My solution -> *[2026_01_04_leap_year_calculator](2026_01_04_leap_year_calculator.py)*

## **_Task condition:_**

Given an integer year, determine whether it is a leap year.

A year is a leap year if it satisfies the following rules:

- The year is evenly divisible by `4`, and
- The year is not evenly divisible by `100`, unless
- The year is evenly divisible by `400`.

### **_Examples_**

```
Input: is_leap_year(2024) => Output: True

Input: is_leap_year(2023) => Output: False

Input: is_leap_year(2100) => Output: False

Input: is_leap_year(2000) => Output: True

Input: is_leap_year(1999) => Output: False

Input: is_leap_year(2040) => Output: True

Input: is_leap_year(2026) => Output: False
```

#

<br />

# 2026.01.05 Challenge - Tire Pressure

My solution -> *[2026_01_05_tire_pressure](2026_01_05_tire_pressure.py)*

## **_Task condition:_**

Given an array with four numbers representing the tire pressures in psi of the four tires in your vehicle, and another array of two numbers representing the minimum and maximum pressure for your tires in bar, return an array of four strings describing each tire's status.

- `1` bar equal `14.5038` psi.

Return an array with the following values for each tire:

- `"Low"` if the tire pressure is below the minimum allowed.
- `"Good"` if it's between the minimum and maximum allowed.
- `"High"` if it's above the maximum allowed.

### **_Examples_**

```
Input: tire_status([32, 28, 35, 29], [2, 3]) => Output: ["Good", "Low", "Good", "Low"]

Input: tire_status([32, 28, 35, 30], [2, 2.3]) => Output: ["Good", "Low", "High", "Good"]

Input: tire_status([29, 26, 31, 28], [2.1, 2.5]) => Output: ["Low", "Low", "Good", "Low"]

Input: tire_status([31, 31, 30, 29], [1.5, 2]) => Output: ["High", "High", "High", "Good"]

Input: tire_status([30, 28, 30, 29], [1.9, 2.1]) => Output: ["Good", "Good", "Good", "Good"]
```

#

<br />