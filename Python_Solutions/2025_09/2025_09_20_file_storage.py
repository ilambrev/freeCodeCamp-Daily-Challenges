from math import floor

def number_of_files(file_size, file_unit, drive_size_gb):
    pow = 0

    if file_unit == 'B':
        pow = 3
    elif file_unit == 'KB':
        pow = 2
    elif file_unit == 'MB':
        pow = 1

    files_count = floor(drive_size_gb * 1000 ** pow / file_size)

    return files_count

# print(number_of_files(500, "KB", 1))
# print(number_of_files(50000, "B", 1))
# print(number_of_files(5, "MB", 1))
# print(number_of_files(4096, "B", 1.5))
# print(number_of_files(220.5, "KB", 100))
# print(number_of_files(4.5, "MB", 750))