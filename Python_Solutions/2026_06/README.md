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