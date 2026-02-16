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

# 2026.02.05 Challenge - Pocket Change

My solution -> *[2026_02_05_pocket_change](2026_02_05_pocket_change.py)*

## **_Task condition:_**

Given an array of integers representing the coins in your pocket, with each integer being the value of a coin in cents, return the total amount in the format `"$D.CC"`.

- `100` cents equals `1` dollar.
- In the return value, include a leading zero for amounts less than one dollar and always exactly two digits for the cents.

### **_Examples_**

```
Input: count_change([25, 10, 5, 1]) => Output: "$0.41"

Input: count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]) => Output: "$1.43"

Input: count_change([100, 25, 100, 1000, 5, 500, 2000, 25]) => Output: "$37.55"

Input: count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]) => Output: "$0.70"

Input: count_change([1]) => Output: "$0.01"

Input: count_change([25, 25, 25, 25]) => Output: "$1.00"
```

#

<br />

# 2026.02.06 Challenge - 2026 Winter Games Day 1: Opening Day

My solution -> *[2026_02_06_2026_winter_games_day_1_opening_day](2026_02_06_2026_winter_games_day_1_opening_day.py)*

## **_Task condition:_**

Today marks the start of the 2026 Winter Games. The next 17 days will bring you coding challenges inspired by them.

For the first one, you are given a two-letter country code and need to return the flag emoji for that country.

Use this list:

