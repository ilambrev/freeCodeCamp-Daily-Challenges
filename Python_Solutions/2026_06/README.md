# 2026.06.01 Challenge - Schema Validator Part 1

My solution -> *[2026_06_01_schema_validator_part_1](2026_06_01_schema_validator_part_1.py)*

## **_Task condition:_**

Given an dictionary, determine if it matches the following schema:

```
{
  username: string
}
```

- Extra keys are allowed

### **_Examples_**

```
Input: is_valid_schema({"username": "bob"}) => Output: True

Input: is_valid_schema({"username": "jen", "posts": 30}) => Output: True

Input: is_valid_schema({"username": ""}) => Output: True

Input: is_valid_schema({"username": 7}) => Output: False

Input: is_valid_schema({"posts": 25}) => Output: False
```
#

<br />

# 2026.06.02 Challenge - Schema Validator Part 2

My solution -> *[2026_06_02_schema_validator_part_2](2026_06_02_schema_validator_part_2.py)*

## **_Task condition:_**

Given an dictionary, determine if it matches the following schema:

```
{
  username: string,
  posts: number,
  verified: boolean
}
```

- Extra keys are allowed

### **_Examples_**

```
Input: is_valid_schema({"username": "alice", "posts": 10, "verified": False}) => Output: True

Input: is_valid_schema({"username": "carol", "posts": 15, "verified": True, "followers": 25}) => Output: True

Input: is_valid_schema({"username": "frank", "posts": "21", "verified": True}) => Output: False

Input: is_valid_schema({"username": "sam", "posts": 17, "verified": "false"}) => Output: False

Input: is_valid_schema({"username": "bill", "verified": True}) => Output: False

Input: is_valid_schema({"username": "fred", "verified": True}) => Output: False

Input: is_valid_schema({"username": 5, "posts": 10, "verified": True}) => Output: False
```
#

<br />

# 2026.06.03 Challenge - Schema Validator Part 3

My solution -> *[2026_06_03_schema_validator_part_3](2026_06_03_schema_validator_part_3.py)*

## **_Task condition:_**

Given an dictionary, determine if it matches the following schema:

```
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles
}
```

- The pipe (`|`) symbol means `"or"`. `role` must be one of the listed `Roles` values.
- Extra keys are allowed

### **_Examples_**

```
Input: is_valid_schema({"username": "henry", "posts": 0, "verified": True, "role": "staff"}) => Output: True

Input: is_valid_schema({"username": "sara", "posts": 45, "verified": False, "role": "creator", "followers": 70}) => Output: True

Input: is_valid_schema({"username": "penelope", "posts": 20, "verified": True, "role": "admin"}) => Output: True

Input: is_valid_schema({"username": "kevin", "posts": 0, "verified": False, "role": "user"}) => Output: True

Input: is_valid_schema({"username": "george", "posts": 15, "verified": True, "role": "moderator"}) => Output: True

Input: is_valid_schema({"username": "david", "posts": 0, "verified": False, "role": "guest"}) => Output: False

Input: is_valid_schema({"username": "wendy", "posts": 10, "verified": True}) => Output: False

Input: is_valid_schema({"username": "fabian", "posts": 1, "verified": True, "role": True}) => Output: False

Input: is_valid_schema({"username": 8, "posts": 1, "verified": True, "role": "user"}) => Output: False

Input: is_valid_schema({"username": "penny", "posts": "10", "verified": True, "role": "staff"}) => Output: False

Input: is_valid_schema({"username": "john", "posts": "1", "verified": "true", "role": "admin"}) => Output: False
```
#

<br />

# 2026.06.04 Challenge - Schema Validator Part 4

My solution -> *[2026_06_04_schema_validator_part_4](2026_06_04_schema_validator_part_4.py)*

## **_Task condition:_**

Given an dictionary, determine if it matches the following schema:

```
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean
}
```

- The pipe (`|`) symbol means `"or"`. `role` must be one of the listed `Roles` values.
- The question mark (`?`) after `supporter` means that the field is optional, but is the specified type if it exists.
- Extra keys are allowed

