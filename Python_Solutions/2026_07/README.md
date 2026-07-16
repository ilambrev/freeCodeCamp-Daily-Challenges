# 2026.07.01 Challenge - Lucky Number

My solution -> *[2026_07_01_lucky_number](2026_07_01_lucky_number.py)*

## **_Task condition:_**

Given a string of a person's first and last name, calculate their lucky number using the following rules:

- First and last names are separated by a space
- Find the vowel and consonant count for each name
- Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
- Do the same for the two larger counts and the larger name
- Subtract the smaller value from the larger one to get their lucky number

If the final value is zero (`0`), return `13`.

### **_Examples_**

```
Input: get_lucky_number("John Doe") => Output: 21

Input: get_lucky_number("Olivia Lewis") => Output: 52

Input: get_lucky_number("James Wilson") => Output: 18

Input: get_lucky_number("Elizabeth Hernandez") => Output: 81

Input: get_lucky_number("Mike Walker") => Output: 32

Input: get_lucky_number("Chloe Perez") => Output: 13
```
#

<br />

# 2026.07.02 Challenge - Max Profit

My solution -> *[2026_07_02_max_profit](2026_07_02_max_profit.py)*

## **_Task condition:_**

Given an array of daily stock prices and a budget (in dollars), calculate the maximum profit you could make by buying and selling the stock over the given period.

- You may only sell after you buy.
- You can only buy whole shares.
- Return the maximum possible profit as a string, rounded down to the nearest cent and formatted to two decimal places.

### **_Examples_**

```
Input: get_max_profit([5, 6], 50) => Output: "10.00"

Input: get_max_profit([8, 2, 5, 10], 20) => Output: "80.00"

Input: get_max_profit([4, 5, 3, 6], 20) => Output: "18.00"

Input: get_max_profit([54.40, 51.22, 53.99, 50.28, 53.01, 52.84], 200) => Output: "8.31"

Input: get_max_profit([15.38, 15.01, 14.99, 14.62, 14.28], 80) => Output: "0.00"

Input: get_max_profit([121.45, 126.82, 122.91, 124.65, 128.83, 128.83, 127.33], 1230.25) => Output: "73.80"
```
#

<br />

# 2026.07.03 Challenge - Database Migration

My solution -> *[2026_07_03_database_migration](2026_07_03_database_migration.py)*

## **_Task condition:_**

Given two database objects, return the second object with any missing properties from the first filled in.

- Fields that already exist in the record should not be overwritten.

### **_Examples_**

```
Input: migrate_record({ "username": "", "posts": 0 }, { "verified": True }) => Output: { "username": "", "posts": 0, "verified": True }

Input: migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "posts": 5 }) => Output: { "username": "camper", "posts": 5 }

Input: migrate_record({ "username": "", "posts": 0, "verified": False }, { "username": "camper" }) => Output: { "username": "camper", "posts": 0, "verified": False }

Input: migrate_record({ "username": "", "posts": 0 }, { "username": "camper", "role": "admin" }) => Output: { "username": "camper", "role": "admin", "posts": 0 }

Input: migrate_record({ "username": "", "email": "", "posts": 0, "verified": False, "role": "user", "banned": False }, { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin" }) => Output: { "username": "camper", "email": "camper@freecodecamp.org", "role": "admin", "posts": 0, "verified": False, "banned": False }
```
#

<br />

# 2026.07.04 Challenge - Kaprekar's Routine

My solution -> *[2026_07_04_kaprekars_routine](2026_07_04_kaprekars_routine.py)*

## **_Task condition:_**

Given a `4-digit` number, return the number of times you need to apply Kaprekar's routine until reaching `6174`.

Kaprekar's routine works as follows:

- Arrange the digits in descending order to form the largest number
- Arrange the digits in ascending order to form the smallest number (pad with leading zeros if necessary)
- Subtract the smaller from the larger
- Repeat with the new number

### **_Examples_**

```
Input: kaprekar(1234) => Output: 3

Input: kaprekar(2025) => Output: 6

Input: kaprekar(7173) => Output: 4

Input: kaprekar(3164) => Output: 7

Input: kaprekar(8082) => Output: 2
```
#

<br />

# 2026.07.06 Challenge - lowercase words

My solution -> *[2026_07_06_lowercase_words](2026_07_06_lowercase_words.py)*

## **_Task condition:_**

Given a string, return only the words that are entirely lowercase, in their original order and with a space between each word.

### **_Examples_**

```
Input: get_lowercase_words("hello GOOD world") => Output: "hello world"

Input: get_lowercase_words("these are all lowercase") => Output: "these are all lowercase"

Input: get_lowercase_words("less is NoT more") => Output: "less is more"

Input: get_lowercase_words("DonT eat pizza every OTHER day") => Output: "eat pizza every day"

Input: get_lowercase_words("the Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the lazy SloW dog") => Output: "the quick brown fox jumped over the lazy dog"
```
#

