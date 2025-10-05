def has_exoplanet(readings):
    levels = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    average = sum([levels.find(level) for level in readings]) / len(readings)
    target_value = 0.8 * average

    return len([luminosity for luminosity in readings if levels.find(luminosity) <= target_value]) > 0

# print(has_exoplanet("665544554"))
# print(has_exoplanet("FGFFCFFGG"))
# print(has_exoplanet("MONOPLONOMONPLNOMPNOMP"))
# print(has_exoplanet("FREECODECAMP"))
# print(has_exoplanet("9AB98AB9BC98A"))
# print(has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE"))