### **_Examples_**

```
Input: is_valid_schema({"username": "vivian", "posts": 1, "verified": False, "role": "user", "supporter": True}) => Output: True

Input: is_valid_schema({"username": "rudolph", "posts": 15, "verified": True, "role": "creator"}) => Output: True

Input: is_valid_schema({"username": "hernandez", "posts": 35, "verified": True, "role": "moderator", "supporter": False, "followers": 55}) => Output: True

Input: is_valid_schema({"username": "julia", "posts": 50, "verified": True, "role": "admin", "supporter": "true"}) => Output: False

Input: is_valid_schema({"username": "bernard", "posts": 0, "verified": True, "role": "friend", "supporter": True}) => Output: False

Input: is_valid_schema({"username": "felix", "posts": 40, "verified": "yes", "role": "staff", "supporter": False}) => Output: False

Input: is_valid_schema({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True}) => Output: False

Input: is_valid_schema({"username": True, "posts": 30, "verified": True, "role": "moderator", "supporter": False}) => Output: False
```
#

<br />

# 2026.06.05 Challenge - Schema Validator Part 5

My solution -> *[2026_06_05_schema_validator_part_5](2026_06_05_schema_validator_part_5.py)*

## **_Task condition:_**

Given an dictionary, determine if it matches the following schema:

```
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}
```

- The pipe (`|`) symbol means `"or"`. `role` must be one of the listed `Roles` values.
- The question mark (`?`) after `supporter` means that the field is optional, but is the specified type if it exists.
- The brackets `[]` after `string` means that `badges` should be an array of strings (or empty).
- Extra keys are allowed

### **_Examples_**

```
Input: is_valid_schema({"username": "gill", "posts": 12, "verified": False, "role": "creator", "supporter": False, "badges": ["early-adopter", "popular"]}) => Output: True

Input: is_valid_schema({"username": "tonya", "posts": 299, "verified": True, "role": "moderator", "supporter": True, "badges": ["streak-master", "veteran"], "followers": 1233}) => Output: True

Input: is_valid_schema({"username": "zara", "posts": 0, "verified": False, "role": "user", "supporter": False, "badges": []}) => Output: True

Input: is_valid_schema({"username": "nicole", "posts": 65, "verified": True, "role": "admin", "supporter": False, "badges": ["first-post", 18]}) => Output: False

Input: is_valid_schema({"username": "tim", "posts": 25, "verified": True, "role": "staff", "supporter": False}) => Output: False

Input: is_valid_schema({"username": "charlie", "posts": 0, "verified": False, "role": "user", "supporter": "no", "badges": ["first-post", "anniversary"]}) => Output: False

Input: is_valid_schema({"username": "wanda", "posts": 15, "verified": True, "role": "friend", "supporter": True, "badges": ["popular"]}) => Output: False

Input: is_valid_schema({"username": "guy", "posts": 5, "verified": "false", "role": "staff", "supporter": True, "badges": ["helper"]}) => Output: False

Input: is_valid_schema({"username": "carrie", "verified": True, "role": "moderator", "supporter": True, "badges": ["helper", "sharer"]}) => Output: False

Input: is_valid_schema({"username": True, "posts": 75, "verified": True, "role": "creator", "supporter": True, "badges": ["veteran"]}) => Output: False
```
#

<br />

# 2026.06.07 Challenge - Last Load

My solution -> *[2026_06_07_last_load](2026_06_07_last_load.py)*

## **_Task condition:_**

Given the number of scoops of laundry detergent you have remaining and an array of how many scoops you used in each of the previous days, return the number of full days of detergent you have remaining.

Calculate your average daily usage from the usage history and assume that amount of usage each day going forward.

### **_Examples_**

```
Input: last_load_date(10, [2, 2, 2, 2, 2, 2, 2]) => Output: 5

Input: last_load_date(16, [2, 3, 0, 3, 4, 2, 1]) => Output: 7

Input: last_load_date(33, [5, 0, 4, 3, 3, 2]) => Output: 11

Input: last_load_date(50, [2, 0, 2, 9, 12, 0, 2]) => Output: 12

Input: last_load_date(20, [13, 9, 12, 10, 8]) => Output: 1
```
#

