# 2025.09.01 Challenge - Tribonacci Sequence

My solution -> *[2025_09_01_tribonacci_sequence](2025_09_01_tribonacci_sequence.py)*

## **_Task condition:_**

The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. When starting with `0`, `0` and `1`, the first 10 numbers in the sequence are `0`, `0`, `1`, `1`, `2`, `4`, `7`, `13`, `24`, `44`.

Given an array containing the first three numbers of a Tribonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

### **_Examples_**

```
Input: tribonacci_sequence([0, 0, 1], 20) => Output: [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513]

Input: tribonacci_sequence([21, 32, 43], 1) => Output: [21]

Input: tribonacci_sequence([0, 0, 1], 0) => Output: []

Input: tribonacci_sequence([10, 20, 30], 2) => Output: [10, 20]

Input: tribonacci_sequence([10, 20, 30], 3) => Output: [10, 20, 30]

Input: tribonacci_sequence([123, 456, 789], 8) => Output: [123, 456, 789, 1368, 2613, 4770, 8751, 16134]
```

**_NOTES:_**

- Your function should handle sequences of any length greater than or equal to zero.
- If the length is zero, return an empty array.
- Note that the starting numbers are part of the sequence.

#

<br />

# 2025.09.02 Challenge - RGB to Hex

My solution -> *[2025_09_02_rgb_to_hex](2025_09_02_rgb_to_hex.py)*

## **_Task condition:_**

Given a CSS `rgb(r, g, b)` color string, return its hexadecimal equivalent.

Here are some example outputs for a given input:

| Input                   | Output      |
| :---------------------- | :---------- |
| "rgb(255, 255, 255)"  | "#ffffff" |
| "rgb(1, 2, 3)"        | "#010203" |

### **_Examples_**

```
Input: rgb_to_hex("rgb(255, 255, 255)") => Output: "#ffffff"

Input: rgb_to_hex("rgb(1, 11, 111)") => Output: "#010b6f"

Input: rgb_to_hex("rgb(173, 216, 230)") => Output: "#add8e6"

Input: rgb_to_hex("rgb(79, 123, 201)") => Output: "#4f7bc9"
```

**_NOTES:_**

- Make any letters lowercase.
- Return a `#` followed by six characters. Don't use any shorthand values.

#

<br />

# 2025.09.03 Challenge - Pangram

My solution -> *[2025_09_03_pangram](2025_09_03_pangram.py)*

## **_Task condition:_**

Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.

### **_Examples_**

```
Input: is_pangram("hello", "helo") => Output: True

Input: is_pangram("hello", "hel") => Output: False

Input: is_pangram("hello", "helow") => Output: False

Input: is_pangram("hello world", "helowrd") => Output: True

Input: is_pangram("Hello World!", "helowrd") => Output: True

Input: is_pangram("Hello World!", "heliowrd") => Output: False

Input: is_pangram("freeCodeCamp", "frcdmp") => Output: False

Input: is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz") => Output: True
```

**_NOTES:_**

- Ignore non-alphabetical characters in the word or sentence.
- Ignore letter casing in the word or sentence.

#

<br />

# 2025.09.04 Challenge - Vowel Repeater

My solution -> *[2025_09_04_vowel_repeater](2025_09_04_vowel_repeater.py)*

## **_Task condition:_**

Given a string, return a new version of the string where each vowel is duplicated one more time than the previous vowel you encountered. For instance, the first vowel in the sentence should remain unchanged. The second vowel should appear twice in a row. The third vowel should appear three times in a row, and so on.

### **_Examples_**

```
Input: repeat_vowels("hello world") => Output: "helloo wooorld"

Input: repeat_vowels("freeCodeCamp") => Output: "freeeCooodeeeeCaaaaamp"

Input: repeat_vowels("AEIOU") => Output: "AEeIiiOoooUuuuu"

Input: repeat_vowels("I like eating ice cream in Iceland") => Output: "I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee creeeeeeeeeaaaaaaaaaam iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand"
```

**_NOTES:_**

