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

# 2026.02.09 Challenge - 2026 Winter Games Day 3: Biathlon

My solution -> *[2026_02_09_2026_winter_games_day_4_ski_jumping](2026_02_09_2026_winter_games_day_4_ski_jumping.py)*

## **_Task condition:_**

Given `distance points`, `style points`, a `wind compensation value`, and `K-point bonus` value, calculate your score for the ski jump and determine if you won a medal or not.

- Your score is calculated by summing the above four values.

The current total scores of the other jumpers are:

|**165.5**|
|---------|
|**172.0**|
|**158.0**|
|**180.0**|
|**169.5**|
|**175.0**|
|**162.0**|
|**170.0**|

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