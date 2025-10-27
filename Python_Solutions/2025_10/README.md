# 2025.10.01 Challenge - Binary To Decimal

My solution -> *[2025_10_01_binary_to_decimal](2025_10_01_binary_to_decimal.py)*

## **_Task condition:_**

Given a string representing a binary number, return its decimal equivalent as a number.

A binary number uses only the digits `0` and `1` to represent any number. To convert binary to decimal, multiply each digit by a power of `2` and add them together. Start by multiplying the rightmost digit by `2^0`, the next digit to the left by `2^1`, and so on. Once all digits have been multiplied by a power of `2`, add the result together.

For example, the binary number `101` equals `5` in decimal because:

```
1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5
```

### **_Examples_**

```
Input: to_decimal("101") => Output: 5

Input: to_decimal("1010") => Output: 10

Input: to_decimal("10010") => Output: 18

Input: to_decimal("1010101") => Output: 85
```

#

<br />

# 2025.10.02 Challenge - Decimal To Binary

My solution -> *[2025_10_02_decimal_to_binary](2025_10_02_decimal_to_binary.py)*

## **_Task condition:_**

Given a non-negative integer, return its binary representation as a string.

A binary number uses only the digits `0` and `1` to represent any number. To convert a decimal number to binary, repeatedly divide the number by `2` and record the remainder. Repeat until the number is zero. Read the remainders last recorded to first. For example, to convert `12` to binary:

```
12 ÷ 2 = 6 remainder 0
6 ÷ 2 = 3 remainder 0
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1
```

`12` in binary is `1100`.

### **_Examples_**

```
Input: to_binary(5) => Output: "101"

Input: to_binary(12) => Output: "1100"

Input: to_binary(50) => Output: "110010"

Input: to_binary(99) => Output: "1100011"
```

#

<br />

# 2025.10.03 Challenge - P@ssw0rd Str3ngth!

My solution -> *[2025_10_03_password_strength](2025_10_03_password_strength.py)*

## **_Task condition:_**

Given a password string, return `"weak"`, `"medium"`, or `"strong"` based on the strength of the password.

A password is evaluated according to the following rules:

- It is at least `8` characters long.
- It contains both uppercase and lowercase letters.
- It contains at least one number.
- It contains at least one special character from this set: `!`, `@`, `#`, `$`, `%`, `^`, `&`, or `*`.

Return `"weak"` if the password meets fewer than two of the rules. Return `"medium"` if the password meets 2 or 3 of the rules. Return `"strong"` if the password meets all `4` rules.

### **_Examples_**

```
Input: check_strength("123456") => Output: "weak"

Input: check_strength("pass!!!") => Output: "weak"

Input: check_strength("Qwerty") => Output: "weak"

Input: check_strength("PASSWORD") => Output: "weak"

Input: check_strength("PASSWORD!") => Output: "medium"

Input: check_strength("PassWord%^!") => Output: "medium"

Input: check_strength("qwerty12345") => Output: "medium"

Input: check_strength("PASSWORD!") => Output: "medium"

Input: check_strength("PASSWORD!") => Output: "medium"

Input: check_strength("S3cur3P@ssw0rd") => Output: "strong"

Input: check_strength("C0d3&Fun!") => Output: "strong"
```

#

<br />

# 2025.10.04 Challenge - Space Week Day 1: Stellar Classification

My solution -> *[2025_10_04_space_week_day_1_stellar_classification](2025_10_04_space_week_day_1_stellar_classification.py)*

## **_Task condition:_**

October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.

For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar classification based on the following ranges:

- `"O"`: 30,000 K or higher
- `"B"`: 10,000 K - 29,999 K
- `"A"`: 7,500 K - 9,999 K
- `"F"`: 6,000 K - 7,499 K
- `"G"`: 5,200 K - 5,999 K
- `"K"`: 3,700 K - 5,199 K
- `"M"`: 0 K - 3,699 K

Return the classification of the given star.

### **_Examples_**

```
Input: classification(5778) => Output: "G"

Input: classification(2400) => Output: "M"

Input: classification(9999) => Output: "A"

Input: classification(3700) => Output: "K"

Input: classification(3699) => Output: "M"

Input: classification(210000) => Output: "O"

Input: classification(6000) => Output: "F"

Input: classification(11432) => Output: "B"
```

