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