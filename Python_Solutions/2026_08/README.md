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