- The letters `a`, `e`, `i`, `o`, and `u`, in either uppercase or lowercase, are considered vowels.
- The original vowel should keeps its case.
- Repeated vowels should be lowercase.
- All non-vowel characters should keep their original case.

#

<br />

# 2025.09.05 Challenge - IPv4 Validator

My solution -> *[2025_09_05_ipv4_validator](2025_09_05_ipv4_validator.py)*

## **_Task condition:_**

Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists of four integer numbers separated by dots (`.`). Each number must satisfy the following conditions:

- It is between `0` and `255` inclusive.
- It does not have leading zeros (e.g. `0` is allowed, `01` is not).
- Only numeric characters are allowed.

### **_Examples_**

```
Input: is_valid_ipv4("192.168.1.1") => Output: True

Input: is_valid_ipv4("0.0.0.0") => Output: True

Input: is_valid_ipv4("255.01.50.111") => Output: False

Input: is_valid_ipv4("255.00.50.111") => Output: False

Input: is_valid_ipv4("256.101.50.115") => Output: False

Input: is_valid_ipv4("192.168.101.") => Output: False

Input: is_valid_ipv4("192168145213") => Output: False
```

#

<br />

# 2025.09.06 Challenge - Matrix Rotate

My solution -> *[2025_09_06_matrix_rotate](2025_09_06_matrix_rotate.py)*

## **_Task condition:_**

Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it. For instance, given `[[1, 2], [3, 4]]`, which looks like this:

| 1 | 2 |
|---|---|
| 3 | 4 |

You should return `[[3, 1], [4, 2]]`, which looks like this:

| 3 | 1 |
|---|---|
| 4 | 2 |

### **_Examples_**

```
Input: rotate([[1]]) => Output: [[1]]

Input: rotate([[1, 2], [3, 4]]) => Output: [[3, 1], [4, 2]]

Input: rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) => Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

Input: rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]]) => Output: [[0, 1, 0], [0, 0, 1], [0, 1, 0]]
```

#

<br />

# 2025.09.07 Challenge - Roman Numeral Parser

My solution -> *[2025_09_07_roman_numeral_parser](2025_09_07_roman_numeral_parser.py)*

## **_Task condition:_**

Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:

| Symbol  | Value   |
| :-----: | :-----: |
| I       | 1       |
| V       | 5       |
| X       | 10      |
| L       | 50      |
| C       | 100     |
| D       | 500     |
| M       | 1000    |

### **_Examples_**

```
Input: parse_roman_numeral("III") => Output: 3

Input: parse_roman_numeral("IV") => Output: 4

Input: parse_roman_numeral("XXVI") => Output: 26

Input: parse_roman_numeral("XCIX") => Output: 99

Input: parse_roman_numeral("CDLX") => Output: 460

Input: parse_roman_numeral("DIV") => Output: 504

Input: parse_roman_numeral("MMXXV") => Output: 2025
```

**_NOTES:_**

- Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted. Otherwise, values are added.

#

<br />

# 2025.09.08 Challenge - Acronym Builder

My solution -> *[2025_09_08_acronym_builder](2025_09_08_acronym_builder.py)*

## **_Task condition:_**

Given a string containing one or more words, return an acronym of the words using the following constraints:

- The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
- The acronym should ignore the first letter of these words unless they are the first word of the given string: `a`, `for`, `an`, `and`, `by`, and `of`.
- The acronym letters should be returned in the order they are given.
- The acronym should not contain any spaces.

### **_Examples_**

```
Input: build_acronym("Search Engine Optimization") => Output: "SEO"

Input: build_acronym("Frequently Asked Questions") => Output: "FAQ"

Input: build_acronym("National Aeronautics and Space Administration") => Output: "NASA"

Input: build_acronym("Federal Bureau of Investigation") => Output: "FBI"

Input: build_acronym("For your information") => Output: "FYI"

Input: build_acronym("By the way") => Output: "BTW"

Input: build_acronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily") => Output: "AUHWPOTIMSH"
```

#

<br />

# 2025.09.09 Challenge - Unique Characters

My solution -> *[2025_09_09_unique_characters](2025_09_09_unique_characters.py)*