<br />

# 2026.07.07 Challenge - Nearest Multiple

My solution -> *[2026_07_07_nearest_multiple](2026_07_07_nearest_multiple.py)*

## **_Task condition:_**

Given two integers, round the first to the nearest multiple of the second.

### **_Examples_**

```
Input: round_to_nearest_multiple(5, 3) => Output: 6

Input: round_to_nearest_multiple(17, 4) => Output: 16

Input: round_to_nearest_multiple(43, 5) => Output: 45

Input: round_to_nearest_multiple(38, 11) => Output: 33

Input: round_to_nearest_multiple(93, 12) => Output: 96
```
#

<br />

# 2026.07.08 Challenge - Issue Triage

My solution -> *[2026_07_08_issue_triage](2026_07_08_issue_triage.py)*

## **_Task condition:_**

Given a number of milliseconds since the last post on an issue, and the last message posted on the issue, determine what you should do with the issue according to these rules:

- If the last message is `less than 7 days` ago, return `"leave it"`
- If the last message is `7 or more days` ago and its content contains `"bump"` (case-insensitive), return `"close it"`
- Otherwise, return `"bump it"`

### **_Examples_**

```
Input: triage_issue(86400000, "Lets fix it") => Output: "leave it"

Input: triage_issue(1209600000, "still waiting") => Output: "bump it"

Input: triage_issue(864000000, "bump") => Output: "close it"

Input: triage_issue(604800000, "Do we still want this?") => Output: "bump it"

Input: triage_issue(604800000, "Bumping this") => Output: "close it"

Input: triage_issue(345600000, "I'll make a PR") => Output: "leave it"
```
#

<br />

# 2026.07.09 Challenge - Issue Triage 2

My solution -> *[2026_07_09_issue_triage_2](2026_07_09_issue_triage_2.py)*

## **_Task condition:_**

Given an issue title and an array of current labels, return an updated array of labels based on the following rules:

If the issue doesn't have any labels, add:

- `"bug"` and `"needs triage"` if the title contains `"error"` or `"bug"`
- `"enhancement"` and `"discussing"` if the title contains `"feature"` or `"add"`

Otherwise, if the given labels contain:

- `"needs triage"` and the title contains `"simple"` or `"easy"`, remove `"needs triage"` and add `"good first issue"`
- `"discussing"` and the title contains `"planned"` or `"next"`, remove `"discussing"` and add `"on the roadmap"`
- Otherwise, if `"needs triage"` or `"discussing"` is present, remove it and add `"help wanted"`

If the title contains:

- `"security"`, add a `"critical"` label

### **_Examples_**

```
Input: triage_issue("app crashes with error", []) => Output: ["bug", "needs triage"]

Input: triage_issue("app crashes with error", ["bug", "needs triage"]) => Output: ["bug", "help wanted"]

Input: triage_issue("add dark mode", []) => Output: ["enhancement", "discussing"]

Input: triage_issue("add dark mode", ["enhancement", "discussing"]) => Output: ["enhancement", "help wanted"]

Input: triage_issue("xss security bug", []) => Output: ["bug", "needs triage", "critical"]

Input: triage_issue("security vulnerability in auth", []) => Output: ["critical"]

Input: triage_issue("easy a11y fix", ["bug", "needs triage"]) => Output: ["bug", "good first issue"]

Input: triage_issue("planned api migration", ["enhancement", "discussing"]) => Output: ["enhancement", "on the roadmap"]

Input: triage_issue("improve security", ["enhancement", "discussing"]) => Output: ["enhancement", "help wanted", "critical"]
```
#

<br />

# 2026.07.12 Challenge - Horoscope Match

My solution -> *[2026_07_12_horoscope_match](2026_07_12_horoscope_match.py)*

## **_Task condition:_**

Given two star sign strings, return their compatibility percentage.

The signs are arranged in a wheel of `12` positions in this order: `"Aries"`, `"Taurus"`, `"Gemini"`, `"Cancer"`, `"Leo"`, `"Virgo"`, `"Libra"`, `"Scorpio"`, `"Sagittarius"`, `"Capricorn"`, `"Aquarius"`, `"Pisces"`, wrapping back to `"Aries"` after `"Pisces"`. Find the shortest distance between the two signs and return the compatibility:

| Distance | Compatibility |
| :------: | :-----------: |
| 0        | `"100%"`      |
| 1        | `"40%"`       |
| 2        | `"80%"`       |
| 3        | `"30%"`       |
| 4        | `"90%"`       |
| 5        | `"20%"`       |
| 6        | `"50%"`       |

