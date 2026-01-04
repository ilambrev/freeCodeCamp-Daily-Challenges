def is_leap_year(year):
    
    return (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0)

# print(is_leap_year(2024))
# print(is_leap_year(2023))
# print(is_leap_year(2100))
# print(is_leap_year(2000))
# print(is_leap_year(1999))
# print(is_leap_year(2040))
# print(is_leap_year(2026))