#

<br />

# 2025.10.05 Challenge - Space Week Day 2: Exoplanet Search

My solution -> *[2025_10_05_space_week_day_2_exoplanet_search](2025_10_05_space_week_day_2_exoplanet_search.py)*

## **_Task condition:_**

For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

- Luminosity readings only comprise of characters `0-9` and `A-Z` where each reading corresponds to the following numerical values:
- Characters `0-9` correspond to luminosity levels `0-9`.
- Characters `A-Z` correspond to luminosity levels `10-35`.

A star is considered to have an exoplanet if any single reading is less than or equal to `80%` of the average of all readings. For example, if the average luminosity of a star is `10`, it would be considered to have a exoplanet if any single reading is `8` or less.

### **_Examples_**

```
Input: has_exoplanet("665544554") => Output: False

Input: has_exoplanet("FGFFCFFGG") => Output: True

Input: has_exoplanet("MONOPLONOMONPLNOMPNOMP") => Output: False

Input: has_exoplanet("FREECODECAMP") => Output: True

Input: has_exoplanet("9AB98AB9BC98A") => Output: False

Input: has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE") => Output: True
```

#

<br />

# 2025.10.06 Challenge - Space Week Day 3: Phone Home

My solution -> *[2025_10_06_space_week_day_3_phone_home](2025_10_06_space_week_day_3_phone_home.py)*

## **_Task condition:_**

For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:

- The first value in the array is the distance from your location to the first satellite.
- Each subsequent value, except for the last, is the distance to the next satellite.
- The last value in the array is the distance from the previous satellite to your home planet.
- The message travels at `300,000 km/s`.
- Each satellite the message `passes through` adds a `0.5` second transmission delay.
- Return a number rounded to `4` decimal places, with trailing zeros removed.

### **_Examples_**

```
Input: send_message([300000, 300000]) => Output: 2.5

Input: send_message([384400, 384400]) => Output: 3.0627

Input: send_message([54600000, 54600000]) => Output: 364.5

Input: send_message([1000000, 500000000, 1000000]) => Output: 1674.3333

Input: send_message([10000, 21339, 50000, 31243, 10000]) => Output: 2.4086

Input: send_message([802101, 725994, 112808, 3625770, 481239]) => Output: 21.1597
```

#

<br />

# 2025.10.07 Challenge - Space Week Day 4: Landing Spot

My solution -> *[2025_10_07_space_week_day_4_landing_spot](2025_10_07_space_week_day_4_landing_spot.py)*

## **_Task condition:_**

In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

- Each spot in the matrix will contain a number from `0-9`, inclusive.
- Any `0` represents a potential landing spot.
- Any number other than `0` is too dangerous to land. The higher the number, the more dangerous.
- The safest spot is defined as the `0` cell whose surrounding cells (up to `4` neighbors, ignore diagonals) have the lowest total danger.
- Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
- Return the indices of the safest landing spot. There will always only be one safest spot.

For instance, given:

```
[
  [1, 0],
  [2, 0]
]
```

Return `[0, 1]`, the indices for the `0` in the first array.

### **_Examples_**

```
Input: find_landing_spot([[1, 0], [2, 0]]) => Output: [0, 1]

Input: find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]) => Output: [1, 1]

Input: find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]) => Output: [2, 2]

Input: find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]) => Output: [2, 1]

```

#

<br />

# 2025.10.08 Challenge - Space Week Day 5: Goldilocks Zone

My solution -> *[2025_10_08_space_week_day_5_goldilocks_zone](2025_10_08_space_week_day_5_goldilocks_zone.py)*

## **_Task condition:_**

For the fifth day of Space Week, you will calculate the `"Goldilocks Zone"` of a star - the region around a star where conditions are "just right" for liquid water to exist.

Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.

To calculate the Goldilocks Zone:

- Find the luminosity of the star by raising its mass to the power of `3.5`.
- The start of the zone is `0.95` times the square root of its luminosity.
- The end of the zone is `1.37` times the square root of its luminosity.

