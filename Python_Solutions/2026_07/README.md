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