## **_Task condition:_**

Given a string, determine if all the characters in the string are unique.

### **_Examples_**

```
Input: all_unique("abc") => Output: True

Input: all_unique("aA") => Output: True

Input: all_unique("QwErTy123!@") => Output: True

Input: all_unique("~!@#$%^&*()_+") => Output: True

Input: all_unique("hello") => Output: False

Input: all_unique("freeCodeCamp") => Output: False

Input: all_unique("!@#*$%^&*()aA") => Output: False
```

**_NOTES:_**

- Uppercase and lowercase letters should be considered different characters.

#

<br />

# 2025.09.10 Challenge - Array Diff

My solution -> *[2025_09_10_array_diff](2025_09_10_array_diff.py)*

## **_Task condition:_**

Given two arrays with strings values, return a new array containing all the values that appear in only one of the arrays.

### **_Examples_**

```
Input: array_diff(["apple", "banana"], ["apple", "banana", "cherry"]) => Output: ["cherry"]

Input: array_diff(["apple", "banana", "cherry"], ["apple", "banana"]) => Output: ["cherry"]

Input: array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]) => Output: ["eight", "four", "six", "two"]

Input: array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]) => Output: ["five", "one", "seven", "three"]

Input: array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]) => Output: ["freeCodeCamp", "rocks"]
```

**_NOTES:_**

- The returned array should be sorted in alphabetical order.

#

<br />

# 2025.09.11 Challenge - Reverse Sentence

My solution -> *[2025_09_11_reverse_sentence](2025_09_11_reverse_sentence.py)*

## **_Task condition:_**

Given a string of words, return a new string with the words in reverse order. For example, the first word should be at the end of the returned string, and the last word should be at the beginning of the returned string.

### **_Examples_**

```
Input: reverse_sentence("world hello") => Output: "hello world"

Input: reverse_sentence("push commit git") => Output: "git commit push"

Input: reverse_sentence("npm  install   apt    sudo") => Output: "sudo apt install npm"

Input: reverse_sentence("import    default   function  export") => Output: "export function default import"
```

**_NOTES:_**

- In the given string, words can be separated by one or more spaces.
- The returned string should only have one space between words.

#

<br />

# 2025.09.12 Challenge - Screen Time

My solution -> *[2025_09_12_screen_time](2025_09_12_screen_time.py)*

## **_Task condition:_**

Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on your phone that day, determine if it is too much screen time based on these constraints:

- If any single day has `10` hours or more, it's too much.
- If the average of any three days in a row is greater than or equal to `8` hours, it’s too much.
- If the average of the seven days is greater than or equal to `6` hours, it's too much.

### **_Examples_**

```
Input: too_much_screen_time([1, 2, 3, 4, 5, 6, 7]) => Output: False

Input: too_much_screen_time([7, 8, 8, 4, 2, 2, 3]) => Output: False

Input: too_much_screen_time([5, 6, 6, 6, 6, 6, 6]) => Output: False

Input: too_much_screen_time([1, 2, 3, 11, 1, 3, 4]) => Output: True

Input: too_much_screen_time([1, 2, 3, 10, 2, 1, 0]) => Output: True

Input: too_much_screen_time([3, 3, 5, 8, 8, 9, 4]) => Output: True

Input: too_much_screen_time([3, 9, 4, 8, 5, 7, 6]) => Output: True
```

#

<br />

# 2025.09.13 Challenge - Missing Numbers

My solution -> *[2025_09_13_missing_numbers](2025_09_13_missing_numbers.py)*

## **_Task condition:_**

Given an array of integers from `1` to `n`, inclusive, return an array of all the missing integers between `1` and `n` (where `n` is the largest number in the given array).

### **_Examples_**

```
Input: find_missing_numbers([1, 3, 5]) => Output: [2, 4]

Input: find_missing_numbers([1, 2, 3, 4, 5]) => Output: []

Input: find_missing_numbers([1, 10]) => Output: [2, 3, 4, 5, 6, 7, 8, 9]

Input: find_missing_numbers([10, 1, 10, 1, 10, 1]) => Output: [2, 3, 4, 5, 6, 7, 8, 9]

Input: find_missing_numbers([3, 1, 4, 1, 5, 9]) => Output: [2, 6, 7, 8]

Input: find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4]) => Output: [11]
```

