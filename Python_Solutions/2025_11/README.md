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

# 2025.11.08 Challenge - Character Limit

My solution -> *[2025_11_08_character_limit](2025_11_08_character_limit.py)*

## **_Task condition:_**

In this challenge, you are given a string and need to determine if it fits in a social media post. Return the following strings based on the rules given:

- `"short post"` if it fits within a `40`-character limit.
- `"long post"` if it's greater than `40` characters and fits within an `80`-character limit.
- `"invalid post"` if it's too long to fit within either limit.

### **_Examples_**

```
Input: can_post("Hello world") => Output: "short post"

Input: can_post("This is a longer message but still under eighty characters.") => Output: "long post"

Input: can_post("This message is too long to fit into either of the character limits for a social media post.") => Output: "invalid post"
```

#

<br />

# 2025.11.09 Challenge - Word Search

My solution -> *[2025_11_09_word_search](2025_11_09_word_search.py)*

## **_Task condition:_**

Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.

- The given matrix will be filled with all lowercase letters (`a-z`).
- The word to find will always be in the matrix exactly once.
- The word to find will always be in a straight line in one of these directions:
  - left to right
  - right to left
  - top to bottom
  - bottom to top

For example, given the matrix:

```
[
  ["a", "c", "t"],
  ["t", "a", "t"],
  ["c", "t", "c"]
]
```

And the word "cat", return:

```
[[0, 1], [2, 1]]
```

Where `[0, 1]` are the indices for the `"c"` (start of the word), and `[2, 1]` are the indices for the `"t"` (end of the word).

### **_Examples_**

```
Input: find_word([["a", "c", "t"], ["t", "a", "t"], ["c", "t", "c"]], "cat") => Output: [[0, 1], [2, 1]]

Input: find_word([["d", "o", "g"], ["o", "g", "d"], ["d", "g", "o"]], "dog") => Output: [[0, 0], [0, 2]]

Input: find_word([["h", "i", "s", "h"], ["i", "s", "f", "s"], ["f", "s", "i", "i"], ["s", "h", "i", "f"]], "fish") => Output: [[3, 3], [0, 3]]

Input: find_word([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox") => Output: [[1, 3], [1, 1]]
```

#

<br />

# 2025.11.10 Challenge - Extension Extractor

My solution -> *[2025_11_10_extension_extractor](2025_11_10_extension_extractor.py)*

## **_Task condition:_**

Given a string representing a filename, return the extension of the file.

- The extension is the part of the filename that comes after the last period (`.`).
- If the filename does not contain a period or ends with a period, return `"none"`.
- The extension should be returned as-is, preserving case.

### **_Examples_**

```
Input: get_extension("document.txt") => Output: "txt"

Input: get_extension("README") => Output: "none"

Input: get_extension("image.PNG") => Output: "PNG"

Input: get_extension(".gitignore") => Output: "gitignore"

Input: get_extension("archive.tar.gz") => Output: "gz"

Input: get_extension("final.draft.") => Output: "none"
```

#

<br />

# 2025.11.11 Challenge - Vowels And Consonants

My solution -> *[2025_11_11_vowels_and_consonants](2025_11_11_vowels_and_consonants.py)*

## **_Task condition:_**

Given a string, return an array with the number of vowels and number of consonants in the string.

- Vowels consist of `a`, `e`, `i`, `o`, `u` in any case.
- Consonants consist of all other letters in any case.
- Ignore any non-letter characters.

For example, given `"Hello World"`, return `[3, 7]`.

### **_Examples_**

```
Input: count("Hello World") => Output: [3, 7]

Input: count("JavaScript") => Output: [3, 7]

Input: count("Python") => Output: [1, 5]

Input: count("freeCodeCamp") => Output: [5, 7]

Input: count("Hello, World!") => Output: [3, 7]

Input: count("The quick brown fox jumps over the lazy dog.") => Output: [11, 24]
```

#

<br />

# 2025.11.12 Challenge - Email Signature Generator

My solution -> *[2025_11_12_email_signature_generator](2025_11_12_email_signature_generator.py)*

## **_Task condition:_**

Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:

- The name should appear first, preceded by a prefix that depends on the first letter of the name. For names starting with (case-insensitive):
  - `A-I`: Use `>>` as the prefix.
  - `J-R`: Use `--` as the prefix.
  - `S-Z`: Use `::` as the prefix.
- A comma and space (`, `) should follow the name.
- The title and company should follow the comma and space, separated by `" at "` (with spaces around it).

For example, given `"Quinn Waverly"`, `"Founder and CEO"`, and `"TechCo"` return `"--Quinn Waverly, Founder and CEO at TechCo"`.

### **_Examples_**