| Country                | Code   | Flag   |
| :--------------------: | :----: | :----: |	 	
| Albania 	             | `"AL"` | `"🇦🇱"` |
| Andorra                | `"AD"` | `"🇦🇩"` |
| Argentina              | `"AR"` | `"🇦🇷"` |
| Armenia                | `"AM"` | `"🇦🇲"` |
| Australia              | `"AU"` | `"🇦🇺"` |
| Austria                | `"AT"` | `"🇦🇹"` |
| Azerbaijan             | `"AZ"` | `"🇦🇿"` |
| Belgium                | `"BE"` | `"🇧🇪"` |
| Benin                  | `"BJ"` | `"🇧🇯"` |
| Bolivia                | `"BO"` | `"🇧🇴"` |
| Bosnia and Herzegovina | `"BA"` | `"🇧🇦"` |
| Brazil                 | `"BR"` | `"🇧🇷"` |
| Bulgaria               | `"BG"` | `"🇧🇬"` |
| Canada                 | `"CA"` | `"🇨🇦"` |
| Chile                  | `"CL"` | `"🇨🇱"` |
| China                  | `"CN"` | `"🇨🇳"` |
| Colombia               | `"CO"` | `"🇨🇴"` |
| Croatia                | `"HR"` | `"🇭🇷"` |
| Cyprus                 | `"CY"` | `"🇨🇾"` |
| Czech Republic         | `"CZ"` | `"🇨🇿"` |
| Denmark                | `"DK"` | `"🇩🇰"` |
| Ecuador                | `"EC"` | `"🇪🇨"` |
| Eritrea                | `"ER"` | `"🇪🇷"` |
| Estonia                | `"EE"` | `"🇪🇪"` |
| Finland                | `"FI"` | `"🇫🇮"` |
| France                 | `"FR"` | `"🇫🇷"` |
| Georgia                | `"GE"` | `"🇬🇪"` |
| Germany                | `"DE"` | `"🇩🇪"` |
| Great Britain          | `"GB"` | `"🇬🇧"` |
| Greece                 | `"GR"` | `"🇬🇷"` |
| Guinea-Bissau          | `"GW"` | `"🇬🇼"` |
| Haiti                  | `"HT"` | `"🇭🇹"` |
| Hong Kong              | `"HK"` | `"🇭🇰"` |
| Hungary                | `"HU"` | `"🇭🇺"` |
| Iceland                | `"IS"` | `"🇮🇸"` |
| India                  | `"IN"` | `"🇮🇳"` |
| Iran                   | `"IR"` | `"🇮🇷"` |
| Ireland                | `"IE"` | `"🇮🇪"` |
| Israel                 | `"IL"` | `"🇮🇱"` |
| Italy                  | `"IT"` | `"🇮🇹"` |
| Jamaica                | `"JM"` | `"🇯🇲"` |
| Japan                  | `"JP"` | `"🇯🇵"` |
| Kazakhstan             | `"KZ"` | `"🇰🇿"` |
| Kenya                  | `"KE"` | `"🇰🇪"` |
| Kosovo                 | `"XK"` | `"🇽🇰"` |
| Kyrgyzstan             | `"KG"` | `"🇰🇬"` |
| Latvia                 | `"LV"` | `"🇱🇻"` |
| Lebanon                | `"LB"` | `"🇱🇧"` |
| Liechtenstein          | `"LI"` | `"🇱🇮"` |
| Lithuania              | `"LT"` | `"🇱🇹"` |
| Luxembourg             | `"LU"` | `"🇱🇺"` |
| Madagascar             | `"MG"` | `"🇲🇬"` |
| Malaysia               | `"MY"` | `"🇲🇾"` |
| Malta                  | `"MT"` | `"🇲🇹"` |
| Mexico                 | `"MX"` | `"🇲🇽"` |
| Moldova                | `"MD"` | `"🇲🇩"` |
| Monaco                 | `"MC"` | `"🇲🇨"` |
| Mongolia               | `"MN"` | `"🇲🇳"` |
| Montenegro             | `"ME"` | `"🇲🇪"` |
| Morocco                | `"MA"` | `"🇲🇦"` |
| Netherlands            | `"NL"` | `"🇳🇱"` |
| New Zealand            | `"NZ"` | `"🇳🇿"` |
| Nigeria                | `"NG"` | `"🇳🇬"` |
| North Macedonia        | `"MK"` | `"🇲🇰"` |
| Norway                 | `"NO"` | `"🇳🇴"` |
| Pakistan               | `"PK"` | `"🇵🇰"` |
| Philippines            | `"PH"` | `"🇵🇭"` |
| Poland                 | `"PL"` | `"🇵🇱"` |
| Portugal               | `"PT"` | `"🇵🇹"` |
| Puerto Rico            | `"PR"` | `"🇵🇷"` |
| Romania                | `"RO"` | `"🇷🇴"` |
| San Marino             | `"SM"` | `"🇸🇲"` |
| Saudi Arabia           | `"SA"` | `"🇸🇦"` |
| Serbia                 | `"RS"` | `"🇷🇸"` |
| Singapore              | `"SG"` | `"🇸🇬"` |
| Slovakia               | `"SK"` | `"🇸🇰"` |
| Slovenia               | `"SI"` | `"🇸🇮"` |
| South Africa           | `"ZA"` | `"🇿🇦"` |
| South Korea            | `"KR"` | `"🇰🇷"` |
| Spain                  | `"ES"` | `"🇪🇸"` |
| Sweden                 | `"SE"` | `"🇸🇪"` |
| Switzerland            | `"CH"` | `"🇨🇭"` |
| Thailand               | `"TH"` | `"🇹🇭"` |
| Trinidad & Tobago      | `"TT"` | `"🇹🇹"` |
| Turkey                 | `"TR"` | `"🇹🇷"` |
| Ukraine                | `"UA"` | `"🇺🇦"` |
| United Arab Emirates   | `"AE"` | `"🇦🇪"` |
| United States          | `"US"` | `"🇺🇸"` |
| Uruguay                | `"UY"` | `"🇺🇾"` |
| Uzbekistan             | `"UZ"` | `"🇺🇿"` |
| Venezuela              | `"VE"` | `"🇻🇪"` |

### **_Examples_**

