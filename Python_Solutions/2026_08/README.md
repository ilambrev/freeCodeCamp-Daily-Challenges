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