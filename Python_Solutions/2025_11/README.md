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