```
Input: get_flag("AL") => Output: "🇦🇱"

Input: get_flag("AD") => Output: "🇦🇩"

Input: get_flag("AR") => Output: "🇦🇷"

Input: get_flag("AM") => Output: "🇦🇲"

Input: get_flag("AU") => Output: "🇦🇺"

Input: get_flag("AT") => Output: "🇦🇹"

Input: get_flag("AZ") => Output: "🇦🇿"

Input: get_flag("BE") => Output: "🇧🇪"

Input: get_flag("BJ") => Output: "🇧🇯"

Input: get_flag("BO") => Output: "🇧🇴"

Input: get_flag("BA") => Output: "🇧🇦"

Input: get_flag("BR") => Output: "🇧🇷"

Input: get_flag("BG") => Output: "🇧🇬"

Input: get_flag("CA") => Output: "🇨🇦"

Input: get_flag("CL") => Output: "🇨🇱"

Input: get_flag("CN") => Output: "🇨🇳"

Input: get_flag("CO") => Output: "🇨🇴"

Input: get_flag("HR") => Output: "🇭🇷"

Input: get_flag("CY") => Output: "🇨🇾"

Input: get_flag("CZ") => Output: "🇨🇿"

Input: get_flag("DK") => Output: "🇩🇰"

Input: get_flag("EC") => Output: "🇪🇨"

Input: get_flag("ER") => Output: "🇪🇷"

Input: get_flag("EE") => Output: "🇪🇪"

Input: get_flag("FI") => Output: "🇫🇮"

Input: get_flag("FR") => Output: "🇫🇷"

Input: get_flag("GE") => Output: "🇬🇪"

Input: get_flag("DE") => Output: "🇩🇪"

Input: get_flag("GB") => Output: "🇬🇧"

Input: get_flag("GR") => Output: "🇬🇷"

Input: get_flag("GW") => Output: "🇬🇼"

Input: get_flag("HT") => Output: "🇭🇹"

Input: get_flag("HK") => Output: "🇭🇰"

Input: get_flag("HU") => Output: "🇭🇺"

Input: get_flag("IS") => Output: "🇮🇸"

Input: get_flag("IN") => Output: "🇮🇳"

Input: get_flag("IR") => Output: "🇮🇷"

Input: get_flag("IE") => Output: "🇮🇪"

Input: get_flag("IL") => Output: "🇮🇱"

Input: get_flag("IT") => Output: "🇮🇹"

Input: get_flag("JM") => Output: "🇯🇲"

Input: get_flag("JP") => Output: "🇯🇵"

Input: get_flag("KZ") => Output: "🇰🇿"

Input: get_flag("KE") => Output: "🇰🇪"

Input: get_flag("XK") => Output: "🇽🇰"

Input: get_flag("KG") => Output: "🇰🇬"

Input: get_flag("LV") => Output: "🇱🇻"

Input: get_flag("LB") => Output: "🇱🇧"

Input: get_flag("LI") => Output: "🇱🇮"

Input: get_flag("LT") => Output: "🇱🇹"

Input: get_flag("LU") => Output: "🇱🇺"

Input: get_flag("MG") => Output: "🇲🇬"

Input: get_flag("MY") => Output: "🇲🇾"

Input: get_flag("MT") => Output: "🇲🇹"

Input: get_flag("MX") => Output: "🇲🇽"

Input: get_flag("MD") => Output: "🇲🇩"

Input: get_flag("MC") => Output: "🇲🇨"

Input: get_flag("MN") => Output: "🇲🇳"

Input: get_flag("ME") => Output: "🇲🇪"

Input: get_flag("MA") => Output: "🇲🇦"

Input: get_flag("NL") => Output: "🇳🇱"

Input: get_flag("NZ") => Output: "🇳🇿"

Input: get_flag("NG") => Output: "🇳🇬"

Input: get_flag("MK") => Output: "🇲🇰"

Input: get_flag("NO") => Output: "🇳🇴"

Input: get_flag("PK") => Output: "🇵🇰"

Input: get_flag("PH") => Output: "🇵🇭"

Input: get_flag("PL") => Output: "🇵🇱"

Input: get_flag("PT") => Output: "🇵🇹"

Input: get_flag("PR") => Output: "🇵🇷"

Input: get_flag("RO") => Output: "🇷🇴"

Input: get_flag("SM") => Output: "🇸🇲"

Input: get_flag("SA") => Output: "🇸🇦"

Input: get_flag("RS") => Output: "🇷🇸"

Input: get_flag("SG") => Output: "🇸🇬"

Input: get_flag("SK") => Output: "🇸🇰"

Input: get_flag("SI") => Output: "🇸🇮"

Input: get_flag("ZA") => Output: "🇿🇦"

Input: get_flag("KR") => Output: "🇰🇷"

Input: get_flag("ES") => Output: "🇪🇸"

Input: get_flag("SE") => Output: "🇸🇪"

Input: get_flag("CH") => Output: "🇨🇭"

Input: get_flag("TH") => Output: "🇹🇭"

Input: get_flag("TT") => Output: "🇹🇹"

Input: get_flag("TR") => Output: "🇹🇷"

Input: get_flag("UA") => Output: "🇺🇦"

Input: get_flag("AE") => Output: "🇦🇪"

Input: get_flag("US") => Output: "🇺🇸"

Input: get_flag("UY") => Output: "🇺🇾"

Input: get_flag("UZ") => Output: "🇺🇿"

Input: get_flag("VE") => Output: "🇻🇪"
```