**_NOTES:_**

- The given array may be unsorted and may contain duplicates.
- The returned array should be in ascending order.
- If no integers are missing, return an empty array.

#

<br />

# 2025.09.14 Challenge - Word Frequency

My solution -> *[2025_09_14_word_frequency](2025_09_14_word_frequency.py)*

## **_Task condition:_**

Given a paragraph, return an array of the three most frequently occurring words.

### **_Examples_**

```
Input: get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding") => Output: ["coding", "python", "in"]

Input: get_words("I like coding. I like testing. I love debugging!") => Output: ["i", "like", "coding"]

Input: get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!") => Output: ["debug", "test", "deploy"]
```

**_NOTES:_**

- Words in the paragraph will be separated by spaces.
- Ignore case in the given paragraph. For example, treat `Hello` and `hello` as the same word.
- Ignore punctuation in the given paragraph. Punctuation consists of commas (`,`), periods (`.`), and exclamation points (`!`).
- The returned array should have all lowercase words.
- The returned array should be in descending order with the most frequently occurring word first.

#

<br />

# 2025.09.15 Challenge - Thermostat Adjuster

My solution -> *[2025_09_15_thermostat_adjuster](2025_09_15_thermostat_adjuster.py)*

## **_Task condition:_**

Given the current temperature of a room and a target temperature, return a string indicating how to adjust the room temperature based on these constraints:

- Return `"heat"` if the current temperature is below the target.
- Return `"cool"` if the current temperature is above the target.
- Return `"hold"` if the current temperature is equal to the target.

### **_Examples_**

```
Input: adjust_thermostat(68, 72) => Output: "heat"

Input: adjust_thermostat(75, 72) => Output: "cool"

Input: adjust_thermostat(72, 72) => Output: "hold"

Input: adjust_thermostat(-20.5, -10.1) => Output: "heat"

Input: adjust_thermostat(100, 99.9) => Output: "cool"

Input: adjust_thermostat(0.0, 0.0) => Output: "hold"
```

#

<br />

# 2025.09.16 Challenge - Sentence Capitalizer

My solution -> *[2025_09_16_sentence_capitalizer](2025_09_16_sentence_capitalizer.py)*

## **_Task condition:_**

Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.

- All other characters should be preserved.
- Sentences can end with a period (`.`), one or more question marks (`?`), or one or more exclamation points (`!`).

### **_Examples_**

```
Input: capitalize("this is a simple sentence.") => Output: "This is a simple sentence."

Input: capitalize("hello world. how are you?") => Output: "Hello world. How are you?"

Input: capitalize("i did today's coding challenge... it was fun!!") => Output: "I did today's coding challenge... It was fun!!"

Input: capitalize("crazy!!!strange???unconventional...sentences.") => Output: "Crazy!!!Strange???Unconventional...Sentences."

Input: capitalize("there's a space before this period . why is there a space before that period ?") => Output: "There's a space before this period . Why is there a space before that period ?"
```

#

<br />

# 2025.09.17 Challenge - Slug Generator

My solution -> *[2025_09_17_slug_generator](2025_09_17_slug_generator.py)*

## **_Task condition:_**

Given a string, return a URL-friendly version of the string using the following constraints:

- All letters should be lowercase.
- All characters that are not letters, numbers, or spaces should be removed.
- All spaces should be replaced with the URL-encoded space code `%20`.
- Consecutive spaces should be replaced with a single `%20`.
- The returned string should not have leading or trailing `%20`.

### **_Examples_**

```
Input: generate_slug("helloWorld") => Output: "helloworld"

Input: generate_slug("hello world!") => Output: "hello%20world"

Input: generate_slug(" hello-world ") => Output: "helloworld"

Input: generate_slug("hello  world") => Output: "hello%20world"

Input: generate_slug("  ?H^3-1*1]0! W[0%R#1]D  ") => Output: "h3110%20w0r1d"
```

