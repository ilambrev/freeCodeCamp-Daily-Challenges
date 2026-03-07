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

# 2026.03.05 Challenge - Smallest Gap

My solution -> *[2026_03_05_smallest_gap](2026_03_05_smallest_gap.py)*

## **_Task condition:_**

Given a string, return the substring between the two identical characters that have the smallest number of characters between them (`smallest gap`).

- There will always be at least one pair of matching characters.
- The returned substring should exclude the matching characters.
- If two or more gaps are the same length, return the characters from the first one.

For example, given `"ABCDAC"`, return `"DA"`.

- Only `"A"` and `"C"` repeat in the string.
- The number of characters between the two `"A"` characters is `3`, and between the `"C"` characters is `2`.
- So return the string between the two `"C"` characters.

### **_Examples_**

```
Input: smallest_gap("ABCDAC") => Output: "DA"

Input: smallest_gap("racecar") => Output: "e"

Input: smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4") => Output: "#q6e&rkf(p"

Input: smallest_gap("Hello World") => Output: ""

Input: smallest_gap("The quick brown fox jumps over the lazy dog.") => Output: "fox"
```
#

<br />

# 2026.03.06 Challenge - Trail Traversal

My solution -> *[2026_03_06_trail_traversal](2026_03_06_trail_traversal.py)*

## **_Task condition:_**

Given an array of strings representing your trail map, return a string of the moves needed to get to your goal.

The given strings will contain the values:

- `"C"`: Your current location
- `"G"`: Your goal
- `"T"`: Traversable parts of the trail
- `"-"`: Untraversable parts of the map

Return a string with the moves needed to follow the trail from your location to your goal where:

- `"R"` is a move right
- `"D"` is a move down
- `"L"` is a move left
- `"U"` is a move up
- There will always be a single continuous trail, without any branching, from your current location to your goal.
- Each trail location will have a maximum of two traversable locations touching it.

For example, given:

```
[
  "-CT--",
  "--T--",
  "--TT-",
  "---T-",
  "---G-"
]
```

Return `"RDDRDD"`.

### **_Examples_**

```
Input: navigate_trail(["-CT--", "--T--", "--TT-", "---T-", "---G-"]) => Output: "RDDRDD"

Input: navigate_trail(["-----", "--TTG", "--T--", "--T--", "CTT--"]) => Output: "RRUUURR"

Input: navigate_trail(["-C----", "TT----", "T-----", "TTTTT-", "----G-"]) => Output: "DLDDRRRRD"

Input: navigate_trail(["--------", "-CTTT---", "----T---", "---GT---", "--------"]) => Output: "RRRDDL"

Input: navigate_trail(["TTTTTTT-", "T-----T-", "T-----T-", "TTTT--TG", "---C----"]) => Output: "ULLLUUURRRRRRDDDR"
```
#

<br />

# 2026.03.07 Challenge - Element Size

My solution -> *[2026_03_07_element_size](2026_03_07_element_size.py)*

## **_Task condition:_**

Given a window size, the width of an element in viewport width `"vw"` units, and the height of an element in viewport height `"vh"` units, determine the size of the element in pixels.

- The given window size and returned element size are strings in the format `"width x height"`, `"1200 x 800"` for example.
- `"vw"` units are the percent of window width. `"50vw"` for example, is `50%` of the width of the window.
- `"vh"` units are the percent of window height. `"50vh"` for example, is `50%` of the height of the window.

### **_Examples_**

```
Input: get_element_size("1200 x 800", "50vw", "50vh") => Output: "600 x 400"

Input: get_element_size("320 x 480", "25vw", "50vh") => Output: "80 x 240"

Input: get_element_size("1000 x 500", "7vw", "3vh") => Output: "70 x 15"

Input: get_element_size("1920 x 1080", "95vw", "100vh") => Output: "1824 x 1080"

Input: get_element_size("1200 x 800", "0vw", "0vh") => Output: "0 x 0"

Input: get_element_size("1440 x 900", "100vw", "114vh") => Output: "1440 x 1026"
```
#

<br />