<br />

# 2026.06.08 Challenge - Jet Lagged

My solution -> *[2026_06_08_jet_lagged](2026_06_08_jet_lagged.py)*

## **_Task condition:_**

Given a departure city, an arrival city, a flight duration in hours, and a direction of travel, return the number of jet lag hours the traveller is experiencing.

The given cities will be from the following list that includes their UTC offset:

| City            | Offset |
| :-------------: | :----: |
| `"Los Angeles"` | -8     |
| `"New York"`    | -5     |
| `"London"`      | 0      |
| `"Istanbul"`    | +3     |
| `"Dubai"`       | +4     |
| `"Hong Kong"`   | +8     |
| `"Tokyo"`       | +9     |

To calculate jet lag hours:

1. Find the timezone difference in hours between the two cities.
2. Determine the direction multiplier. If travelling `"east"`, it's `1.5`, otherwise, it's `1.0`.
3. Get the jet lag hours with the formula: `timezone difference + (flight duration * 0.1) * direction multiplier`

Return the jet lag hours rounded to one decimal place.

### **_Examples_**

```
Input: get_jet_lag_hours("Istanbul", "Hong Kong", 10, "east") => Output: 6.5

Input: get_jet_lag_hours("London", "New York", 8, "west") => Output: 5.8

Input: get_jet_lag_hours("Hong Kong", "Tokyo", 4, "east") => Output: 1.6

Input: get_jet_lag_hours("Dubai", "London", 7, "west") => Output: 4.7

Input: get_jet_lag_hours("Los Angeles", "Hong Kong", 15, "west") => Output: 17.5

Input: get_jet_lag_hours("Tokyo", "Dubai", 9, "west") => Output: 5.9

Input: get_jet_lag_hours("New York", "Istanbul", 10, "east") => Output: 9.5
```
#

<br />

# 2026.06.09 Challenge - Roommates

My solution -> *[2026_06_09_roommates](2026_06_09_roommates.py)*

## **_Task condition:_**

Given an array of people and their roommate group, return the room assignments for a hotel stay using the following rules:

- Each person has a `name` and a `group` property:

```
[
  { "name": "Alice", "group": "A" },
  { "name": "Bob", "group": "B" },
  { "name": "Carol", "group": "A" }
]
```

- People can only share a room with someone from the same group and are paired in the order they are given.
- Return an array of strings with names separated by `" and "` for a shared room, and just the name for a solo room. Names must appear in the order they were paired. For the example above, return `["Alice and Carol", "Bob"]`.

### **_Examples_**

```
Input: get_roommates([{ "name": "Alice", "group": "A" }, { "name": "Bob", "group": "B" }, { "name": "Carol", "group": "A" }]) => Output: ["Alice and Carol", "Bob"]

Input: get_roommates([{ "name": "John", "group": "C" }, { "name": "Julia", "group": "C" }, { "name": "Jim", "group": "C" }]) => Output: ["John and Julia", "Jim"]

Input: get_roommates([{ "name": "Adam", "group": "D" }, { "name": "Abraham", "group": "E" }, { "name": "Austin", "group": "E" }, { "name": "Augustus", "group": "D" }, { "name": "Angelica", "group": "D" }, { "name": "Aaron", "group": "E" }]) => Output: ["Adam and Augustus", "Angelica", "Abraham and Austin", "Aaron"]

Input: get_roommates([{ "name": "Frank", "group": "A" }, { "name": "Emitt", "group": "B" }, { "name": "Daria", "group": "F" }, { "name": "Charles", "group": "D" }, { "name": "Bailey", "group": "A" }, { "name": "Albert", "group": "F" }]) => Output: ["Frank and Bailey", "Emitt", "Daria and Albert", "Charles"]

Input: get_roommates([{ "name": "Kevin", "group": "A" }, { "name": "Yuri", "group": "A" }, { "name": "Hugo", "group": "B" }, { "name": "Violet", "group": "A" }, { "name": "Brett", "group": "A" }, { "name": "Wayne", "group": "B" }]) => Output: ["Kevin and Yuri", "Violet and Brett", "Hugo and Wayne"]
```
#

