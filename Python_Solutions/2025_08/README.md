# 2025.08.11 Challenge - Vowel Balance

My solution -> *[2025_08_11_vowel_balance](2025_08_11_vowel_balance.py)*

## **_Task condition:_**

Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

### **_Examples_**

```
Input: is_balanced("racecar") => Output: True

Input: is_balanced("Lorem Ipsum") => Output: True

Input: is_balanced("Kitty Ipsum") => Output: False

Input: is_balanced("string") => Output: False

Input: is_balanced(" ") => Output: True

Input: is_balanced("abcdefghijklmnopqrstuvwxyz") => Output: False

Input: is_balanced("123A#b!E&*456-o.U") => Output: True
```

**_NOTES:_**

- The string can contain any characters.
- The letters `a`, `e`, `i`, `o`, and `u`, in either uppercase or lowercase, are considered vowels.
- If there's an odd number of characters in the string, ignore the center character.

#

<br />

# 2025.08.12 Challenge - Base Check

My solution -> *[2025_08_12_base_check](2025_08_12_base_check.py)*

## **_Task condition:_**

Given a string representing a number, and an integer base from `2` to `36`, determine whether the number is valid in that base.

### **_Examples_**

```
Input: is_valid_number("10101", 2) => Output: True

Input: is_valid_number("10201", 2) => Output: False

Input: is_valid_number("76543210", 8) => Output: True

Input: is_valid_number("9876543210", 8) => Output: False

Input: is_valid_number("9876543210", 10) => Output: True

Input: is_valid_number("ABC", 10) => Output: False

Input: is_valid_number("ABC", 16) => Output: True

Input: is_valid_number("Z", 36) => Output: True

Input: is_valid_number("ABC", 20) => Output: True

Input: is_valid_number("4B4BA9", 16) => Output: True

Input: is_valid_number("5G3F8F", 16) => Output: False

Input: is_valid_number("5G3F8F", 17) => Output: True

Input: is_valid_number("abc", 10) => Output: False

Input: is_valid_number("abc", 16) => Output: True

Input: is_valid_number("AbC", 16) => Output: True

Input: is_valid_number("z", 36) => Output: True
```

**_NOTES:_**

- The string may contain integers, and uppercase or lowercase characters.
- The check should be case-insensitive.
- The base can be any number `2-36`.
- A number is valid if every character is a valid digit in the given base.
- Example of valid digits for bases:
    - **Base 2**: `0-1`
    - **Base 8**: `0-7`
    - **Base 10**: `0-9`
    - **Base 16**: `0-9 and A-F`
    - **Base 36**: `0-9 and A-Z`

#

<br />

# 2025.08.13 Challenge - Fibonacci Sequence

My solution -> *[2025_08_13_fibonacci_sequence](2025_08_13_fibonacci_sequence.py)*

## **_Task condition:_**

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. When starting with `0` and `1`, the first `10` numbers in the sequence are `0`, `1`, `1`, `2`, `3`, `5`, `8`, `13`, `21`, `34`.

Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

### **_Examples_**

```
Input: fibonacci_sequence([0, 1], 20) => Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

Input: fibonacci_sequence([21, 32], 1) => Output: [21]

Input: fibonacci_sequence([0, 1], 0) => Output: []

Input: fibonacci_sequence([10, 20], 2) => Output: [10, 20]

Input: fibonacci_sequence([123456789, 987654321], 5) => Output: [123456789, 987654321, 1111111110, 2098765431, 3209876541]
```

**_NOTES:_**

- Your function should handle sequences of any length greater than or equal to zero.
- If the length is zero, return an empty array.
- Note that the starting numbers are part of the sequence.

#

<br />

# 2025.08.14 Challenge - S  P  A  C  E  J  A  M

My solution -> *[2025_08_14_spacejam](2025_08_14_spacejam.py)*

## **_Task condition:_**

Given a string, remove all spaces from the string, insert two spaces between every character, convert all alphabetical letters to uppercase, and return the result.

### **_Examples_**

```
Input: space_jam("freeCodeCamp") => Output: "F  R  E  E  C  O  D  E  C  A  M  P"

Input: space_jam("   free   Code   Camp   ") => Output: "F  R  E  E  C  O  D  E  C  A  M  P"

Input: space_jam("Hello World?!") => Output: "H  E  L  L  O  W  O  R  L  D  ?  !"

Input: space_jam("C@t$ & D0g$") => Output: "C  @  T  $  &  D  0  G  $"

Input: space_jam("allyourbase") => Output: "A  L  L  Y  O  U  R  B  A  S  E"
```

**_NOTES:_**

- Non-alphabetical characters should remain unchanged (except for spaces).

#

<br />

# 2025.08.15 Challenge - Jbelmud Text

My solution -> *[2025_08_15_jbelmud_text](2025_08_15_jbelmud_text.py)*

## **_Task condition:_**

Given a string, return a jumbled version of that string where each word is transformed using the following constraints:

- The first and last letters of the words remain in place.
- All letters between the first and last letter are sorted alphabetically.
- The input strings will contain no punctuation, and will be entirely lowercase.

### **_Examples_**

```
Input: jbelmu("hello world") => Output: "hello wlord"

Input: jbelmu("i love jumbled text") => Output: "i love jbelmud text"

Input: jbelmu("freecodecamp is my favorite place to learn to code") => Output: "faccdeeemorp is my faiortve pacle to laern to cdoe"

Input: jbelmu("the quick brown fox jumps over the lazy dog") => Output: "the qciuk borwn fox jmpus oevr the lazy dog"
```

#

<br />

# 2025.08.16 Challenge - Anagram Checker

My solution -> *[2025_08_16_anagram_checker](2025_08_16_anagram_checker.py)*