### **_Examples_**

```
Input: horoscope_match("Libra", "Sagittarius") => Output: "80%"

Input: horoscope_match("Gemini", "Scorpio") => Output: "20%"

Input: horoscope_match("Pisces", "Aries") => Output: "40%"

Input: horoscope_match("Capricorn", "Cancer") => Output: "50%"

Input: horoscope_match("Aquarius", "Aquarius") => Output: "100%"

Input: horoscope_match("Virgo", "Taurus") => Output: "90%"

Input: horoscope_match("Leo", "Scorpio") => Output: "30%"
```
#

<br />

# 2026.07.13 Challenge - Tally Counter

My solution -> *[2026_07_13_tally_counter](2026_07_13_tally_counter.py)*

## **_Task condition:_**

Given a string of tally marks, return the total count represented.

- Each pipe `"|"` represents one count.
- Every fifth mark is represented as a forward slash `"/"`, completing a group of five (`"||||/"`).
- Groups are separated by a space.

### **_Examples_**

```
Input: get_tally_count("||||") => Output: 4

Input: get_tally_count("||||/") => Output: 5

Input: get_tally_count("||||/ |||") => Output: 8

Input: get_tally_count("||||/ ||||/ ||||/ ||") => Output: 17

Input: get_tally_count("||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |") => Output: 41
```
#

<br />

# 2026.07.14 Challenge - Pet Age Calculator

My solution -> *[2026_07_14_pet_age_calculator](2026_07_14_pet_age_calculator.py)*

## **_Task condition:_**

Given a pet type and age in human years, return the equivalent age in pet years using the following conversion table:

| Pet           | Multiplier |
| :-----------: | :--------: |
| `"dog"`       | 7          |
|`"cat"`        | 6          |
|`"rabbit"`     | 8          |
|`"hamster"`    | 30         |
|`"guinea pig"` | 12         |
|`"goldfish"`   | 6          |
|`"bird"`       | 5          |

### **_Examples_**

```
Input: pet_years("dog", 5) => Output: 35

Input: pet_years("cat", 9) => Output: 54

Input: pet_years("rabbit", 3) => Output: 24

Input: pet_years("hamster", 4) => Output: 120

Input: pet_years("guinea pig", 5) => Output: 60

Input: pet_years("goldfish", 2) => Output: 12

Input: pet_years("bird", 1) => Output: 5
```
#

<br />

# 2026.07.15 Challenge - Array Chunks

My solution -> *[2026_07_15_array_chunks](2026_07_15_array_chunks.py)*

## **_Task condition:_**

Given an array and a chunk size, return the array split into sub-arrays of that size.

- The last chunk may be smaller if the array doesn't divide evenly.

### **_Examples_**

```
Input: chunk_array([1, 2, 3, 4, 5, 6], 3) => Output: [[1, 2, 3], [4, 5, 6]]

Input: chunk_array([1, "two", 3, "four", 5, "six", 7, "eight"], 2) => Output: [[1, "two"], [3, "four"], [5, "six"], [7, "eight"]]

Input: chunk_array([1, 2, 3, 4, 5], 3) => Output: [[1, 2, 3], [4, 5]]

Input: chunk_array(["a", "b", "c", "d", "e"], 1) => Output: [["a"], ["b"], ["c"], ["d"], ["e"]]

Input: chunk_array([1, 2, 3], 5) => Output: [[1, 2, 3]]
```
#

<br />

# 2026.07.16 Challenge - Pig Latin Converter

My solution -> *[2026_07_16_pig_latin_converter](2026_07_16_pig_latin_converter.py)*

## **_Task condition:_**

Given a string, convert it to Pig Latin using the following rules:

- If a word begins with a vowel (`"a"`, `"e"`, `"i"`, `"o"`, or `"u"`), add `"way"` to the end. For example, `"universe"` converts to `"universeway"`.
- If a word begins with one or more consonants, move them to the end and add `"ay"`. For example, `"hello"` converts to `"ellohay"`.
- Preserve the case of the first letter. For example, `"Hello"` converts to `"Ellohay"`.

### **_Examples_**

```
Input: pig_latin("universe") => Output: "universeway"

Input: pig_latin("hello") => Output: "ellohay"

Input: pig_latin("hello universe") => Output: "ellohay universeway"

Input: pig_latin("Hello universe") => Output: "Ellohay universeway"

Input: pig_latin("Pig Latin is fun") => Output: "Igpay Atinlay isway unfay"

Input: pig_latin("The quick brown fox jumped over the lazy dog") => Output: "Ethay uickqay ownbray oxfay umpedjay overway ethay azylay ogday"
```
#

<br />