#

<br />

# 2026.02.07 Challenge - 2026 Winter Games Day 2: Snowboarding

My solution -> *[2026_02_07_2026_winter_games_day_2_snowboarding](2026_02_07_2026_winter_games_day_2_snowboarding.py)*

## **_Task condition:_**

Given a snowboarder's starting stance and a rotation in degrees, determine their landing stance.

- A snowboarder's stance is either `"Regular"` or `"Goofy"`.
- Trick rotations are multiples of `90` degrees. Positive indicates `clockwise rotation`, and negative indicate `counter-clockwise rotation`.
- The landing stance flips every `180` degrees of rotation.

For example, given `"Regular"` and `90`, return `"Regular"`. Given `"Regular"` and `180` degrees, return `"Goofy"`.

### **_Examples_**

```
Input: get_landing_stance("Regular", 90) => Output: "Regular"

Input: get_landing_stance("Regular", 180) => Output: "Goofy"

Input: get_landing_stance("Goofy", -270) => Output: "Regular"

Input: get_landing_stance("Regular", 2340) => Output: "Goofy"

Input: get_landing_stance("Goofy", 2160) => Output: "Goofy"

Input: get_landing_stance("Goofy", -540) => Output: "Regular"
```

#

<br />

# 2026.02.08 Challenge - 2026 Winter Games Day 3: Biathlon

My solution -> *[2026_02_08_2026_winter_games_day_3_biathlon](2026_02_08_2026_winter_games_day_3_biathlon.py)*

## **_Task condition:_**

Given an array of integers, where each value represents the number of targets hit in a single round of a biathlon, return the total penalty distance the athlete must ski.

- Each round consists of `5` targets.
- Each missed target results in a `150` meter penalty loop.

### **_Examples_**

```
Input: calculate_penalty_distance([4, 4]) => Output: 300

Input: calculate_penalty_distance([5, 5]) => Output: 0

Input: calculate_penalty_distance([4, 5, 3, 5]) => Output: 450

Input: calculate_penalty_distance([5, 4, 5, 5]) => Output: 150

Input: calculate_penalty_distance([4, 3, 0, 3]) => Output: 1500
```

#

<br />

# 2026.02.09 Challenge - 2026 Winter Games Day 4: Ski Jumping

My solution -> *[2026_02_09_2026_winter_games_day_4_ski_jumping](2026_02_09_2026_winter_games_day_4_ski_jumping.py)*

## **_Task condition:_**

Given `distance points`, `style points`, a `wind compensation value`, and `K-point bonus` value, calculate your score for the ski jump and determine if you won a medal or not.

- Your score is calculated by summing the above four values.

The current total scores of the other jumpers are:

|       |
|-------|
|`165.5`|
|`172.0`|
|`158.0`|
|`180.0`|
|`169.5`|
|`175.0`|
|`162.0`|
|`170.0`|

- If your score is the best, return `"Gold"`
- If it's second best, return `"Silver"`
- If it's third best, return `"Bronze"`
- Otherwise, return `"No Medal"`

### **_Examples_**

```
Input: ski_jump_medal(125.0, 58.0, 0.0, 6.0) => Output: "Gold"

Input: ski_jump_medal(119.0, 50.0, 1.0, 4.0) => Output: "Bronze"

Input: ski_jump_medal(122.0, 52.0, -1.0, 4.0) => Output: "Silver"

Input: ski_jump_medal(118.0, 50.5, -1.5, 4.0) => Output: "No Medal"

Input: ski_jump_medal(124.0, 50.5, 2.0, 5.0) => Output: "Gold"

Input: ski_jump_medal(119.0, 49.5, 0.0, 3.0) => Output: "No Medal"
```

#

<br />

# 2026.02.10 Challenge - 2026 Winter Games Day 5: Cross-Country Skiing

My solution -> *[2026_02_10_2026_winter_games_day_5_cross_country_skiing](2026_02_10_2026_winter_games_day_5_cross_country_skiing.py)*

## **_Task condition:_**

Given an array of finish times for a cross-country ski race, convert them into times behind the winner.

- Given times are strings in `"H:MM:SS"` format.
- Given times will be in order from fastest to slowest.
- The winners time (fastest time) should correspond to `"0"`.
- Each other time should show the time behind the winner, in the format `"+M:SS"`.

For example, given `["1:25:32", "1:26:10", "1:27:05"]`, return `["0", "+0:38", "+1:33"]`.

### **_Examples_**

```
Input: get_relative_results(["1:25:32", "1:26:10", "1:27:05"]) => Output: ["0", "+0:38", "+1:33"]

Input: get_relative_results(["1:00:01", "1:00:05", "1:00:10"]) => Output: ["0", "+0:04", "+0:09"]

Input: get_relative_results(["1:10:06", "1:10:23", "1:10:48", "1:12:11"]) => Output: ["0", "+0:17", "+0:42", "+2:05"]

Input: get_relative_results(["0:49:13", "0:49:15", "0:50:14", "0:51:30", "0:51:58", "0:52:16", "0:53:12", "0:53:31", "0:56:19", "1:02:20"]) => Output: ["0", "+0:02", "+1:01", "+2:17", "+2:45", "+3:03", "+3:59", "+4:18", "+7:06", "+13:07"]

Input: get_relative_results(["2:01:15", "2:10:45", "2:10:53", "2:11:04", "2:11:55", "2:13:27", "2:14:30", "2:15:10"]) => Output: ["0", "+9:30", "+9:38", "+9:49", "+10:40", "+12:12", "+13:15", "+13:55"]
```

#

<br />

# 2026.02.11 Challenge - 2026 Winter Games Day 6: Figure Skating

My solution -> *[2026_02_11_2026_winter_games_day_6_figure_skating](2026_02_11_2026_winter_games_day_6_figure_skating.py)*

## **_Task condition:_**

Given an array of judge scores and optional penalties, calculate the final score for a figure skating routine.

The first argument is an array of `10` judge scores, each a number from `0 to 10`. Remove the highest and lowest judge scores and sum the remaining `8` scores to get the base score.

Any additional arguments passed to the function are penalties. Subtract all penalties from the base score to get the final score.

### **_Examples_**

```
Input: compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1) => Output: 64

Input: compute_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) => Output: 80

Input: compute_score([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1) => Output: 67

Input: compute_score([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], 0.5, 1.0) => Output: 67.5

Input: compute_score([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], 1.5, 0.5, 0.5) => Output: 59
```

#

<br />

# 2026.02.12 Challenge - 2026 Winter Games Day 7: Speed Skating

My solution -> *[2026_02_12_2026_winter_games_day_7_speed_skating](2026_02_12_2026_winter_games_day_7_speed_skating.py)*