<br />

# 2026.06.10 Challenge - Itinerary Arrangements

My solution -> *[2026_06_10_itinerary_arrangements](2026_06_10_itinerary_arrangements.py)*

## **_Task condition:_**

Given an array of at least two optional stops for a day trip, return the number of valid itinerary arrangements.

The itinerary always includes `"breakfast"`, `"lunch"`, and `"dinner"`, these will not be passed in as arguments. The optional stops can be placed anywhere in the itinerary, subject to the following rules:

- `"breakfast"` is always first, with at least one stop before `"lunch"`.
- `"lunch"` must appear before `"dinner"`, with at least one stop in between.
- At most, one optional stop may appear after `"dinner"`.

Return the number of valid arrangements.

### **_Examples_**

```
Input: get_itinerary_count(["library", "park"]) => Output: 2

Input: get_itinerary_count(["library", "park", "arcade"]) => Output: 18

Input: get_itinerary_count(["library", "park", "arcade", "store"]) => Output: 120

Input: get_itinerary_count(["library", "park", "arcade", "store", "cafe"]) => Output: 840

Input: get_itinerary_count(["library", "park", "arcade", "store", "cafe", "market", "museum"]) => Output: 55440
```
#

<br />

# 2026.06.11 Challenge - Idea Rankings

My solution -> *[2026_06_11_idea_rankings](2026_06_11_idea_rankings.py)*

## **_Task condition:_**

Given a 2D array where each inner array contains (in this order) an idea name, an optimistic estimate, a realistic estimate, and a pessimistic estimate (in days), return an array of the idea names sorted by expected time to completion, shortest first.

Calculate the expected time to completion for each idea using the following formula:

- `expected = ((optimistic + 4 * realistic + pessimistic) / 6) * length of idea name`

### **_Examples_**

```
Input: analyze_ideas([["Add logging", 2, 5, 15], ["SEO optimization", 4, 8, 20], ["Fix bug", 1, 3, 5]]) => Output: ["Fix bug", "Add logging", "SEO optimization"]

Input: analyze_ideas([["Dark mode", 1, 3, 8], ["Real-time collaboration feature", 6, 12, 20], ["Add tooltip", 1, 2, 4]]) => Output: ["Add tooltip", "Dark mode", "Real-time collaboration feature"]

Input: analyze_ideas([["Update user profile page", 3, 7, 14], ["Add pagination", 2, 5, 10], ["Add tags", 2, 3, 6], ["Fix login bug", 1, 4, 8]]) => Output: ["Add tags", "Fix login bug", "Add pagination", "Update user profile page"]

Input: analyze_ideas([["Migrate database", 14, 25, 40], ["Add chat assistant", 8, 15, 24], ["Redesign onboarding flow", 3, 7, 13], ["Add language support", 6, 11, 18]]) => Output: ["Redesign onboarding flow", "Add language support", "Add chat assistant", "Migrate database"]

Input: analyze_ideas([["Add email notifications", 3, 7, 10], ["Migrate deployment flow", 6, 10, 16], ["Add push notifications", 2, 6, 10], ["Optimize continuous integration", 5, 8, 15], ["Analyze user patterns", 5, 10, 18], ["Create onboarding curriculum", 6, 15, 25]]) => Output: ["Add push notifications", "Add email notifications", "Analyze user patterns", "Migrate deployment flow", "Optimize continuous integration", "Create onboarding curriculum"]
```
#

<br />

# 2026.06.12 Challenge - HTML Content Extractor

My solution -> *[2026_06_12_html_content_extractor](2026_06_12_html_content_extractor.py)*

## **_Task condition:_**

Given a string of HTML, return the plain text content with all tags removed.

### **_Examples_**