#

<br />

# 2025.09.18 Challenge - Fill The Tank

My solution -> *[2025_09_18_fill_the_tank](2025_09_18_fill_the_tank.py)*

## **_Task condition:_**

Given the size of a fuel tank, the current fuel level, and the price per gallon, return the cost to fill the tank all the way.

- `tankSize` is the total capacity of the tank in gallons.
- `fuelLevel` is the current amount of fuel in the tank in gallons.
- `pricePerGallon` is the cost of one gallon of fuel.

### **_Examples_**

```
Input: cost_to_fill(20, 0, 4.00) => Output: "$80.00"

Input: cost_to_fill(15, 10, 3.50) => Output: "$17.50"

Input: cost_to_fill(18, 9, 3.25) => Output: "$29.25"

Input: cost_to_fill(12, 12, 4.99) => Output: "$0.00"

Input: cost_to_fill(15, 9.5, 3.98) => Output: "$21.89"
```

**_NOTES:_**

- The returned value should be rounded to two decimal places in the format: "$d.dd".

#

<br />

# 2025.09.19 Challenge - Photo Storage

My solution -> *[2025_09_19_photo_storage](2025_09_19_photo_storage.py)*

## **_Task condition:_**

Given a photo size in megabytes (`MB`), and hard drive capacity in gigabytes (`GB`), return the number of photos the hard drive can store using the following constraints:

- `1` gigabyte equals `1000` megabytes.
- Return the number of whole photos the drive can store.

### **_Examples_**

```
Input: number_of_photos(1, 1) => Output: 1000

Input: number_of_photos(2, 1) => Output: 500

Input: number_of_photos(4, 256) => Output: 64000

Input: number_of_photos(3.5, 750) => Output: 214285

Input: number_of_photos(3.5, 5.5) => Output: 1571
```

#

<br />

# 2025.09.20 Challenge - File Storage

My solution -> *[2025_09_20_file_storage](2025_09_20_file_storage.py)*

## **_Task condition:_**

Given a file size, a unit for the file size, and hard drive capacity in gigabytes (`GB`), return the number of files the hard drive can store using the following constraints:

- The unit for the file size can be bytes (`"B"`), kilobytes (`"KB"`), or megabytes (`"MB"`).
- Return the number of whole files the drive can fit.
- Use the following conversions:

| Unit          | Equivalent |
| :-----------: | :--------: |
| 1 B           | 1 B        |
| 1 KB          | 1000 B     |
| 1 MB          | 1000 KB    |
| 1 GB          | 1000 MB    |

For example, given `500`, `"KB"`, and `1` as arguments, determine how many `500 KB` files can fit on a `1 GB` hard drive.

### **_Examples_**

```
Input: number_of_files(500, "KB", 1) => Output: 2000

Input: number_of_files(50000, "B", 1) => Output: 20000

Input: number_of_files(5, "MB", 1) => Output: 200

Input: number_of_files(4096, "B", 1.5) => Output: 366210

Input: number_of_files(220.5, "KB", 100) => Output: 453514

Input: number_of_files(4.5, "MB", 750) => Output: 166666
```

#

<br />

# 2025.09.21 Challenge - Video Storage

My solution -> *[2025_09_21_video_storage](2025_09_21_video_storage.py)*

## **_Task condition:_**

Given a video size, a unit for the video size, a hard drive capacity, and a unit for the hard drive, return the number of videos the hard drive can store using the following constraints:

- The unit for the video size can be bytes (`"B"`), kilobytes (`"KB"`), megabytes (`"MB"`), or gigabytes (`"GB"`).
- If not given one of the video units above, return `"Invalid video unit"`.
- The unit of the hard drive capacity can be gigabytes (`"GB"`) or terabytes (`"TB"`).
- If not given one of the hard drive units above, return `"Invalid drive unit"`.
- Return the number of whole videos the drive can fit.
- Use the following conversions:

