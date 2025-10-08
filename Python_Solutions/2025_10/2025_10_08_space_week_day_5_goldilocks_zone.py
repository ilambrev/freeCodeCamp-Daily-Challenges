from math import sqrt

def goldilocks_zone(mass):
    star_luminosity = mass ** 3.5
    zone_start = round(0.95 * sqrt(star_luminosity), 2)
    zone_end = round(1.37 * sqrt(star_luminosity), 2)
    goldilocks_zone = [zone_start, zone_end]

    return goldilocks_zone

# print(goldilocks_zone(1))
# print(goldilocks_zone(0.5))
# print(goldilocks_zone(6))
# print(goldilocks_zone(3.7))
# print(goldilocks_zone(20))