For example, given `1` as a mass, return `[0.95, 1.37]`.

### **_Examples_**

```
Input: goldilocks_zone(1) => Output: [0.95, 1.37]

Input: goldilocks_zone(0.5) => Output: [0.28, 0.41]

Input: goldilocks_zone(6) => Output: [21.85, 31.51]

Input: goldilocks_zone(3.7) => Output: [9.38, 13.52]

Input: goldilocks_zone(20) => Output: [179.69, 259.13]
```

**_NOTES:_**

- Return the distances rounded to two decimal places.

#

<br />

# 2025.10.09 Challenge - Space Week Day 6: Moon Phase

My solution -> *[2025_10_09_space_week_day_6_moon_phase](2025_10_09_space_week_day_6_moon_phase.py)*

## **_Task condition:_**

For day six of Space Week, you will be given a date in the format `"YYYY-MM-DD"` and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of `28` days, divided into four equal phases:

- `"New"`: days 1 - 7
- `"Waxing"`: days 8 - 14
- `"Full"`: days 15 - 21
- `"Waning"`: days 22 - 28

After day `28`, the cycle repeats with day `1`, a new moon.

### **_Examples_**

```
Input: moon_phase("2000-01-12") => Output: "New"

Input: moon_phase("2000-01-13") => Output: "Waxing"

Input: moon_phase("2014-10-15") => Output: "Full"

Input: moon_phase("2012-10-21") => Output: "Waning"

Input: moon_phase("2022-12-14") => Output: "New"
```

**_NOTES:_**

- Use `"2000-01-06"` as a reference new moon (day `1` of the cycle) to determine the phase of the given day.
- You will not be given any dates before the reference date.
- Return the correct phase as a string.

#

<br />

# 2025.10.10 Challenge - Space Week Day 7: Launch Fuel

My solution -> *[2025_10_10_space_week_day_7_launch_fuel](2025_10_10_space_week_day_7_launch_fuel.py)*

## **_Task condition:_**

For the final day of Space Week, you will be given the mass in kilograms (`kg`) of a payload you want to send to orbit. Determine the amount of fuel needed to send your payload to orbit using the following rules:

- Rockets require `1` kg of fuel per `5` kg of mass they must lift.
- Fuel itself has mass. So when you add fuel, the mass to lift goes up, which requires more fuel, which increases the mass, and so on.
- To calculate the total fuel needed: start with the payload mass, calculate the fuel needed for that, add that fuel to the total mass, and calculate again. Repeat this process until the additional fuel required is less than `1` kg, then stop.
- Ignore the mass of the rocket itself. Only compute fuel needed to lift the payload and its own fuel.

For example, given a payload mass of `50` kg, you would need `10` kg of fuel to lift it (`payload / 5`), which increases the total mass to `60` kg, which needs `12` kg to lift (`2` additional kg), which increases the total mass to `62` kg, which needs `12.4` kg to lift - `0.4` additional kg - which is less `1` additional kg, so we stop here. The total mass to lift is `62.4` kg, `50` of which is the initial payload and `12.4` of fuel.

- Return the amount of fuel needed rounded to one decimal place.

### **_Examples_**

```
Input: launch_fuel(50) => Output: 12.4

Input: launch_fuel(500) => Output: 124.8

Input: launch_fuel(243) => Output: 60.7

Input: launch_fuel(11000) => Output: 2749.8

Input: launch_fuel(6214) => Output: 1553.4
```

#

<br />

# 2025.10.11 Challenge - Hex To Decimal

My solution -> *[2025_10_11_hex_to_decimal](2025_10_11_hex_to_decimal.py)*

## **_Task condition:_**

Given a string representing a hexadecimal number (`base 16`), return its decimal (`base 10`) value as an integer.

Hexadecimal is a number system that uses `16` digits:

- `0-9` represent values `0` through `9`.
- `A-F` represent values `10` through `15`.

Here's a partial conversion table:

| Hexadecimal   | Decimal    |
| :-----------: | :--------: |
| 0             | 0          |
| 1             | 1          |
| ...           | ...        |
| 9             | 9          |
| A             | 10         |
| ...           | ...        |
| F             | 15         |
| 10            | 16         |
| ...           | ...        |
| 9F            | 159        |
| A0            | 160        |
| ...           | ...        |
| FF            | 255        |
| 100           | 256        |