| Unit          | Equivalent |
| :-----------: | :--------: |
| 1 B           | 1 B        |
| 1 KB          | 1000 B     |
| 1 MB          | 1000 KB    |
| 1 GB          | 1000 MB    |
| 1 TB          | 1000 GB    |

For example, given `500`, `"MB"`, `100`, and `"GB"` as arguments, determine how many `500 MB` videos can fit on a `100 GB` hard drive.

### **_Examples_**

```
Input: number_of_videos(500, "MB", 100, "GB") => Output: 200

Input: number_of_videos(1, "TB", 10, "TB") => Output: "Invalid video unit"

Input: number_of_videos(2000, "MB", 100000, "MB") => Output: "Invalid drive unit"

Input: number_of_videos(500000, "KB", 2, "TB") => Output: 4000

Input: number_of_videos(1.5, "GB", 2.2, "TB") => Output: 1466
```

#

<br />

# 2025.09.22 Challenge - Digits vs Letters

My solution -> *[2025_09_22_digits_vs_letters](2025_09_22_digits_vs_letters.py)*

## **_Task condition:_**

Given a string, return `"digits"` if the string has more digits than letters, `"letters"` if it has more letters than digits, and `"tie"` if it has the same amount of digits and letters.

### **_Examples_**

```
Input: digits_or_letters("abc123") => Output: "tie"

Input: digits_or_letters("a1b2c3d") => Output: "letters"

Input: digits_or_letters("1a2b3c4") => Output: "digits"

Input: digits_or_letters("abc123!@#DEF") => Output: "letters"

Input: digits_or_letters("H3110 W0R1D") => Output: "digits"

Input: digits_or_letters("P455W0RD") => Output: "tie"
```

**_NOTES:_**

- Digits consist of `0-9`.
- Letters consist of `a-z` in upper or lower case.
- Ignore any other characters.

#

<br />

# 2025.09.23 Challenge - String Mirror

My solution -> *[2025_09_23_string_mirror](2025_09_23_string_mirror.py)*

## **_Task condition:_**

Given two strings, determine if the second string is a mirror of the first.

### **_Examples_**

```
Input: is_mirror("helloworld", "helloworld") => Output: False

Input: is_mirror("Hello World", "dlroW olleH") => Output: True

Input: is_mirror("RaceCar", "raCecaR") => Output: True

Input: is_mirror("RaceCar", "RaceCar") => Output: False

Input: is_mirror("Mirror", "rorrim") => Output: False

Input: is_mirror("Hello World", "dlroW-olleH") => Output: True

Input: is_mirror("Hello World", "!dlroW !olleH") => Output: True
```

**_NOTES:_**

- A string is considered a mirror if it contains the same letters in reverse order.
- Treat uppercase and lowercase letters as distinct.
- Ignore all non-alphabetical characters.

#

<br />

# 2025.09.24 Challenge - Perfect Square

My solution -> *[2025_09_24_perfect_square](2025_09_24_perfect_square.py)*

## **_Task condition:_**

Given an integer, determine if it is a perfect square.

### **_Examples_**

```
Input: is_perfect_square(9) => Output: True

Input: is_perfect_square(49) => Output: True

Input: is_perfect_square(1) => Output: True

Input: is_perfect_square(2) => Output: False

Input: is_perfect_square(99) => Output: False

Input: is_perfect_square(-9) => Output: False

Input: is_perfect_square(0) => Output: True

Input: is_perfect_square(25281) => Output: True
```

**_NOTES:_**

- A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, `9` is a perfect square because you can multiply `3` by itself to get it.

#

<br />

# 2025.09.25 Challenge - 2nd Largest

My solution -> *[2025_09_25_2nd_largest](2025_09_25_2nd_largest.py)*

## **_Task condition:_**

Given an array, return the second largest distinct number.

### **_Examples_**

```
Input: second_largest([1, 2, 3, 4]) => Output: 3

Input: second_largest([20, 139, 94, 67, 31]) => Output: 94

Input: second_largest([2, 3, 4, 6, 6]) => Output: 4

Input: second_largest([10, -17, 55.5, 44, 91, 0]) => Output: 55.5

Input: second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]) => Output: 0
```

#

<br />