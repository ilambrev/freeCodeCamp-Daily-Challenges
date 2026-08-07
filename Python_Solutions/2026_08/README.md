# 2026.08.01 Challenge - Magic Square Solver

My solution -> *[2026_08_01_magic_square_solver](2026_08_01_magic_square_solver.py)*

## **_Task condition:_**

Given a `3x3` grid with one missing number (represented as `0`), return the missing number that completes the magic square, or `"impossible"` if no valid number exists.

A magic square is a grid where every row, column, and diagonal adds up to the same number.

### **_Examples_**

```
Input: solve_magic_square([[2, 7, 6], [9, 0, 1], [4, 3, 8]]) => Output: 5

Input: solve_magic_square([[0, 14, 12], [18, 10, 2], [8, 6, 16]]) => Output: 4

Input: solve_magic_square([[12, 17, 16], [19, 0, 10], [14, 13, 18]]) => Output: "impossible"

Input: solve_magic_square([[15, 35, 31], [43, 27, 11], [23, 19, 0]]) => Output: 39

Input: solve_magic_square([[26, 41, 14], [47, 35, 0], [32, 29, 44]]) => Output: "impossible"
```
#

<br />

# 2026.08.02 Challenge - Food Chain

My solution -> *[2026_08_02_food_chain](2026_08_02_food_chain.py)*

## **_Task condition:_**

Given an array of `[predator, prey]` pairs, return the food chain from the apex predator down to the bottom.

- The apex predator is the animal that is never prey to another animal.
- Return the chain as an array of strings.

### **_Examples_**

```
Input: get_food_chain([["cat", "mouse"]]) => Output: ["cat", "mouse"]

Input: get_food_chain([["wolf", "deer"], ["deer", "grass"]]) => Output: ["wolf", "deer", "grass"]

Input: get_food_chain([["hawk", "snake"], ["snake", "frog"], ["frog", "fly"]]) => Output: ["hawk", "snake", "frog", "fly"]

Input: get_food_chain([["rabbit", "grass"], ["fox", "rabbit"], ["eagle", "fox"]]) => Output: ["eagle", "fox", "rabbit", "grass"]

Input: get_food_chain([["seal", "salmon"], ["herring", "shrimp"], ["orca", "seal"], ["shrimp", "plankton"], ["salmon", "herring"]]) => Output: ["orca", "seal", "salmon", "herring", "shrimp", "plankton"]
```
#

<br />

# 2026.08.03 Challenge - Emoji Translator

My solution -> *[2026_08_03_emoji_translator](2026_08_03_emoji_translator.py)*

## **_Task condition:_**

Given a string of emojis, return the phrase using the following table:

|Emoji | Word      |
| :--: | :-------: |
| 👶   | `"baby"`  |
| 🐱   | `"cat"`   |
| 🐕   | `"dog"`   |
| 🐟   | `"fish"`  |
| 🥵   | `"hot"`   |
| 🧊   | `"ice"`   |
| 🪨   | `"rock"`  |
| 🦈   | `"shark"` |
| 🍲   | `"soup"`  |
| ⭐   | `"star"`  |

Return the words separated by spaces.

### **_Examples_**

```
Input: get_emoji_phrase("🪨⭐") => Output: "rock star"

Input: get_emoji_phrase("🥵🐕") => Output: "hot dog"

Input: get_emoji_phrase("👶🦈") => Output: "baby shark"

Input: get_emoji_phrase("⭐🐟") => Output: "star fish"

Input: get_emoji_phrase("🧊🧊👶") => Output: "ice ice baby"

Input: get_emoji_phrase("🐱🐟🍲") => Output: "cat fish soup"
```
#

<br />

# 2026.08.04 Challenge - Golf Handicap Calculator

My solution -> *[2026_08_04_golf_handicap_calculator](2026_08_04_golf_handicap_calculator.py)*

## **_Task condition:_**

Given an array of golf scores and a corresponding array of course par values, return the golfer's handicap index using the following method:

- Calculate the differential for each round by subtracting the par from the score, then return the average of all differentials rounded to one decimal place.

### **_Examples_**

```
Input: calculate_handicap([72, 72, 72], [72, 72, 72]) => Output: 0

Input: calculate_handicap([80, 76, 78, 78], [72, 72, 72, 72]) => Output: 6

Input: calculate_handicap([42, 45, 46, 44], [36, 36, 36, 36]) => Output: 8.3

Input: calculate_handicap([85, 80, 76, 79, 82], [72, 72, 72, 71, 71]) => Output: 8.8

Input: calculate_handicap([41, 50, 48, 52, 46, 49], [35, 37, 35, 37, 35, 37]) => Output: 11.7
```
#

<br />

# 2026.08.05 Challenge - Spoken Duration

My solution -> *[2026_08_05_spoken_duration](2026_08_05_spoken_duration.py)*

## **_Task condition:_**

Given a number of seconds, return the duration in spoken English.

- Break the duration into hours, minutes, and seconds.
- Skip any zero values.
- Use singular or plural as appropriate (`"1 hour"`, `"2 hours"`).
- If present, join the last two units with `"and"`, and the second and third to last units with a comma (`"1 hour, 2 minutes and 3 seconds"`).

### **_Examples_**

```
Input: get_spoken_duration(3723) => Output: "1 hour, 2 minutes and 3 seconds"

Input: get_spoken_duration(7295) => Output: "2 hours, 1 minute and 35 seconds"

Input: get_spoken_duration(8521) => Output: "2 hours, 22 minutes and 1 second"

Input: get_spoken_duration(435) => Output: "7 minutes and 15 seconds"

Input: get_spoken_duration(14455) => Output: "4 hours and 55 seconds"

Input: get_spoken_duration(72000) => Output: "20 hours"

Input: get_spoken_duration(1) => Output: "1 second"
```
#

<br />

# 2026.08.06 Challenge - Spoken Time

My solution -> *[2026_08_06_spoken_time](2026_08_06_spoken_time.py)*

## **_Task condition:_**

Given the angles for the hour and minute hands of an analog clock in degrees (`clockwise from 12`), return the time in spoken English.

Convert the minute hand angle to minutes (`360° = 60 minutes`), then use the following rules:

| Minutes              | Spoken                                     |
| :------------------: | :----------------------------------------: |
| 0                    | "Y o'clock"                                |
| 15                   | "quarter past Y"                           |
| 1–29 (excluding 15)  | "X minutes past Y"                         |
| 30                   | "half past Y"                              |
| 45                   | "quarter to Z"                             |
| 31–59 (excluding 45) | "X minutes to Z" (where X is 60 - minutes) |

Where `Y` is the current hour and `Z` is the next hour, both derived from the hour hand angle (`360° = 12 hours`).

### **_Examples_**

```
Input: get_spoken_time(90, 0) => Output: "3 o'clock"

Input: get_spoken_time(160, 120) => Output: "20 minutes past 5"

Input: get_spoken_time(255, 180) => Output: "half past 8"

Input: get_spoken_time(67.5, 92) => Output: "quarter past 2"

Input: get_spoken_time(200, 240) => Output: "20 minutes to 7"

Input: get_spoken_time(322.5, 273) => Output: "quarter to 11"

Input: get_spoken_time(117.5, 335) => Output: "5 minutes to 4"
```

**_NOTES:_**

- Hand angles may not land exactly on a number, consider rounding them somehow.

#

<br />