- The string will only contain characters `0–9` and `A–F`.

### **_Examples_**

```
Input: hex_to_decimal("A") => Output: 10

Input: hex_to_decimal("15") => Output: 21

Input: hex_to_decimal("2E") => Output: 46

Input: hex_to_decimal("FF") => Output: 255

Input: hex_to_decimal("A3F") => Output: 2623
```

#

<br />

# 2025.10.12 Challenge - Battle Of Words

My solution -> *[2025_10_12_battle_of_words](2025_10_12_battle_of_words.py)*

## **_Task condition:_**

Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

- The given sentences will always contain the same number of words.
- Words are separated by a single space and will only contain letters.
- The value of each word is the sum of its letters.
- Letters `a` to `z` correspond to the values `1` through `26`. For example, `a` is `1`, and `z` is `26`.
- A capital letter doubles the value of the letter. For example, `A` is `2`, and `Z` is `52`.
- Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
- A word wins if its value is greater than the opposing word's value.
- The team with more winning words is the winner.

Return `"We win"` if your team is the winner, `"We lose"` if your team loses, and `"Draw"` if both teams have the same number of wins.

### **_Examples_**

```
Input: battle("hello world", "hello word") => Output: "We win"

Input: battle("Hello world", "hello world") => Output: "We win"

Input: battle("lorem ipsum", "kitty ipsum") => Output: "We lose"

Input: battle("hello world", "world hello") => Output: "Draw"

Input: battle("git checkout", "git switch") => Output: "We win"

Input: battle("Cheeseburger with fries", "Cheeseburger with Fries") => Output: "We lose"

Input: battle("We must never surrender", "Our team must win") => Output: "Draw"
```

#

<br />

# 2025.10.13 Challenge - 24 To 12

My solution -> *[2025_10_13_24_to_12](2025_10_13_24_to_12.py)*

## **_Task condition:_**

Given a string representing a time of the day in the `24-hour` format of `"HHMM"`, return the time in its equivalent `12-hour` format of `"H:MM AM"` or `"H:MM PM"`.

- The given input will always be a four-digit string in `24-hour` time format, from `"0000"` to `"2359"`.

### **_Examples_**

```
Input: to_12("1124") => Output: "11:24 AM"

Input: to_12("0900") => Output: "9:00 AM"

Input: to_12("1455") => Output: "2:55 PM"

Input: to_12("2346") => Output: "11:46 PM"

Input: to_12("0030") => Output: "12:30 AM"
```

#

<br />

# 2025.10.14 Challenge - String Count

My solution -> *[2025_10_14_string_count](2025_10_14_string_count.py)*

## **_Task condition:_**

Given two strings, determine how many times the second string appears in the first.

### **_Examples_**

```
Input: count('abcdefg', 'def') => Output: 1

Input: count('hello', 'world') => Output: 0

Input: count('mississippi', 'iss') => Output: 2

Input: count('she sells seashells by the seashore', 'sh') => Output: 3

Input: count('101010101010101010101', '101') => Output: 10
```

**_NOTES:_**

- The pattern string can overlap in the first string. For example, `"aaa"` contains `"aa"` twice. The first two `a`'s and the second two.

#

<br />

# 2025.10.15 Challenge - HTML Tag Stripper

My solution -> *[2025_10_15_html_tag_stripper](2025_10_15_html_tag_stripper.py)*

## **_Task condition:_**

Given a string of `HTML` code, remove the tags and return the plain text content.

- The input string will contain only valid `HTML`.
- `HTML` tags may be nested.
- Remove the tags and any attributes.

For example, `'<a href="#">Click here</a>'` should return `"Click here"`.

### **_Examples_**

```
Input: strip_tags('<a href="#">Click here</a>') => Output: "Click here"

Input: strip_tags('<p class="center">Hello <b>World</b>!</p>') => Output: "Hello World!"

Input: strip_tags('<img src="cat.jpg" alt="Cat">') => Output: ""

Input: strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>') => Output: "sectionsection"
```