```
Input: extract_content('<p>hello world</p>') => Output: "hello world"

Input: extract_content('<p>hello <span>world</span></p>') => Output: "hello world"

Input: extract_content('<a href="example.com">Click me</a>') => Output: "Click me"

Input: extract_content('<p><button onClick="learnToCode()">Learn</button> to <code>code<code> <br/>for <strong>free</strong> <br/>on <a href="https://freecodecamp.org/" target="_blank"><span class="highlight">freecodecamp</span>.org</a>') => Output: "Learn to code for free on freecodecamp.org"

Input: extract_content('<div class="container"><h1 id="title">Welcome to <strong>My</strong> Website.</h1><p>This is a <a href="https://example.com" target="_blank">link</a> to something <em>really</em> <span class="highlight">important</span>.</p><ul><li>Item <strong>one</strong></li><li>Item <em>two</em></li><li>Item three</li></ul><img src="pic.jpg" alt="A picture"/><p class="footer">Contact us at <a href="mailto:hello@example.com">hello@example.com</a> for <span>more <strong>info</strong></span>.</p></div>') => Output: "Welcome to My Website.This is a link to something really important.Item oneItem twoItem threeContact us at hello@example.com for more info."
```
#

<br />

# 2026.06.13 Challenge - Zoning Regulations

My solution -> *[2026_06_13_zoning_regulations](2026_06_13_zoning_regulations.py)*

## **_Task condition:_**

Given a 2D grid (array of arrays) representing a city's building layout, return the coordinates of all buildings that are violating zoning rules.

Each cell in the grid contains one of the labels from the table below. A building is in violation if any of its (up to) `4` neighbors, horizontal or vertical, are a type it cannot be adjacent to.

| Label               | Type          | Cannot be adjacent to |
| :-----------------: | :-----------: | :-------------------: |
| `"i"`               | industrial    | `"R"`, `"I"`          |
| `"A"`               | Agricultural  | `"C"`                 |
| `"R"`               | Residential   | `"i"`, `"C"`          |
| `"I"`               | Institutional | `"i"`                 |
| `"C"`               | Commercial    | `"R"`, `"A"`          |
| `""` (empty string) | undeveloped   | no restrictions       |

Return the coordinates of all violating cells as an array of `[row, col]` pairs, in any order. If no violations exist, return an empty array.

### **_Examples_**

```
Input: get_zone_violations([["R", "C"], ["", "C"]]) => Output: [[0, 0], [0, 1]]

Input: get_zone_violations([["", "i"], ["", "R"], ["R", "I"]]) => Output: [[0, 1], [1, 1]]

Input: get_zone_violations([["A", "i", "C"], ["A", "", "C"], ["R", "R", "I"]]) => Output: []

Input: get_zone_violations([["R", "R", "C", "R", "R"], ["R", "I", "C", "", "A"], ["R", "R", "", "i", "A"]]) => Output: [[0, 1], [0, 2], [0, 3]]

Input: get_zone_violations([["R", "A", "A", "", "i", "i"], ["R", "I", "", "C", "i", "i"], ["R", "", "C", "C", "A", "A"], ["R", "R", "C", "I", "R", "R"]]) => Output: [[2, 3], [2, 4], [3, 1], [3, 2]]
```
#

<br />

# 2026.06.14 Challenge - Credit Card Validator

My solution -> *[2026_06_14_credit_card_validator](2026_06_14_credit_card_validator.py)*

## **_Task condition:_**

Given a string of digits for a credit card number, determine if it's a valid card number using the following method:

- Starting from the second-to-last digit, double every other digit moving left.
- If doubling a digit results in a number greater than `9`, subtract `9`.
- Sum all the digits (doubled and undoubled).
- If the total is divisible by `10`, the number is valid.

### **_Examples_**

```
Input: is_valid_card("4532015112830366") => Output: True

Input: is_valid_card("5425233430109903") => Output: True

Input: is_valid_card("371449635398431") => Output: True

Input: is_valid_card("6011111111111117") => Output: True

Input: is_valid_card("4532015112830367") => Output: False

Input: is_valid_card("1234567890123456") => Output: False

Input: is_valid_card("4532015112830368") => Output: False
```
#

<br />