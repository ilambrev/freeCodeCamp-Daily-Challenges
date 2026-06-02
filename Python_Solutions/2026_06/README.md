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