#

<br />

# 2025.10.16 Challenge - Email Validator

My solution -> *[2025_10_16_email_validator](2025_10_16_email_validator.py)*

## **_Task condition:_**

Given a string, determine if it is a valid email address using the following constraints:

- It must contain exactly one `@` symbol.
- The local part (before the `@`):
  - Can only contain letters (`a-z`, `A-Z`), digits (`0-9`), dots (`.`), underscores (`_`), or hyphens (`-`).
  - Cannot start or end with a dot.
- The domain part (after the `@`):
  - Must contain at least one dot.
  - Must end with a dot followed by at least two letters.
- Neither the local or domain part can have two dots in a row.

### **_Examples_**

```
Input: validate("a@b.cd") => Output: True

Input: validate("hell.-w.rld@example.com") => Output: True

Input: validate(".b@sh.rc") => Output: False

Input: validate("example@test.c0") => Output: False

Input: validate("freecodecamp.org") => Output: False

Input: validate("develop.ment_user@c0D!NG.R.CKS") => Output: True

Input: validate("hello.@wo.rld") => Output: False

Input: validate("hello@world..com") => Output: False

Input: validate("git@commit@push.io") => Output: False
```

#

<br />

# 2025.10.17 Challenge - Credit Card Masker

My solution -> *[2025_10_17_credit_card_masker](2025_10_17_credit_card_masker.py)*

## **_Task condition:_**

Given a string of credit card numbers, return a masked version of it using the following constraints:

- The string will contain four sets of four digits (`0-9`), with all sets being separated by a single space, or a single hyphen (`-`).
- Replace all numbers, except the last four, with an asterisk (`*`).
- Leave the remaining characters unchanged.

For example, given `"4012-8888-8888-1881"` return `"****-****-****-1881"`.

### **_Examples_**

```
Input: mask("4012-8888-8888-1881") => Output: "****-****-****-1881"

Input: mask("5105 1051 0510 5100") => Output: "**** **** **** 5100"

Input: mask("6011 1111 1111 1117") => Output: "**** **** **** 1117"

Input: mask("2223-0000-4845-0010") => Output: "****-****-****-0010"
```

#

<br />

# 2025.10.18 Challenge - Missing Socks

My solution -> *[2025_10_18_missing_socks](2025_10_18_missing_socks.py)*

## **_Task condition:_**

Given an integer representing the number of pairs of socks you started with, and another integer representing how many wash cycles you have gone through, return the number of complete pairs of socks you currently have using the following constraints:

- Every `2` wash cycles, you lose a single sock.
- Every `3` wash cycles, you find a single missing sock.
- Every `5` wash cycles, a single sock is worn out and must be thrown away.
- Every `10` wash cycles, you buy a pair of socks.
- You can never have less than `zero` total socks.
- Rules can overlap. For example, on wash cycle `10`, you will lose a single sock, throw away a single sock, and buy a new pair of socks.
- Return the number of complete pairs of socks.

### **_Examples_**

```
Input: sock_pairs(2, 5) => Output: 1

Input: sock_pairs(1, 2) => Output: 0

Input: sock_pairs(5, 11) => Output: 4

Input: sock_pairs(6, 25) => Output: 3

Input: sock_pairs(1, 8) => Output: 0
```

#

<br />

# 2025.10.19 Challenge - HTML Attribute Extractor

My solution -> *[2025_10_19_html_attribute_extractor](2025_10_19_html_attribute_extractor.py)*

## **_Task condition:_**

Given a string of a valid HTML element, return the attributes of the element using the following criteria:

- You will only be given one element.
- Attributes will be in the format: `attribute="value"`.
- Return an array of strings with each attribute property and value, separated by a comma, in this format: `["attribute1, value1", "attribute2, value2"]`.
- Return attributes in the order they are given.
- If no attributes are found, return an empty array.

### **_Examples_**