```
Input: generate_signature("Quinn Waverly", "Founder and CEO", "TechCo") => Output: "--Quinn Waverly, Founder and CEO at TechCo"

Input: generate_signature("Alice Reed", "Engineer", "TechCo") => Output: ">>Alice Reed, Engineer at TechCo"

Input: generate_signature("Tina Vaughn", "Developer", "example.com") => Output: "::Tina Vaughn, Developer at example.com"

Input: generate_signature("B. B.", "Product Tester", "AcmeCorp") => Output: ">>B. B., Product Tester at AcmeCorp"

Input: generate_signature("windstorm", "Cloud Architect", "Atmospheronics") => Output: "::windstorm, Cloud Architect at Atmospheronics"
```

#

<br />

# 2025.11.13 Challenge - Array Shift

My solution -> *[2025_11_13_array_shift](2025_11_13_array_shift.py)*

## **_Task condition:_**

Given an array and an integer representing how many positions to shift the array, return the shifted array.

- A positive integer shifts the array to the left.
- A negative integer shifts the array to the right.
- The shift wraps around the array.

For example, given `[1, 2, 3]` and `1`, shift the array `1` to the left, returning `[2, 3, 1]`.

### **_Examples_**

```
Input: shift_array([1, 2, 3], 1) => Output: [2, 3, 1]

Input: shift_array([1, 2, 3], -1) => Output: [3, 1, 2]

Input: shift_array(["alpha", "bravo", "charlie"], 5) => Output: ["charlie", "alpha", "bravo"]

Input: shift_array(["alpha", "bravo", "charlie"], -11) => Output: ["bravo", "charlie", "alpha"]

Input: shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15) => Output: [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
```

#

<br />

# 2025.11.14 Challenge - Is It the Weekend?

My solution -> *[2025_11_14_is_it_the_weekend](2025_11_14_is_it_the_weekend.py)*

## **_Task condition:_**

Given a date in the format `"YYYY-MM-DD"`, return the number of days left until the weekend.

- The weekend starts on `Saturday`.
- If the given date is `Saturday` or `Sunday`, return `"It's the weekend!"`.
- Otherwise, return `"X days until the weekend."`, where `X` is the number of days until `Saturday`.
- If `X` is `1`, use `"day"` (singular) instead of `"days"` (plural).
- Make sure the calculation ignores your local timezone.

### **_Examples_**

```
Input: days_until_weekend("2025-11-14") => Output: "1 day until the weekend."

Input: days_until_weekend("2025-01-01") => Output: "3 days until the weekend."

Input: days_until_weekend("2025-12-06") => Output: "It's the weekend!"

Input: days_until_weekend("2026-01-27") => Output: "4 days until the weekend."

Input: days_until_weekend("2026-09-07") => Output: "5 days until the weekend."

Input: days_until_weekend("2026-11-29") => Output: "It's the weekend!"
```

#

<br />

# 2025.11.15 Challenge - GCD

My solution -> *[2025_11_15_gcd](2025_11_15_gcd.py)*

## **_Task condition:_**

Given two positive integers, return their greatest common divisor (`GCD`).

- The `GCD` of two integers is the largest number that divides evenly into both numbers without leaving a remainder.

For example, the divisors of `4` are `1`, `2`, and `4`. The divisors of `6` are `1`, `2`, `3`, and `6`. So given `4` and `6`, return `2`, the largest number that appears in both sets of divisors.

### **_Examples_**

```
Input: gcd(4, 6) => Output: 2

Input: gcd(20, 15) => Output: 5

Input: gcd(13, 17) => Output: 1

Input: gcd(654, 456) => Output: 6

Input: gcd(3456, 4320) => Output: 864
```

#

<br />

# 2025.11.16 Challenge - Rectangle Count

My solution -> *[2025_11_16_rectangle_count](2025_11_16_rectangle_count.py)*

## **_Task condition:_**

Given two positive integers representing the width and height of a rectangle, determine how many rectangles can fit in the given one.

- Only count rectangles with integer width and height.

For example, given `1` and `3`, return `6`. Three `1x1` rectangles, two `1x2` rectangles, and one `1x3` rectangle.

### **_Examples_**

```
Input: count_rectangles(1, 3) => Output: 6

Input: count_rectangles(3, 2) => Output: 18

Input: count_rectangles(1, 2) => Output: 3

Input: count_rectangles(5, 4) => Output: 150

Input: count_rectangles(11, 19) => Output: 12540
```

#

<br />

# 2025.11.17 Challenge - Fingerprint Test

My solution -> *[2025_11_17_fingerprint_test](2025_11_17_fingerprint_test.py)*

## **_Task condition:_**

