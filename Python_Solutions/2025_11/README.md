# 2025.11.01 Challenge - Signature Validation

My solution -> *[2025_11_01_signature_validation](2025_11_01_signature_validation.py)*

## **_Task condition:_**

Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

- Letters in the message and secret key have these values:
  - `a` to `z` have values `1` to `26` respectively.
  - `A` to `Z` have values `27` to `52` respectively.
- All other characters have no value.
- Compute the signature by taking the sum of the message plus the sum of the secret key.

For example, given the message `"foo"` and the secret key `"bar"`, the signature would be `57`:

```
f (6) + o (15) + o (15) = 36
b (2) + a (1) + r (18) = 21
36 + 21 = 57
```

Check if the computed signature matches the provided signature.

### **_Examples_**

```
Input: verify("foo", "bar", 57) => Output: True

Input: verify("foo", "bar", 54) => Output: False

Input: verify("freeCodeCamp", "Rocks", 238) => Output: True

Input: verify("Is this valid?", "No", 210) => Output: False

Input: verify("Is this valid?", "Yes", 233) => Output: True

Input: verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514) => Output: True
```

#

<br />

# 2025.11.02 Challenge - Infected

My solution -> *[2025_11_02_infected](2025_11_02_infected.py)*

## **_Task condition:_**

On November 2nd, 1988, the first major internet worm was released, infecting about 10% of computers connected to the internet after only a day.

In this challenge, you are given a number of days that have passed since an internet worm was released, and you need to determine how many computers are infected using the following rules:

- On day `0`, the first computer is infected.
- Each subsequent day, the number of infected computers doubles.
- Every `3rd` day, a patch is applied after the virus spreads and reduces the number of infected computers by `20%`. Round the number of patched computers up to the nearest whole number.

For example, on:

- Day 0: 1 total computer is infected.
- Day 1: 2 total computers are infected.
- Day 2: 4 total computers are infected.
- Day 3: 8 total computers are infected. Then, apply the patch: 8 infected * 20% = 1.6 patched. Round 1.6 up to 2. 8 computers infected - 2 patched = 6 total computers infected after day 3.

Return the number of total infected computers after the given amount of days have passed.

### **_Examples_**

```
Input: infected(1) => Output: 2

Input: infected(3) => Output: 6

Input: infected(8) => Output: 152

Input: infected(17) => Output: 39808

Input: infected(25) => Output: 5217638
```

#

<br />

# 2025.11.03 Challenge - Word Counter

My solution -> *[2025_11_03_word_counter](2025_11_03_word_counter.py)*

## **_Task condition:_**

Given a sentence string, return the number of words that are in the sentence.

### **_Examples_**

```
Input: count_words("Hello world") => Output: 2

Input: count_words("The quick brown fox jumps over the lazy dog.") => Output: 9

Input: count_words("I like coding challenges!") => Output: 4

Input: count_words("Complete the challenge in JavaScript and Python.") => Output: 7

Input: count_words("The missing semi-colon crashed the entire internet.") => Output: 7
```

**_NOTES:_**

- Words are any sequence of non-space characters and are separated by a single space.

#

<br />

# 2025.11.04 Challenge - Image Search

My solution -> *[2025_11_04_image_search](2025_11_04_image_search.py)*

## **_Task condition:_**

On November 4th, 2001, Google launched its image search, allowing people to find images using search terms. In this challenge, you will imitate the image search.

Given an array of image names and a search term, return an array of image names containing the search term.

### **_Examples_**

```
Input: image_search(["dog.png", "cat.jpg", "parrot.jpeg"], "dog") => Output: ["dog.png"]

Input: image_search(["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun") => Output: ["Sunset.jpg", "sunflower.jpeg"]

Input: image_search(["Moon.png", "sun.jpeg", "stars.png"], "PNG") => Output: ["Moon.png", "stars.png"]

Input: image_search(["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat") => Output: ["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"]
```

**_NOTES:_**

- Ignore the case when matching the search terms.
- Return the images in the same order they appear in the input array.

#

<br />

# 2025.11.05 Challenge - Matrix Builder

My solution -> *[2025_11_05_matrix_builder](2025_11_05_matrix_builder.py)*

## **_Task condition:_**

Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros (`0`) of the given size.

For example, given `2` and `3`, return:

```
[
  [0, 0, 0],
  [0, 0, 0]
]
```

### **_Examples_**

```
Input: build_matrix(2, 3) => Output: [[0, 0, 0], [0, 0, 0]]

Input: build_matrix(3, 2) => Output: [[0, 0], [0, 0], [0, 0]]

Input: build_matrix(4, 3) => Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

Input: build_matrix(9, 1) => Output: [[0], [0], [0], [0], [0], [0], [0], [0], [0]]
```

#

<br />

# 2025.11.06 Challenge - Weekday Finder

My solution -> *[2025_11_06_weekday_finder](2025_11_06_weekday_finder.py)*

## **_Task condition:_**

Given a string date in the format `YYYY-MM-DD`, return the day of the week.

Valid return days are:

- `"Sunday"`
- `"Monday"`
- `"Tuesday"`
- `"Wednesday"`
- `"Thursday"`
- `"Friday"`
- `"Saturday"`

Be sure to ignore time zones.

### **_Examples_**

```
Input: get_weekday("2025-11-06") => Output: "Thursday"

Input: get_weekday("1999-12-31") => Output: "Friday"

Input: get_weekday("1111-11-11") => Output: "Saturday"

Input: get_weekday("2112-12-21") => Output: "Wednesday"

Input: get_weekday("2345-10-01") => Output: "Monday"
```

#

<br />

# 2025.11.07 Challenge - Counting Cards

My solution -> *[2025_11_07_counting_cards](2025_11_07_counting_cards.py)*

## **_Task condition:_**

A standard deck of playing cards has `13` unique cards in each suit. Given an integer representing the number of cards to pick from the deck, return the number of unique combinations of cards you can pick.

- Order does not matter. Picking card `A` then card `B` is the same as picking card `B` then card `A`.

For example, given `52`, return `1`. There's only one combination of `52` cards to pick from a `52` card deck. And given `2`, return `1326`, There's `1326` card combinations you can end up with when picking `2` cards from the deck.

### **_Examples_**

```
Input: combinations(52) => Output: 1

Input: combinations(1) => Output: 52

Input: combinations(2) => Output: 1326

Input: combinations(5) => Output: 2598960

Input: combinations(10) => Output: 15820024220

Input: combinations(50) => Output: 1326
```

#

<br />