```
Input: extract_attributes('<span class="red"></span>') => Output: ["class, red"]

Input: extract_attributes('<meta charset="UTF-8" />') => Output: ["charset, UTF-8"]

Input: extract_attributes("<p>Lorem ipsum dolor sit amet</p>") => Output: []

Input: extract_attributes('<input name="email" type="email" required="true" />') => Output: ["name, email", "type, email", "required, true"]

Input: extract_attributes('<button id="submit" class="btn btn-primary">Submit</button>') => Output: ["id, submit", "class, btn btn-primary"]
```

#

<br />

# 2025.10.20 Challenge - Tip Calculator

My solution -> *[2025_10_20_tip_calculator](2025_10_20_tip_calculator.py)*

## **_Task condition:_**

Given the price of your meal and a custom tip percent, return an array with three tip values; `15%`, `20%`, and the custom amount.

- Prices will be given in the format: `"$N.NN"`.
- Custom tip percents will be given in this format: `"25%"`.
- Return amounts in the same `"$N.NN"` format, rounded to two decimal places.

For example, given a `"$10.00"` meal price, and a `"25%"` custom tip value, return `["$1.50", "$2.00", "$2.50"]`.

### **_Examples_**

```
Input: calculate_tips("$10.00", "25%") => Output: ["$1.50", "$2.00", "$2.50"]

Input: calculate_tips("$89.67", "26%") => Output: ["$13.45", "$17.93", "$23.31"]

Input: calculate_tips("$19.85", "9%") => Output: ["$2.98", "$3.97", "$1.79"]
```

#

<br />

# 2025.10.21 Challenge - Thermostat Adjuster 2

My solution -> *[2025_10_21_thermostat_adjuster_2](2025_10_21_thermostat_adjuster_2.py)*

## **_Task condition:_**

Given the current temperature of a room in `Fahrenheit` and a target temperature in `Celsius`, return a string indicating how to adjust the room temperature based on these constraints:

- Return `"Heat: X degrees Fahrenheit"` if the current temperature is below the target. With `X` being the number of degrees in `Fahrenheit` to heat the room to reach the target, rounded to `1` decimal place.
- Return `"Cool: X degrees Fahrenheit"` if the current temperature is above the target. With `X` being the number of degrees in `Fahrenheit` to cool the room to reach the target, rounded to `1` decimal place.
- Return `"Hold"` if the current temperature is equal to the target.

To convert Celsius to Fahrenheit, multiply the Celsius temperature by `1.8` and add `32` to the result (`F = (C * 1.8) + 32`).

### **_Examples_**

```
Input: adjust_thermostat(32, 0) => Output: "Hold"

Input: adjust_thermostat(70, 25) => Output: "Heat: 7.0 degrees Fahrenheit"

Input: adjust_thermostat(72, 18) => Output: "Cool: 7.6 degrees Fahrenheit"

Input: adjust_thermostat(212, 100) => Output: "Hold"

Input: adjust_thermostat(59, 22) => Output: "Heat: 12.6 degrees Fahrenheit"
```

#

<br />

# 2025.10.22 Challenge - Speak Wisely, You Must

My solution -> *[2025_10_22_speak_wisely_you_must](2025_10_22_speak_wisely_you_must.py)*

## **_Task condition:_**

Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:

- Words are separated by a single space.
- Find the first occurrence of one of the following words in the sentence: `"have"`, `"must"`, `"are"`, `"will"`, `"can"`.
- Move all words before and including that word to the end of the sentence and:
  - Preserve the order of the words when you move them.
  - Make them all lowercase.
  - And add a comma and space before them.
- Capitalize the first letter of the new first word of the sentence.
- All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
- Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.

For example, given `"You must speak wisely."` return `"Speak wisely, you must."`

### **_Examples_**

```
Input: wise_speak("You must speak wisely.") => Output: "Speak wisely, you must."

Input: wise_speak("You can do it!") => Output: "Do it, you can!"

Input: wise_speak("Do you think you will complete this?") => Output: "Complete this, do you think you will?"

Input: wise_speak("All your base are belong to us.") => Output: "Belong to us, all your base are."

Input: wise_speak("You have much to learn.") => Output: "Much to learn, you have."
```

#

<br />

# 2025.10.23 Challenge - Favorite Songs

My solution -> *[2025_10_23_favorite_songs](2025_10_23_favorite_songs.py)*

## **_Task condition:_**

Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