Given two strings representing fingerprints, determine if they are a match using the following rules:

- Each fingerprint will consist only of lowercase letters (`a-z`).
- Two fingerprints are considered a match if:
  - They are the same length.
  - The number of differing characters does not exceed `10%` of the fingerprint length.

### **_Examples_**

```
Input: is_match("helloworld", "helloworld") => Output: True

Input: is_match("helloworld", "helloworlds") => Output: False

Input: is_match("helloworld", "jelloworld") => Output: True

Input: is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthelazydog") => Output: True

Input: is_match("theslickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazydog") => Output: True

Input: is_match("thequickbrownfoxjumpsoverthelazydog", "thequickbrownfoxjumpsoverthehazycat") => Output: False
```

#

<br />

# 2025.11.18 Challenge - 100 Characters

My solution -> *[2025_11_18_100_characters](2025_11_18_100_characters.py)*

## **_Task condition:_**

Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly `100` characters long. If your repetitions go over 100 characters, trim the extra so it's exactly `100`.

### **_Examples_**

```
Input: one_hundred("One hundred ") => Output: "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One "

Input: one_hundred("freeCodeCamp ") => Output: "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC"

Input: one_hundred("daily challenges ") => Output: "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge"

Input: one_hundred("!") => Output: "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
```

#

<br />

# 2025.11.19 Challenge - Markdown Heading Converter

My solution -> *[2025_11_19_markdown_heading_converter](2025_11_19_markdown_heading_converter.py)*

## **_Task condition:_**

Given a string representing a Markdown heading, return the equivalent HTML heading.

A valid Markdown heading must:

- Start with zero or more spaces, followed by
- `1` to `6` hash characters (`#`) in a row, then
- At least one space. And finally,
- The heading text.

The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an `h1` tag, and six hash symbols correspond to an `h6` tag.

If the given string doesn't have the exact format above, return `"Invalid format"`.

For example, given `"# My level 1 heading"`, return `"<h1>My level 1 heading</h1>"`.

### **_Examples_**

```
Input: convert("# My level 1 heading") => Output: "<h1>My level 1 heading</h1>"

Input: convert("My heading") => Output: "Invalid format"

Input: convert("##### My level 5 heading") => Output: "<h5>My level 5 heading</h5>"

Input: convert("#My heading") => Output: "Invalid format"

Input: convert("  ###  My level 3 heading") => Output: "<h3>My level 3 heading</h3>"

Input: convert("####### My level 7 heading") => Output: "Invalid format"

Input: convert("## My #2 heading") => Output: "<h2>My #2 heading</h2>"
```

**_NOTES:_**

- The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included.

#

<br />

# 2025.11.20 Challenge - Longest Word

My solution -> *[2025_11_20_longest_word](2025_11_20_longest_word.py)*

## **_Task condition:_**

Given a sentence string, return the longest word in the sentence.

- Words are separated by a single space.
- Only letters (`a-z`, case-insensitive) count toward the word's length.
- If there are multiple words with the same length, return the first one that appears.
- Return the word as it appears in the given string, with punctuation removed.

### **_Examples_**

```
Input: longest_word("The quick red fox") => Output: "quick"

Input: longest_word("Hello coding challenge.") => Output: "challenge"

Input: longest_word("Do Try This At Home.") => Output: "This"

Input: longest_word("This sentence... has commas, ellipses, and an exlamation point!") => Output: "exlamation"

Input: longest_word("A tie? No way!") => Output: "tie"

Input: longest_word("Wouldn't you like to know.") => Output: "Wouldnt"
```

#

<br />

# 2025.11.21 Challenge - LCM

My solution -> *[2025_11_21_lcm](2025_11_21_lcm.py)*

## **_Task condition:_**

Given two integers, return the least common multiple (`LCM`) of the two numbers.

The `LCM` of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given `4` and `6`, return `12` because:

- Multiples of `4` are `4`, `8`, `12` and so on.
- Multplies of `6` are `6`, `12`, `18` and so on.
- `12` is the smallest number that is a multiple of both.

### **_Examples_**

```
Input: lcm(4, 6) => Output: 12

Input: lcm(9, 6) => Output: 18

Input: lcm(10, 100) => Output: 100

Input: lcm(13, 17) => Output: 221

Input: lcm(45, 70) => Output: 630
```

#

<br />

# 2025.11.22 Challenge - Recipe Scaler

My solution -> *[2025_11_22_recipe_scaler](2025_11_22_recipe_scaler.py)*

## **_Task condition:_**

Given an array of recipe ingredients and a number to scale the recipe, return an array with the quantities scaled accordingly.

