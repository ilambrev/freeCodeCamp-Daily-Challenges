# 2026.02.01 Challenge - Digital Detox

My solution -> *[2026_02_01_digital_detox](2026_02_01_digital_detox.py)*

## **_Task condition:_**

Given an array of your login logs, determine whether you have met your digital detox goal.

Each log is a string in the format `"YYYY-MM-DD HH:mm:ss"`.

You have met your digital detox goal if both of the following statements are true:

- You logged in no more than `once` within any `four-hour` period.
- You logged in no more than `2` times on any `single day`.

### **_Examples_**

```
Input: digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]) => Output: True

Input: digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]) => Output: False

Input: digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"]) => Output: True

Input: digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"]) => Output: False

Input: digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00","2026-02-01 16:50:00", "2026-02-03 09:30:00"]) => Output: True

Input: digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]) => Output: False
```

#

<br />

# 2026.02.02 Challenge - Groundhog Day

My solution -> *[2026_02_02_groundhog_day](2026_02_02_groundhog_day.py)*

## **_Task condition:_**

Today is Groundhog Day, in which a groundhog predicts the weather based on whether or not it sees its shadow.

Given a value representing the groundhog's appearance, return the correct prediction:

- If the given value is the boolean `true` (the groundhog saw its shadow), return `"Looks like we'll have six more weeks of winter."`.
- If the value is the boolean `false` (the groundhog did not see its shadow), return `"It's going to be an early spring."`.
- If the value is anything `else` (the groundhog did not show up), return `"No prediction this year."`.

### **_Examples_**

```
Input: groundhog_day_prediction(True) => Output: "Looks like we'll have six more weeks of winter."

Input: groundhog_day_prediction(False) => Output: "It's going to be an early spring."

Input: groundhog_day_prediction(None) => Output: "No prediction this year."

Input: groundhog_day_prediction(" ") => Output: "No prediction this year."

Input: groundhog_day_prediction("True") => Output: "No prediction this year."
```

#

<br />

# 2026.02.03 Challenge - String Mirror

My solution -> *[2026_02_03_string_mirror](2026_02_03_string_mirror.py)*

## **_Task condition:_**

Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end of it.

### **_Examples_**

```
Input: mirror("freeCodeCamp") => Output: "freeCodeCamppmaCedoCeerf"

Input: mirror("RaceCar") => Output: "RaceCarraCecaR"

Input: mirror("helloworld") => Output: "helloworlddlrowolleh"

Input: mirror("The quick brown fox...") => Output: "The quick brown fox......xof nworb kciuq ehT"
```

#

<br />

# 2026.02.04 Challenge - Truncate the Text

My solution -> *[2026_02_04_truncate_the_text](2026_02_04_truncate_the_text.py)*

## **_Task condition:_**

Given a string, return it as-is if it's `20` characters or shorter. If it's longer than `20` characters, truncate it to the first `17` characters and append `"..."` to the end of it (so it's `20` characters total) and return the result.

### **_Examples_**

```
Input: truncate_text("Hello, world!") => Output: "Hello, world!"

Input: truncate_text("This string should get truncated.") => Output: "This string shoul..."

Input: truncate_text("Exactly twenty chars") => Output: "Exactly twenty chars"

Input: truncate_text(".....................") => Output: "...................."
```

#

<br />