## **_Task condition:_**

Given two arrays representing the lap times (`in seconds`) for two speed skaters, return the lap number where the difference in lap times is the largest.

The first element of each array corresponds to lap `1`, the second to lap `2`, and so on.

### **_Examples_**

```
Input: largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30]) => Output: 3

Input: largest_difference([27.04, 25.94, 26.22, 26.07, 26.18], [25.59, 25.80, 26.11, 26.01, 26.23]) => Output: 1

Input: largest_difference([25.82, 25.90, 26.05, 26.00, 26.48], [25.85, 25.92, 26.07, 25.98, 25.95]) => Output: 5

Input: largest_difference([25.88, 26.10, 25.95, 26.05, 26.00], [25.90, 26.55, 25.92, 26.03, 26.01]) => Output: 2

Input: largest_difference([25.92, 26.01, 26.05, 25.88, 26.12], [25.95, 26.00, 26.03, 26.45, 26.10]) => Output: 4
```

#

<br />

# 2026.02.13 Challenge - 2026 Winter Games Day 8: Luge

My solution -> *[2026_02_13_2026_winter_games_day_8_luge](2026_02_13_2026_winter_games_day_8_luge.py)*

## **_Task condition:_**

Given an array of five numbers, each representing the time (in seconds) it took a luger to complete a segment of a track, determine which segment had the fastest speed and what that speed was.

The track is divided into the following segments:

- Segment 1: 320 meters
- Segment 2: 280 meters
- Segment 3: 350 meters
- Segment 4: 300 meters
- Segment 5: 250 meters

The first value in the given array corresponds to the time for segment `1`, the second value to segment `2`, and so on.

To calculate the speed (in meters per second) for a segment, divide the distance by the time.

Return `"The luger's fastest speed was X m/s on segment Y."`. Where `X` is the fastest speed, rounded to two decimal places, and `Y` is the segment number where the fastest speed occurred.

### **_Examples_**

```
Input: get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128]) => Output: "The luger's fastest speed was 35.07 m/s on segment 5."

Input: get_fastest_speed([9.381, 7.417, 9.912, 8.815, 7.284]) => Output: "The luger's fastest speed was 37.75 m/s on segment 2."

Input: get_fastest_speed([8.890, 7.601, 9.093, 8.392, 6.912]) => Output: "The luger's fastest speed was 38.49 m/s on segment 3."

Input: get_fastest_speed([8.490, 7.732, 10.103, 8.489, 6.840]) => Output: "The luger's fastest speed was 37.69 m/s on segment 1."

Input: get_fastest_speed([8.204, 7.230, 9.673, 7.645, 6.508]) => Output: "The luger's fastest speed was 39.24 m/s on segment 4."
```

#

<br />

# 2026.02.14 Challenge - 2026 Winter Games Day 9: Skeleton

My solution -> *[2026_02_14_2026_winter_games_day_9_skeleton](2026_02_14_2026_winter_games_day_9_skeleton.py)*

## **_Task condition:_**

Given a string representing the curves on a skeleton track, determine the difficulty of the track.

- The given string will only consist of the letters:
    - `"L"` for a left turn
    - `"R"` for a right turn
    - `"S"` for a straight segment
- Each direction change adds 15 points (an "L" followed by an "R" or vice versa).
- All other curves add 5 points each (all other "L" or "R" characters).
- Straight segments add 0 points.

The difficulty of the track is based on the total score. Return:

- `"Easy"` if the total is `0-100`
- `"Medium"` if the total is `101-200`
- `"Hard"` if the total is over `200`

### **_Examples_**

```
Input: get_difficulty("SLSLLSRRLSRLRL") => Output: "Easy"

Input: get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS") => Output: "Hard"

Input: get_difficulty("SRRRRLSLLRLRSSRLSRL") => Output: "Medium"

Input: get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL") => Output: "Hard"

Input: get_difficulty("SLLSSLRLSLSLRSLSSLRL") => Output: "Medium"

Input: get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR") => Output: "Easy"
```

