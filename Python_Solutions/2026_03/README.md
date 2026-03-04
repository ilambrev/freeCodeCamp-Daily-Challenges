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

# 2026.03.03 Challenge - Perfect Cube Count

My solution -> *[2026_03_03_perfect_cube_count](2026_03_03_perfect_cube_count.py)*

## **_Task condition:_**

Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

- The lower number is not garanteed to be the first argument.
- A number is a perfect cube if there exists an integer (`n`) where `n * n * n = number`. For example, `27` is a perfect cube because `3 * 3 * 3 = 27`.

### **_Examples_**

```
Input: count_perfect_cubes(3, 30) => Output: 2

Input: count_perfect_cubes(1, 30) => Output: 3

Input: count_perfect_cubes(30, 0) => Output: 4

Input: count_perfect_cubes(-64, 64) => Output: 9

Input: count_perfect_cubes(9214, -8127) => Output: 41
```
#

<br />

# 2026.03.04 Challenge - Playing Card Values

My solution -> *[2026_03_04_playing_card_values](2026_03_04_playing_card_values.py)*

## **_Task condition:_**

Given an array of playing cards, return a new array with the numeric value of each card.

Card Values:

- An Ace (`"A"`) has a value of `1`.
- Numbered cards (`"2"` - `"10"`) have their face value: `2` - `10`, respectively.
- Face cards: Jack (`"J"`), Queen (`"Q"`), and King (`"K"`) are each worth `10`.

Suits:

- Each card has a suit: Spades (`"S"`), Clubs (`"C"`), Diamonds (`"D"`), or Hearts (`"H"`).

Card Format:

- Each card is represented as a string: `"valueSuit"`. For Example: `"AS"` is the Ace of Spades, `"10H"` is the Ten of Hearts, and `"QC"` is the Queen of Clubs.

### **_Examples_**

```
Input: card_values(["3H", "4D", "5S"]) => Output: [3, 4, 5]

Input: card_values(["AS", "10S", "10H", "6D", "7D"]) => Output: [1, 10, 10, 6, 7]

Input: card_values(["8D", "QS", "2H", "JC", "9C"]) => Output: [8, 10, 2, 10, 9]

Input: card_values(["AS", "KS"]) => Output: [1, 10]

Input: card_values(["10H", "JH", "QH", "KH", "AH"]) => Output: [10, 10, 10, 10, 1]
```
#

<br />