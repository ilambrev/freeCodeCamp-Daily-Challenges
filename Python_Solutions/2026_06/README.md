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