#

<br />

# 2026.02.15 Challenge - 2026 Winter Games Day 10: Alpine Skiing

My solution -> *[2026_02_15_2026_winter_games_day_10_alpine_skiing](2026_02_15_2026_winter_games_day_10_alpine_skiing.py)*

## **_Task condition:_**

Given a ski hill's vertical drop, horizontal distance, and type, determine the difficulty rating of the hill.

To determine the rating:

- Calculate the steepness of the hill by taking the drop divided by the distance.
- Then, calculate the adjusted steepness based on the hill type:
    - `"Downhill"` multiply steepness by `1.2`
    - `"Slalom"`: multiply steepness by `0.9`
    - `"Giant Slalom"`: multiply steepness by `1.0`

Return:

- `"Green"` if the adjusted steepness is less than or equal to `0.1`
- `"Blue"` if the adjusted steepness is greater than `0.1` and less than or equal to `0.25`
- `"Black"` if the adjusted steepness is greater than `0.25`

### **_Examples_**

```
Input: get_hill_rating(95, 900, "Slalom") => Output: "Green"

Input: get_hill_rating(620, 2800, "Downhill") => Output: "Black"

Input: get_hill_rating(420, 1680, "Giant Slalom") => Output: "Blue"

Input: get_hill_rating(250, 3000, "Downhill") => Output: "Green"

Input: get_hill_rating(110, 900, "Slalom") => Output: "Blue"

Input: get_hill_rating(380, 1500, "Giant Slalom") => Output: "Black"
```

#

<br />

# 2026.02.16 Challenge - 2026 Winter Games Day 11: Ice Hockey

My solution -> *[2026_02_16_2026_winter_games_day_11_ice_hockey](2026_02_16_2026_winter_games_day_11_ice_hockey.py)*

## **_Task condition:_**

Given an array of `6` ice hockey teams and their records after the round robin games, determine the match-ups for the semi-final round.

- Each array item will have a team and their record in the format `"TEAM: W-OTW-OTL-L"`. Where:
    - `"W"` is the number of wins in regulation, worth `3` points each
    - `"OTW"` is the number of overtime wins, worth `2` points each
    - `"OTL"` is the number of overtime losses, worth `1` point each
    - `"L"` is the number of losses, worth `0` points each

For example, `"FIN: 2-2-1-0"` would have `11` points after adding up their record.

Find the total number of points for each team and return `"The semi-final games will be (1st) vs (4th) and (2nd) vs (3rd)."`. For example, `"The semi-final games will be FIN vs SWE and CAN vs USA."`

### **_Examples_**

```
Input: get_semifinal_matchups(["CAN: 2-2-0-1", "FIN: 2-2-1-0", "GER: 1-0-1-3", "SUI: 0-1-3-1", "SWE: 1-1-2-1", "USA: 2-1-0-2"]) => Output: "The semi-final games will be FIN vs SWE and CAN vs USA."

Input: get_semifinal_matchups(["CAN: 2-1-1-1", "CZE: 1-1-1-2", "FIN: 1-2-1-1", "NOR: 0-1-1-3", "SLO: 1-0-1-3", "USA: 5-0-0-0"]) => Output: "The semi-final games will be USA vs CZE and CAN vs FIN."

Input: get_semifinal_matchups(["CAN: 3-2-0-0", "CZE: 2-1-2-0", "LAT: 0-0-1-4", "ITA: 1-1-1-2", "DEN: 1-0-0-4", "USA: 3-1-1-0"]) => Output: "The semi-final games will be CAN vs ITA and USA vs CZE."

Input: get_semifinal_matchups(["AUT: 2-2-1-0", "DEN: 1-0-0-4", "ITA: 1-1-1-2", "JPN: 3-2-0-0", "KOR: 2-1-2-0", "LAT: 0-0-1-4"]) => Output: "The semi-final games will be JPN vs ITA and AUT vs KOR."
```

#

<br />