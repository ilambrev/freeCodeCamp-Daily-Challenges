from math import floor

def number_of_photos(photo_size_mb, drive_size_gb):

    return floor(drive_size_gb / photo_size_mb * 1000)

# print(number_of_photos(1, 1))
# print(number_of_photos(2, 1))
# print(number_of_photos(4, 256))
# print(number_of_photos(3.5, 750))
# print(number_of_photos(3.5, 5.5))