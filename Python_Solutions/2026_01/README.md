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

# 2026.01.06 Challenge - vOwElcAsE

My solution -> *[2026_01_06_vowelcase](2026_01_06_vowelcase.py)*

## **_Task condition:_**

Given a string, return a new string where all vowels are converted to uppercase and all other alphabetical characters are converted to lowercase.

- Vowels are `"a"`, `"e"`, `"i"`, `"o"`, and `"u"` in any case.
- Non-alphabetical characters should remain unchanged.

### **_Examples_**

```
Input: vowel_case("vowelcase") => Output: "vOwElcAsE"

Input: vowel_case("coding is fun") => Output: "cOdIng Is fUn"

Input: vowel_case("HELLO, world!") => Output: "hEllO, wOrld!"

Input: vowel_case("git cherry-pick") => Output: "gIt chErry-pIck"

Input: vowel_case("HEAD~1") => Output: "hEAd~1"

```

#

<br />

# 2026.01.08 Challenge - Sorted Array?

My solution -> *[2026_01_08_sorted_array](2026_01_08_sorted_array.py)*

## **_Task condition:_**

Given an array of numbers, determine if the numbers are sorted in ascending order, descending order, or neither.

If the given array is:

- In ascending order (lowest to highest), return `"Ascending"`.
- In descending order (highest to lowest), return `"Descending"`.
- Not sorted in ascending or descending order, return `"Not sorted"`.

### **_Examples_**

```
Input: is_sorted([1, 2, 3, 4, 5]) => Output: "Ascending"

Input: is_sorted([10, 8, 6, 4, 2]) => Output: "Descending"

Input: is_sorted([1, 3, 2, 4, 5]) => Output: "Not sorted"

Input: is_sorted([3.14, 2.71, 1.61, 0.57]) => Output: "Descending"

Input: is_sorted([12.3, 23.4, 34.5, 45.6, 56.7, 67.8, 78.9]) => Output: "Ascending"

Input: is_sorted([0.4, 0.5, 0.3]) => Output: "Not sorted"
```

#

<br />

# 2026.01.09 Challenge - Circular Prime

My solution -> *[2026_01_09_circular_prime](2026_01_09_circular_prime.py)*

## **_Task condition:_**

Given an integer, determine if it is a circular prime.

A circular prime is an integer where all rotations of its digits are themselves prime.

For example, `197` is a circular prime because all rotations of its digits: `197`, `971`, and `719`, are prime numbers.

### **_Examples_**

```
Input: is_circular_prime(197) => Output: True

Input: is_circular_prime(23) => Output: False

Input: is_circular_prime(13) => Output: True

Input: is_circular_prime(89) => Output: False

Input: is_circular_prime(1193) => Output: True
```

#

<br />

# 2026.01.11 Challenge - Par for the Hole

My solution -> *[2026_01_11_par_for_the_hole](2026_01_11_par_for_the_hole.py)*

## **_Task condition:_**

Given two integers, the par for a golf hole and the number of strokes a golfer took on that hole, return the golfer's score using golf terms.

Return:

- `"Hole in one!"` if it took one stroke.
- `"Eagle"` if it took two strokes less than par.
- `"Birdie"` if it took one stroke less than par.
- `"Par"` if it took the same number of strokes as par.
- `"Bogey"` if it took one stroke more than par.
- `"Double bogey"` if took two strokes more than par.

### **_Examples_**

```
Input: golf_score(3, 3) => Output: "Par"

Input: golf_score(4, 3) => Output: "Birdie"

Input: golf_score(3, 1) => Output: "Hole in one!"

Input: golf_score(5, 7) => Output: "Double bogey"

Input: golf_score(4, 5) => Output: "Bogey"

Input: golf_score(5, 3) => Output: "Eagle"
```

#

<br />

# 2026.01.12 Challenge - Plant the Crop

My solution -> *[2026_01_12_plant_the_crop](2026_01_12_plant_the_crop.py)*

## **_Task condition:_**

Given an integer representing the size of your farm field, and `"acres"` or `"hectares"` representing the unit for the size of your farm field, and a type of crop, determine how many plants of that type you can fit in your field.

- `1` acre equals `4046.86` square meters.
- `1` hectare equals `10,000` square meters.

Here's a list of crops that will be given as input and how much space a single plant takes:

| Crop                    | Space per plant      |
| :---------------------- | :------------------- |
| `"corn"`                | 1 square meter       |
| `"wheat"`               | 0.1 square meters    |
| `"soybeans"`            | 0.5 square meters    |
| `"tomatoes"`            | 0.25 square meters   |
| `"lettuce"`             | 0.2 square meters    |

Return the number of plants that fit in the field, rounded down to the nearest whole plant.

### **_Examples_**

```
Input: get_number_of_plants(1, "acres", "corn") => Output: 4046

Input: get_number_of_plants(2, "hectares", "lettuce") => Output: 100000

Input: get_number_of_plants(20, "acres", "soybeans") => Output: 161874

Input: get_number_of_plants(3.75, "hectares", "tomatoes") => Output: 150000

Input: get_number_of_plants(16.75, "acres", "tomatoes") => Output: 271139
```

#

<br />

# 2026.01.13 Challenge - Odd or Even?

My solution -> *[2026_01_13_odd_or_even](2026_01_13_odd_or_even.py)*

## **_Task condition:_**

Given a positive integer, return `"Odd"` if it's an odd number, and `"Even"` is it's even.

### **_Examples_**

```
Input: odd_or_even(1) => Output: "Odd"

Input: odd_or_even(2) => Output: "Even"

Input: odd_or_even(13) => Output: "Odd"

Input: odd_or_even(196) => Output: "Even"

Input: odd_or_even(123456789) => Output: "Odd"
```

#

<br />

# 2026.01.14 Challenge - Markdown Link Parser

My solution -> *[2026_01_14_markdown_link_parser](2026_01_14_markdown_link_parser.py)*

## **_Task condition:_**

Given the string of a link in `Markdown`, return the equivalent `HTML` string.

A Markdown image has the following format: `"[link_text](link_url)"`. Return the string of the HTML `a` tag with the `href` set to the `link_url` and the `link_text` as the tag content.

For example, given `"[freeCodeCamp](https://freecodecamp.org/)"` return `'<a href="https://freecodecamp.org/">freeCodeCamp</a>'`;

### **_Examples_**

```
Input: parse_link("[freeCodeCamp](https://freecodecamp.org/)")
Output: '<a href="https://freecodecamp.org/">freeCodeCamp</a>'

Input: parse_link("[Donate to our charity.](https://www.freecodecamp.org/donate/)")
Output: '<a href="https://www.freecodecamp.org/donate/">Donate to our charity.</a>'

Input: parse_link("[Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.](https://github.com/freeCodeCamp/freeCodeCamp/)")
Output: '<a href="https://github.com/freeCodeCamp/freeCodeCamp/">Contribute to our repository at https://github.com/freeCodeCamp/freeCodeCamp.</a>'
```

**_NOTES:_**

- The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included.

#

<br />

# 2026.01.15 Challenge - Array Swap

My solution -> *[2026_01_15_array_swap](2026_01_15_array_swap.py)*

## **_Task condition:_**

Given an array with two values, return an array with the values swapped.

For example, given `["A", "B"]` return `["B", "A"]`.

### **_Examples_**

```
Input: array_swap(["A", "B"]) => Output: ["B", "A"]

Input: array_swap([25, 20]) => Output: [20, 25]

Input: array_swap([True, False]) => Output: [False, True]

Input: array_swap(["1", 1]) => Output: [1, "1"]
```

#

<br />

# 2026.01.16 Challenge - Integer Hypotenuse

My solution -> *[2026_01_16_integer_hypotenuse](2026_01_16_integer_hypotenuse.py)*

## **_Task condition:_**

Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle, determine whether the hypotenuse is an integer.

The length of the hypotenuse is calculated by adding the squares of the two leg lengths together and then taking the square root of that total:

*a <sup>2</sup> + b <sup>2</sup> = c <sup>2</sup>*

### **_Examples_**

```
Input: is_integer_hypotenuse(3, 4) => Output: True

Input: is_integer_hypotenuse(2, 3) => Output: False

Input: is_integer_hypotenuse(5, 12) => Output: True

Input: is_integer_hypotenuse(10, 10) => Output: False

Input: is_integer_hypotenuse(780, 1040) => Output: True

Input: is_integer_hypotenuse(250, 333) => Output: False
```

#

<br />