- Each object will have a `"title"` property (string), and a `"plays"` property (integer).

### **_Examples_**

```
Input: favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]) => Output: ["Sync or Swim", "Earbud Blues"]

Input: favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ]) => Output: ["Clickwheel Love", "99 Downloads"]

Input: favorite_songs([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75} ]) => Output: ["Song B", "Song C"]
```

#

<br />

# 2025.10.24 Challenge - Hidden Treasure

My solution -> *[2025_10_24_hidden_treasure](2025_10_24_hidden_treasure.py)*

## **_Task condition:_**

Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates (`[row, column]`) for the next dive of your treasure search, return `"Empty"`, `"Found"`, or `"Recovered"` using the following rules:

- The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.
- Each cell in the 2D array will contain one of the following values:
  
  - `"-"`: No treasure.
  - `"O"`: A part of the treasure that has not been found.
  - `"X"`: A part of the treasure that has already been found.

- If the dive location has no treasure, return `"Empty"`.
- If the dive location finds treasure, but at least one other part of the treasure remains unfound, return `"Found"`.
- If the dive location finds the last unfound part of the treasure, return `"Recovered"`.

For example, given:

```
[
  [ "-", "X"],
  [ "-", "X"],
  [ "-", "O"]
]
```

And `[2, 1]` for the coordinates of the dive location, return `"Recovered"` because the dive found the last unfound part of the treasure.

### **_Examples_**

```
Input: dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]) => Output: "Recovered"

Input: dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0]) => Output: "Empty"

Input: dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]) => Output: "Found"

Input: dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2]) => Output: "Found"

Input: dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]) => Output: "Recovered"

Input: dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]) => Output: "Empty"
```

#

<br />

# 2025.10.25 Challenge - Complementary DNA

My solution -> *[2025_10_25_complementary_dna](2025_10_25_complementary_dna.py)*

## **_Task condition:_**

Given a string representing a `DNA` sequence, return its complementary strand using the following rules:

- `DNA` consists of the letters `"A"`, `"C"`, `"G"`, and `"T"`.
- The letters `"A"` and `"T"` complement each other.
- The letters `"C"` and `"G"` complement each other.

For example, given `"ACGT"`, return `"TGCA"`.

### **_Examples_**

```
Input: complementary_dna("ACGT") => Output: "TGCA"

Input: complementary_dna("ATGCGTACGTTAGC") => Output: "TACGCATGCAATCG"

Input: complementary_dna("GGCTTACGATCGAAG") => Output: "CCGAATGCTAGCTTC"

Input: complementary_dna("GATCTAGCTAGGCTAGCTAG") => Output: "CTAGATCGATCCGATCGATC"
```

#

<br />

# 2025.10.26 Challenge - Duration Formatter

My solution -> *[2025_10_26_duration_formatter](2025_10_26_duration_formatter.py)*

## **_Task condition:_**

Given an integer number of seconds, return a string representing the same duration in the format `"H:MM:SS"`, where `"H"` is the number of hours, `"MM"` is the number of minutes, and `"SS"` is the number of seconds. Return the time using the following rules:

- `Seconds`: Should always be two digits.
- `Minutes`: Should omit leading zeros when they aren't needed. Use `"0"` if the duration is less than one minute.
- `Hours`: Should be included only if they're greater than zero.

### **_Examples_**

```
Input: format(500) => Output: "8:20"

Input: format(4000) => Output: "1:06:40"

Input: format(1) => Output: "0:01"

Input: format(5555) => Output: "1:32:35"

Input: format(99999) => Output: "27:46:39"
```

#

<br />

# 2025.10.27 Challenge - Integer Sequence

My solution -> *[2025_10_27_integer_sequence](2025_10_27_integer_sequence.py)*

## **_Task condition:_**

Given a positive integer, return a string with all of the integers from `1` up to, and including, the given number, in numerical order.

For example, given `5`, return `"12345"`.

### **_Examples_**

```
Input: sequence(5) => Output: "12345"

Input: sequence(10) => Output: "12345678910"

Input: sequence(1) => Output: "1"

Input: sequence(27) => Output: "123456789101112131415161718192021222324252627"
```

#

<br />