## **_Task condition:_**

Given two strings, determine if they are anagrams of each other (contain the same characters in any order).

### **_Examples_**

```
Input: are_anagrams("listen", "silent") => Output: True

Input: are_anagrams("School master", "The classroom") => Output: True

Input: are_anagrams("A gentleman", "Elegant man") => Output: True

Input: are_anagrams("Hello", "World") => Output: False

Input: are_anagrams("apple", "banana") => Output: False

Input: are_anagrams("cat", "dog") => Output: False
```

**_NOTES:_**

- Ignore casing and white space.

#

<br />

# 2025.08.17 Challenge - Targeted Sum

My solution -> *[2025_08_17_targeted_sum](2025_08_17_targeted_sum.py)*

## **_Task condition:_**

Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. Return an array with the indices of those two numbers, or `"Target not found"` if no two numbers sum up to the target.

### **_Examples_**

```
Input: find_target([2, 7, 11, 15], 9) => Output: [0, 1]

Input: find_target([3, 2, 4, 5], 6) => Output: [1, 2]

Input: find_target([1, 3, 5, 6, 7, 8], 15) => Output: [4, 5]

Input: find_target([1, 3, 5, 7], 14) => Output: "Target not found"
```

**_NOTES:_**

- The returned array should have the indices in ascending order.

#

<br />

# 2025.08.18 Challenge - Factorializer

My solution -> *[2025_08_18_factorializer](2025_08_18_factorializer.py)*

## **_Task condition:_**

Given an integer from zero to `20`, return the factorial of that number. The factorial of a number is the product of all the numbers between `1` and the given number.

### **_Examples_**

```
Input: factorial(0) => Output: 1

Input: factorial(5) => Output: 120

Input: factorial(20) => Output: 2432902008176640000
```

**_NOTES:_**

- The factorial of zero is 1.

#

<br />

# 2025.08.19 Challenge - Sum Of Squares

My solution -> *[2025_08_19_sum_of_squares](2025_08_19_sum_of_squares.py)*

## **_Task condition:_**

Given a positive integer up to `1,000`, return the sum of all the integers squared from 1 up to the number.

### **_Examples_**

```
Input: sum_of_squares(5) => Output: 55

Input: sum_of_squares(10) => Output: 385

Input: sum_of_squares(25) => Output: 5525

Input: sum_of_squares(500) => Output: 41791750

Input: sum_of_squares(1000) => Output: 333833500
```

#

<br />

# 2025.08.20 Challenge - 3 Strikes

My solution -> *[2025_08_20_3_strikes](2025_08_20_3_strikes.py)*

## **_Task condition:_**

Given an integer between `1` and `10,000`, return a count of how many numbers from `1` up to that integer whose square contains at least one digit `3`.

### **_Examples_**

```
Input: squares_with_three(1) => Output: 0

Input: squares_with_three(10) => Output: 1

Input: squares_with_three(100) => Output: 19

Input: squares_with_three(1000) => Output: 326

Input: squares_with_three(10000) => Output: 4531
```

#

<br />

# 2025.08.21 Challenge - Mile Pace

My solution -> *[2025_08_21_mile_pace](2025_08_21_mile_pace.py)*

## **_Task condition:_**

Given a number of miles ran, and a time in `"MM:SS"` (minutes:seconds) it took to run those miles, return a string for the average time it took to run each mile in the format `"MM:SS"`.

### **_Examples_**

```
Input: mile_pace(3, "24:00") => Output: "08:00"

Input: mile_pace(1, "06:45") => Output: "06:45"

Input: mile_pace(2, "07:00") => Output: "03:30"

Input: mile_pace(26.2, "120:35") => Output: "04:36"
```

**_NOTES:_**

- Add leading zeros when needed.

#

<br />

# 2025.08.22 Challenge - Message Decoder

My solution -> *[2025_08_22_message_decoder](2025_08_22_message_decoder.py)*

## **_Task condition:_**

Given a secret message string, and an integer representing the number of letters that were used to shift the message to encode it, return the decoded string.

### **_Examples_**

```
Input: decode("Xlmw mw e wigvix qiwweki.", 4) => Output: "This is a secret message."

Input: decode("Byffi Qilfx!", 20) => Output: "Hello World!"

Input: decode("Zqd xnt njzx?", -1) => Output: "Are you okay?"

Input: decode("oannLxmnLjvy", 9) => Output: "freeCodeCamp"
```

**_NOTES:_**

- A positive number means the message was shifted forward in the alphabet.
- A negative number means the message was shifted backward in the alphabet.
- Case matters, decoded characters should retain the case of their encoded counterparts.
- Non-alphabetical characters should not get decoded.

#

<br />

# 2025.08.23 Challenge - Unnatural Prime

My solution -> *[2025_08_23_unnatural_prime](2025_08_23_unnatural_prime.py)*

## **_Task condition:_**

Given an integer, determine if that number is a prime number or a negative prime number.

### **_Examples_**

```
Input: is_unnatural_prime(1) => Output: False

Input: is_unnatural_prime(-1) => Output: False

Input: is_unnatural_prime(19) => Output: True

Input: is_unnatural_prime(-23) => Output: True

Input: is_unnatural_prime(0) => Output: False

Input: is_unnatural_prime(97) => Output: True

Input: is_unnatural_prime(-61) => Output: True

Input: is_unnatural_prime(99) => Output: False

Input: is_unnatural_prime(-44) => Output: False
```

**_NOTES:_**

- A prime number is a positive integer greater than `1` that is only divisible by `1` and `itself`.
- A negative prime number is the negative version of a positive prime number.
- `1` and `0` are not considered prime numbers.

#

<br />