- Each item in the given array will be a string in the format: `"quantity unit ingredient"`. For example `"2 C Flour"`.
- Scale the quantity by the given number. Do not include any trailing zeros and do not convert any units.
- Return the scaled items in the same order they are given.

### **_Examples_**

```
Input: scale_recipe(["2 C Flour", "1.5 T Sugar"], 2) => Output: ["4 C Flour", "3 T Sugar"]

Input: scale_recipe(["4 T Flour", "1 C Milk", "2 T Oil"], 1.5) => Output: ["6 T Flour", "1.5 C Milk", "3 T Oil"]

Input: scale_recipe(["3 C Milk", "2 C Oats"], 0.5) => Output: ["1.5 C Milk", "1 C Oats"]

Input: scale_recipe(["2 C All-purpose Flour", "1 t Baking Soda", "1 t Salt", "1 C Butter", "0.5 C Sugar", "0.5 C Brown Sugar", "1 t Vanilla Extract", "2 C Chocolate Chips"], 2.5) => Output: ["5 C All-purpose Flour", "2.5 t Baking Soda", "2.5 t Salt", "2.5 C Butter", "1.25 C Sugar", "1.25 C Brown Sugar", "2.5 t Vanilla Extract", "5 C Chocolate Chips"]
```

#

<br />

# 2025.11.23 Challenge - Character Count

My solution -> *[2025_11_23_character_count](2025_11_23_character_count.py)*

## **_Task condition:_**

Given a sentence string, return an array with a count of each character in alphabetical order.

- Treat upper and lowercase letters as the same letter when counting.
- Ignore numbers, spaces, punctuation, etc.
- Return the count and letter in the format `"letter count"`. For instance, `"a 3"`.
- All returned letters should be lowercase.
- Do not return a count of letters that are not in the given string.

### **_Examples_**

```
Input: count_characters("hello world") => Output: ["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"]

Input: count_characters("I love coding challenges!") => Output: ["a 1", "c 2", "d 1", "e 3", "g 2", "h 1", "i 2", "l 3", "n 2", "o 2", "s 1", "v 1"]

Input: count_characters("// TODO: Complete this challenge ASAP!") => Output: ["a 3", "c 2", "d 1", "e 4", "g 1", "h 2", "i 1", "l 3", "m 1", "n 1", "o 3", "p 2", "s 2", "t 3"]
```

#

<br />

# 2025.11.24 Challenge - Message Validator

My solution -> *[2025_11_24_message_validator](2025_11_24_message_validator.py)*

## **_Task condition:_**

Given a message string and a validation string, determine if the message is valid.

- A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
- Letters are case-insensitive.
- Words in the message are separated by single spaces.

### **_Examples_**

```
Input: is_valid_message("hello world", "hw") => Output: True

Input: is_valid_message("ALL CAPITAL LETTERS", "acl") => Output: True

Input: is_valid_message("Coding challenge are boring.", "cca") => Output: False

Input: is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD") => Output: True

Input: is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT") => Output: False
```

#

<br />

# 2025.11.25 Challenge - FizzBuzz

My solution -> *[2025_11_25_fizzbuzz](2025_11_25_fizzbuzz.py)*

## **_Task condition:_**

Given an integer (`n`), return an array of integers from `1` to `n` (inclusive), replacing numbers that are multiple of:

- 3 with `"Fizz"`.
- 5 with `"Buzz"`.
- 3 and 5 with `"FizzBuzz"`.

### **_Examples_**

```
Input: fizz_buzz(2) => Output: [1, 2]

Input: fizz_buzz(4) => Output: [1, 2, "Fizz", 4]

Input: fizz_buzz(8) => Output: [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8]

Input: fizz_buzz(20) => Output: [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]

Input: fizz_buzz(50) => Output: [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]
```

#

<br />

# 2025.11.26 Challenge - BuzzFizz

My solution -> *[2025_11_26_buzzfizz](2025_11_26_buzzfizz.py)*

## **_Task condition:_**

Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is correct if:

- Numbers that are multiples of `3` are replaced with `"Fizz"`.
- Numbers that are multiples of `5` are replaced with `"Buzz"`.
- Numbers that are multiples of both `3` and `5` are replaced with `"FizzBuzz"`.
- All other numbers remain as integers in ascending order, starting from `1`.
- The array must start at `1` and have no missing or extra elements.

### **_Examples_**

```
Input: is_fizz_buzz([1, 2, "Fizz", 4]) => Output: True

Input: is_fizz_buzz([1, 2, 3, 4]) => Output: False

Input: is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]) => Output: False

Input: is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"]) => Output: False

Input: is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"]) => Output: False

Input: is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]) => Output: False

Input: is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz", 31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz", 46, 47, "Fizz", 49, "Buzz"]) => Output: True
```

#

<br />